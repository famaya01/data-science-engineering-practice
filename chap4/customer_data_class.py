import pandas as pd
from sklearn.model_selection import train_test_split



"""
This code is a collection of tasks we will convert into a class. 
Currently, this code reads in the customer churn data, gets a subset of features needed, 
splits the data into train and test, and encodes the label for both the train and test datasets.

customer_data = pd.read_csv("../data/
    customer_churn_data.csv")

train_data,test_data = train_test_split(
    customer_data,
    train_size = 0.7,
    random_state = 0)


feature_list = ["total_day_minutes",
    "total_day_calls",
    "number_customer_service_calls"]

train_features = train_data[feature_list]
test_features = test_data[feature_list]

train_labels = train_data.churn.
    map(lambda key: 1 if key == "yes" else 0)
test_labels = test_data.churn.
    map(lambda key: 1 if key == "yes" else 0)
"""
##############################################################################################




class CustomerData():

     def __init__(self, feature_list: list):
          
        self.customer_data =  pd.read_csv("data-science-engineering-practice\data\train.csv")

        self.train_data, self.test_data = train_test_split(self.customer_data,
                                             train_size = 0.7,
                                             random_state = 0)
          
          
        self.train_data = self.train_data.reset_index(drop = True)
        self.test_data = self.test_data.reset_index(drop = True)

        self.feature_list = feature_list

        self.train_features = self.train_data[feature_list]
        self.test_features = self.test_data[feature_list]


        self.train_labels = self.train_data.churn.map(lambda key: 1 if key == "yes" else 0)
        self.test_labels = self.test_data.churn.map(lambda key: 1 if key == "yes" else 0)