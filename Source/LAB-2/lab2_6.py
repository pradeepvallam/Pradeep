# From question 4 and 5, it looks like CNN model models the best for this particular model, so we will use CNN and
# tune the parameters to attain better accuracy

from keras.models import Sequential
from keras import layers
from keras.preprocessing.text import Tokenizer
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from keras import backend as K
K.common.set_image_dim_ordering('th')

# read the file
df = pd.read_csv('train.tsv',
                 header=None,
                 delimiter='\t', low_memory=False)
df.columns = ['PhraseID', 'SentenceID', 'Phrase', 'Sentiment']
sentences = df['Phrase'].values
y = df['Sentiment'].values

tokenizer = Tokenizer(num_words=2000)
tokenizer.fit_on_texts(sentences)
sentences = tokenizer.texts_to_matrix(sentences)


le = preprocessing.LabelEncoder()
y = le.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(sentences, y, test_size=0.25, random_state=1000)

# Number of features
# print(input_dim)
model = Sequential()
# creating more layers to change hyper parameters
model.add(layers.Dense(300, input_dim=2000, activation='relu'))
model.add(layers.Dense(10, activation='relu'))
model.add(layers.Dropout(0.2))
model.add(layers.Dense(1024, activation='relu'))
model.add(layers.Dropout(0.2))
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dropout(0.2))
model.add(layers.Dense(256, activation='relu'))

model.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['acc'])
history=model.fit(X_train,y_train, epochs=5, verbose=True, validation_data=(X_test,y_test), batch_size=256)

