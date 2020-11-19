import csv
import math
import statistics
from scipy.stats import * 



#####   TRAINING   ###

import pandas as pd
import numpy as np
import os
import csv

from sklearn.preprocessing import LabelEncoder, StandardScaler

import warnings
warnings.filterwarnings('ignore')


data = pd.read_csv('FEATURE_SET.csv')
data.head()

genre_list = data.iloc[:, -1]
encoder = LabelEncoder()
y = encoder.fit_transform(genre_list)

scaler = StandardScaler()

X = np.array(data.iloc[:, :-1], dtype = float)

print("Training of feature Started")
print("")

from keras import models
from keras import layers

batch_size = 256

model = models.Sequential()

model.add(layers.Dense(8, activation='relu', input_shape=(X.shape[1],)))

model.add(layers.Dense(16, activation='relu'))

model.add(layers.Dense(32, activation='relu'))

model.add(layers.Dense(64, activation='relu'))

model.add(layers.Dense(128, activation='relu'))

model.add(layers.Dense(32, activation='relu'))

model.add(layers.Dense(16, activation='relu'))

model.add(layers.Dense(2, activation='softmax'))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

epochs=20

model.fit(X, y, epochs=epochs)

model.save('CnnModel.h5')
print(' ')
print("Training completed {CnnModel generated}")

########
