import pandas as pd
from tqdm import tqdm
from sklearn.linear_model import SGDClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

class Chunk_pipeline:

    def __init__(self, filename: str, label: str, 
                 numeric_signals: list, cat_signals: list,
                 chunksize: int):
        self.filename = filename
        self.label = label
        self.numeric_signals = numeric_signals
        self.cat_signals = cat_signals
        self.keep_cols = [self.label] + self.numeric_signals + self.cat_signals
        self.chunksize = chunksize
    
    def get_chunks(self):
        return pd.read_csv(self.filename, 
                            chunksize=self.chunksize,
                            usecols=self.keep_cols)
    
    def train_model(self):
        data_chunks = self.get_chunks()
        sgd_model = SGDClassifier(random_state=0, loss="log", n_jobs=-1)
        
        keep_fields = []
        X_train, y_train = [], []
        X_test, y_test = [], []
        
        # Split a chunk for testing purposes
        test_chunk = None

        for frame in tqdm(data_chunks):
            features = pd.concat([frame[self.numeric_signals], 
                                  pd.get_dummies(frame[self.cat_signals])],
                                 axis=1)
            
            if not keep_fields:
                for signal in self.cat_signals:
                    top_categories = set(frame[signal].value_counts().head().index.tolist())
                    fields = [field for field in features.columns.tolist() if field in top_categories]
                    keep_fields.extend(fields)
                
                keep_fields.extend(self.numeric_signals)

            # Split the first chunk as test data
            if test_chunk is None:
                X_test = pd.concat([frame[self.numeric_signals], 
                                    pd.get_dummies(frame[self.cat_signals])],
                                   axis=1)
                y_test = frame[self.label]
                test_chunk = True
                continue
            
            # Prepare data for training
            X_train.append(features[keep_fields])
            y_train.append(frame[self.label])
        
        # Concatenate collected data for training
        X_train = pd.concat(X_train, ignore_index=True)
        y_train = pd.concat(y_train, ignore_index=True)
        
        # Train the model incrementally
        sgd_model.partial_fit(X_train[keep_fields], y_train, classes=(0, 1))
        self.sgd_model = sgd_model
        
        # Calculate metrics on test data
        self.get_model_metrics(X_train[keep_fields], y_train, X_test[keep_fields], y_test)
    
    def get_model_metrics(self, X_train: pd.DataFrame, y_train: pd.Series, 
                          X_test: pd.DataFrame, y_test: pd.Series):
        """Calculate and print evaluation metrics for the model."""
        if not hasattr(self, 'sgd_model'):
            raise ValueError("Model has not been trained.")
        
        # Ensure the test data matches the training data columns
        X_test = X_test.reindex(columns=self.sgd_model.feature_names_in_, fill_value=0)
        X_train = X_train.reindex(columns=self.sgd_model.feature_names_in_, fill_value=0)
        
        # Make predictions
        train_pred = self.sgd_model.predict(X_train)
        test_pred = self.sgd_model.predict(X_test)
        
        # Calculate metrics
        train_precision = metrics.precision_score(y_train, train_pred)
        test_precision = metrics.precision_score(y_test, test_pred)
        train_accuracy = metrics.accuracy_score(y_train, train_pred)
        test_accuracy = metrics.accuracy_score(y_test, test_pred)
        train_recall = metrics.recall_score(y_train, train_pred)
        test_recall = metrics.recall_score(y_test, test_pred)
        train_f1 = metrics.f1_score(y_train, train_pred)
        test_f1 = metrics.f1_score(y_test, test_pred)
        
        print("Train precision = ", train_precision)
        print("Test precision = ", test_precision)
        print("Train accuracy = ", train_accuracy)
        print("Test accuracy = ", test_accuracy)
        print("Train recall = ", train_recall)
        print("Test recall = ", test_recall)
        print("Train F1 score = ", train_f1)
        print("Test F1 score = ", test_f1)

# Example usage
pipeline = Chunk_pipeline(
    filename="data/ads_train_data.csv",  # Your dataset file
    label="click",                      # Target label column
    numeric_signals=["banner_pos"],     # Numeric features
    cat_signals=["site_category"],      # Categorical features
    chunksize=1000000                   # Size of each data chunk
)

pipeline.train_model()
