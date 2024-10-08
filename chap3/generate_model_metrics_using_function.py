
from sklearn import metrics
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd


def get_metrics(model, train_features, test_features, train_labels, test_labels):

    train_pred = model.predict(train_features)
    test_pred = model.predict(test_features)

    print ("printing metric summary ...")

    print("Train Precision = ", metrics.precision_score(train_labels, train_pred))
    print("Train Recall = ", metrics.precision_score(train_labels, train_pred))
    print("Train Accuracy = ", metrics.accuracy_score(train_labels, train_pred))


    print("Train Precision = ", metrics.precision_score(test_labels, test_pred))
    print("Train Recall = ", metrics.precision_score(test_labels, test_pred))
    print("Train Accuracy = ", metrics.accuracy_score(test_labels, test_pred))

    return " ... Metric summary complete!"


train_data = pd.read_csv("data-science-engineering-practice/customer-churn-prediction-2020/train.csv")
test_data = pd.read_csv("data-science-engineering-practice/customer-churn-prediction-2020/test.csv")

print(train_data)
feature_list = ["total_day_minutes", "total_day_calls",
                "number_customer_service_calls"]

train_features = train_data[feature_list]
test_features = test_data[feature_list]

train_labels = train_data.churn.map(lambda key: 1 if key.strip().lower() == "yes" else 0)
test_labels = test_data.churn.map(lambda key: 1 if key.strip().lower() == "yes" else 0)

forest_model = RandomForestClassifier(random_state = 0).fit(train_features,
                                                            train_labels)

logit_model = LogisticRegression().fit(train_features, train_labels)

boosting_model = GradientBoostingClassifier().fit(train_features, train_labels)

for model in [forest_model, logit_model, boosting_model]:

    print(get_metrics(model, train_features, test_features, train_labels, test_labels))



