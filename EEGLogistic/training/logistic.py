import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from warnings import simplefilter
import joblib

simplefilter(action='ignore', category=FutureWarning)

print("---- Seizure predictor using Logistic Regression -----")

model = pd.read_csv('FEATURE_SET.csv')

print("Columns of Dataset")
print(model.columns)

print("First 5 records of dataset")
print(model.head())

print("Dimension of data: {}".format(model.shape))

X_train, X_test, y_train, y_test = train_test_split(model.loc[:, model.columns != 'y'], model['y'], stratify=model['y'],
                                                    test_size=0.30, random_state=6)
print("X train:\n")
print(X_train)
print("X test:\n")
print(X_test)
print("y train:\n")
print(y_train)
print("y test:\n")
print(y_test)

logreg = LogisticRegression().fit(X_train, y_train)

print("Training set accuracy: {:.3f}".format(logreg.score(X_train, y_train)))

print("Test set accuracy: {:.3f}".format(logreg.score(X_test, y_test)))

filename = 'logisticModel'
joblib.dump(logreg, filename)

print("Training completed {logisticModel generated}")
