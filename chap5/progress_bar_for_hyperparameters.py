
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from chap4.data_general_class import DataSet

customer_obj = DataSet(feature_list = ["speechiness", "instrumentalness",
                       "uration_ms"],
                      file_name = ".\data\spotify_data\dataset-of-00s.csv",
                      label_col = "target",
                      pos_category = 1
                     ) 


parameters = {"max_depth":range(2, 8),
              "min_samples_leaf": range(5, 55, 5),
              "min_samples_split": range(10, 110, 5),
              "max_features": [2, 3],
              "n_estimators": [100, 150, 200, 250, 300, 350, 400]}


clf = RandomizedSearchCV(RandomForestClassifier(),
                         parameters,
                         n_jobs=4,
                         scoring = "roc_auc",
                         n_iter = 200,
                         random_state = 0,
                         verbose = 1)

clf.fit(customer_obj.train_features, customer_obj.train_labels)