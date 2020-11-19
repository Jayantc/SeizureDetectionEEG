import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import joblib

print("---- Seizure predictor using K Nearest neighbour -----")
modelKnn = pd.read_csv('FEATURE_SET.csv')

print("Columns of Dataset")
print(modelKnn.columns)

print("First 5 records of dataset")
print(modelKnn.head())

print("Dimension of data: {}".format(modelKnn.shape))

X_train, X_test, y_train, y_test = train_test_split(modelKnn.loc[:, modelKnn.columns != 'y'], modelKnn['y'],
                                                    stratify=modelKnn['y'], test_size=0.30, random_state=66)

print("X train:\n")
print(X_train)
print("X test:\n")
print(X_test)
print("y train:\n")
print(y_train)
print("y test:\n")
print(y_test)

training_accuracy = []
test_accuracy = []
# try n_neighbors from 1 to 15 
# neighbors_settings = range(1, 15) 
# for n_neighbors in neighbors_settings:
#     print(n_neighbors)
# build the model
#     knn = KNeighborsClassifier(n_neighbors=n_neighbors)
#     knn.fit(X_train, y_train)
# record training set accuracy
#     training_accuracy.append(knn.score(X_train, y_train))
# record test set accuracy
#     test_accuracy.append(knn.score(X_test, y_test))

# plt.plot(neighbors_settings, training_accuracy, label="training accuracy") 
# plt.plot(neighbors_settings, test_accuracy, label="test accuracy") 
# plt.ylabel("Accuracy") 
# plt.xlabel("n_neighbors") 
# plt.legend() 
# plt.savefig('knn_compare_model') 
# plt.show() 

knn = KNeighborsClassifier(n_neighbors=10)

knn.fit(X_train, y_train)

filename = 'knnModel'
joblib.dump(knn, filename)

print('Accuracy of KNN classifier on training set: {:.2f}'.format(knn.score(X_train, y_train)))

print('Accuracy of KNN classifier on test set: {:.2f}'.format(knn.score(X_test, y_test)))

print("Training completed {KnnModel generated}")