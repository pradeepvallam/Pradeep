import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras import metrics
from keras import regularizers
from keras import optimizers
from keras.callbacks import TensorBoard
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder


dataset = pd.read_csv('/content/african_crises.csv',header=None).values


x_train, x_test, y_train, y_test = train_test_split(dataset[1:,0:13], dataset[1:,13],
                                                    test_size=0.25, random_state=87)
#normalize data
le = LabelEncoder()
x_train[:,1] = le.fit_transform(x_train[:,1])
x_train[:,2] = le.fit_transform(x_train[:,2])
x_test[:,1] = le.fit_transform(x_test[:,1])
x_test[:,2] = le.fit_transform(x_test[:,2])

y_train = y_train.reshape(len(y_train), 1)
y_train = one_hot.fit_transform(y_train)
y_test = y_test.reshape(len(y_test), 1)
y_test = one_hot.fit_transform(y_test)




#create model
model = Sequential()
model.add(Dense(100, input_shape=(13,), activation='softmax'))
model.add(Dense(30,activation='softmax'))
model.add(Dense(2,activation='softmax'))
#compile
model.compile(optimizer='RMSprop', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

#Tensorboard log generation for graphs
tensorboard = TensorBoard(log_dir="logs/",histogram_freq=0, write_graph=True, write_images=True)

#fitting the model
history=model.fit(x_train, y_train, epochs=10, batch_size=128,callbacks=[tensorboard], validation_data=(x_test,y_test))

score = model.evaluate(x_test, y_test, verbose=1)
print('Loss: %.2f, Accuracy: %.2f' % (score[0], score[1]))

#plotting the loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()


