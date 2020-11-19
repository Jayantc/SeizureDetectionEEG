import pandas as pd
from warnings import simplefilter
import joblib

simplefilter(action='ignore', category=FutureWarning)

print("---- Seizure predictor using SVM -----")
modelSvm = pd.read_csv('FEATURE_SET.csv')

print("Columns of Dataset")
print(modelSvm.columns)

print("First 5 records of dataset")
print(modelSvm.head())

print("Dimension of data: {}".format(modelSvm.shape))

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(modelSvm.loc[:, modelSvm.columns != 'y'], modelSvm['y'],
                                                    stratify=modelSvm['y'], test_size=0.30, random_state=6)

print("X train:\n")
print(X_train)
print("X test:\n")
print(X_test)
print("y train:\n")
print(y_train)
print("y test:\n")
print(y_test)

from sklearn.svm import SVC

svmModel = SVC().fit(X_train, y_train)

filename = 'SvmModel'
joblib.dump(svmModel, filename)

print('Accuracy of SVM classifier on training set: {:.2f}'.format(svmModel.score(X_train, y_train)))

print('Accuracy of SVM classifier on test set: {:.2f}'.format(svmModel.score(X_test, y_test)))

print("Training completed {SvmModel generated}")