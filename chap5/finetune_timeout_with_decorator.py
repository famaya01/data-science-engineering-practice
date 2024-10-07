from stopit import threading_timeoutable as timeoutable
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from chap4.data_general_class import DataSet

@timeoutable()
def finetune_hyperparameters(parameters):
    clf = RandomizedSearchCV(RandomForestClassifier(),
                         parameters,
                         n_jobs=4,
                         scoring = "roc_auc",
                         n_iter = 200,
                         random_state = 0,
                         verbose = 1)
    return clf


customer_obj = DataSet(feature_list = ["speechiness", "instrumentalness",
                       "duration_ms"],
                      file_name = ".\data\spotify_data\dataset-of-00s.csv",
                      label_col = "target",
                      pos_category = 1
                     ) 


parameters = {"max_depth":range(2, 8),
              "min_samples_leaf": range(5, 55, 5),
              "min_samples_split": range(10, 110, 5),
              "max_features": [2, 3],
              "n_estimators": [100, 150, 200, 250, 300, 350, 400]}


clf = finetune_hyperparameters(parameters, timeout=300)
# Did code finish running in under 180 seconds (3 minutes)?
if clf:
    print("FINISHED HYERPARAMETERS TUNING...")
    clf.fit(customer_obj.train_features, customer_obj.train_labels)
# Did code timeout?
else:

    raise AssertionError("DID NOT FINISH HYPERPARAMETERS TUNING WITHIN TIME LIMIT")

