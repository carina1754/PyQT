import os
import pandas as pd
import numpy as np
from time import time
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
import math
from sklearn.model_selection import train_test_split
from keras.callbacks import EarlyStopping
from sklearn.preprocessing import StandardScaler
import random
import matplotlib.pyplot as plt
from tqdm import tqdm
from glob import glob
import keras as K
def make_dataset(data, label, window_size=20):
    feature_list = []
    label_list = []
    for i in range(len(data) - window_size):
        feature_list.append(np.array(data.iloc[i:i+window_size]))
        label_list.append(np.array(label.iloc[i+window_size]))
    return np.array(feature_list), np.array(label_list)

scaler = StandardScaler()

early_stopping = EarlyStopping()

start = time()

train = pd.read_csv('data.csv')

from sklearn.model_selection import train_test_split
train,test = train_test_split(train, test_size=0.3, random_state=0)

train_feature = train[['id','open','high','low','tradevol','traceprice']]
train_label = train[['trade']]

train_feature, train_label = make_dataset(train_feature, train_label, 1)

x_train, x_valid, y_train, y_valid = train_test_split(train_feature, train_label, test_size=0.2)

test_feature = test[['id','open','high','low','tradevol','traceprice']]
test_label = test[['trade']]

test_feature, test_label = make_dataset(test_feature, test_label, 1)

print(x_train.shape)
print(y_train.shape)
print(x_valid.shape)
print(y_valid.shape)
#sgd = tf.keras.optimizers.SGD(lr=0.05, decay=1e-6, momentum=0.9, nesterov=True)
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.layers import LSTM

model = Sequential()
model.add(LSTM(32, 
               activation='relu', 
               return_sequences=False)
          )
model.add(Dense(100))
model.add(Dense(50))
model.add(Dense(50))

model.compile(loss='mean_squared_error', optimizer='adam')
early_stop = EarlyStopping(monitor='val_loss', patience=5)

history = model.fit(x_train, y_train, 
                    epochs=10, 
                    batch_size=64,
                    validation_data=(x_valid, y_valid), 
                    )

# 예측
pred = model.predict(test_feature)

plt.plot(test_label, label='actual')
plt.plot(pred, label='prediction')
plt.legend()
plt.show()