#Import required Python libraries
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib


def data_preprocessing(file_path):
    '''Data processing for machine learning model training

        Args:
            file_path (string): Training data file path

        Returns:
            X: Dataframe for training feature set
            Y: Dataframe for target column
    '''
    dataset = pd.read_csv(file_path)
    dataset = dataset.drop(['Unnamed: 0'], axis=1)
    dataset.drop(['marital'],axis=1, inplace=True)
    dataset1 = dataset.iloc[:, 0:7]
    dataset2 = pd.get_dummies(dataset1, columns = ['job'])
    dataset2 = pd.get_dummies(dataset2, columns = ['education'])
    dataset2['housing'] = dataset2['housing'].map({'yes': 1, 'no': 0})
    dataset2['default'] = dataset2['default'].map({'yes': 1, 'no': 0})
    dataset2['loan'] = dataset2['loan'].map({'yes': 1, 'no': 0})
    dataset_response = pd.DataFrame(dataset['response_binary'])
    dataset2 = pd.merge(dataset2, dataset_response, left_index = True, right_index = True)
    array = dataset2.values
    # Features: first 20 columns
    X = array[:,0:-1]
    # Target variable: 'response_binary'
    Y = array[:,-1]
    return X,Y

def train_test_split_dataset(X,Y,test_size=0.20,seed=7):
    '''Split dataset for train and test

        Args:
            X (dataframe): Dataframe for training feature set
            Y (dataframe): Dataframe for target column
            test_size (int): The proportion of the dataset to include in the test split. Default is 0.20
            seed (int): The seed used by the random number generator

        Returns:
            X_train: feature set for training
            X_test: Dataframe for model performance testing
            Y_train: target for model training
            Y_test: target for model performance testing
    '''
    X_train, X_test, Y_train, Y_test= train_test_split(X, Y, test_size=test_size, random_state=seed)
    return X_train, X_test, Y_train, Y_test

def train_model(file_path):
    X,Y = data_preprocessing(file_path)
    X_train, X_test, Y_train, Y_test = train_test_split_dataset(X,Y,0.30,8)
    LR = LogisticRegression()
    LR.fit(X_train, Y_train)
    predictions = LR.predict(X_test)
    # Accuracy Score 
    print("Accuracy Score for Logistic Regression Model " , accuracy_score(Y_test, predictions))
    return LR

if __name__ == '__main__':
    model = train_model("data/bank.csv")
    # Export the model to a file
    joblib.dump(model, 'model/model_v2.joblib')
    print('Model trained and saved')

