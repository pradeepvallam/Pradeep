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
from sklearn.preprocessing import MinMaxScaler


dataset = pd.read_csv('sfa.csv',header=None).values
dataset = np.delete(dataset,5,1)

x_train, x_test, y_train, y_test = train_test_split(dataset[1:,0:7], dataset[1:,7],
                                                    test_size=0.25, random_state=87)

#normalize data
scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

#create model
model = Sequential()
model.add(Dense(100, input_shape=(7,), activation='relu'))
model.add(Dense(30,activation='relu'))
model.add(Dense(1,activation='relu'))
#compile
lrate = 0.01
decay = lrate/epochs
sgd = SGD(lr=lrate, momentum=0.9, decay=decay, nesterov=False)
model.compile(optimizer=sgd, loss='mean_squared_error', metrics=['accuracy'])
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


