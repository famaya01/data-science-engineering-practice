

from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from data_general_class import DataSet


"""
This code does the following:

First, we start by importing the RandomizedSearchCV class from scikit-learn. This class is often used for 
hyperparmater tuning to select the optimized parameters for machine learning models.
Second, we define a new class called RandomForestModel.
Within this class, we first create the init method. As done earlier, this takes the inputs to our class. 
This time, the inputs will be the values we need to pass to ultimately train the random forest model with hyperparameter tuning. 
This includes a dictionary of hyperparameters, the number of jobs we want to run in parallel, 
the metric used for evaluation in the tuning, number of iterations to test out various combinations of parameters,
 and a random state value to ensure repeatable results.
Next, we define a method called tune. This method serves as a wrapper function to handle the hyperparameter tuning piece.
 It takes the inputs to the class and trains an optimized model based on the hyperparameter grid that is input to the class.
Lastly, we create a method to handle fetching predictions for the trained model.
"""


class RandomForestModel:

    def __init__(self, 
                 parameters: dict, 
                 n_jobs: int,
                 scoring: str,
                 n_iter: int,
                 random_state: int):
        

        self.parameters = parameters
        self.n_jobs = n_jobs
        self.scoring = scoring
        self.n_iter = n_iter
        self.random_state = random_state
    
    def tune(self, x_features, y):


        self.clf = RandomizedSearchCV(RandomForestClassifier(),
                                      self.parameters,
                                      n_jobs=self.n_jobs,
                                      scoring = self.scoring,
                                      n_iter = self.n_iter,
                                      random_state = self.random_state)

        self.clf.fit(x_features, y)

    def predict(self, x_features):
        return self.clf.predict(x_features)
    


customer_obj = DataSet(feature_list =  ["total_day_minutes", "total_day_calls",
                        "number_customer_service_calls"],
                        file_name = "..\data\train.csv",
                        label_col = "churn",
                        pos_category = "yes"
                        )



parameters = {"max_depth":range(2, 6),
              "min_samples_leaf": range(5, 55, 5),
              "min_samples_split": range(10, 110, 5),
              "max_features": [2, 3, 4, 5, 6],
              "n_estimators": [50, 100, 150, 200]}



forest = RandomForestModel(parameters = parameters,
                           n_jobs = 4,
                           scoring = "roc_auc",
                           n_iter = 10,
                           random_state = 0)

forest.tune(customer_obj.train_features, customer_obj.train_labels)