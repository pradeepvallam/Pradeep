from keras.models import Sequential
from keras import layers
from keras.preprocessing.text import Tokenizer
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

# read the file
df = pd.read_csv('train.tsv',
                 header=None,
                 delimiter='\t', low_memory=False)
# labels columns
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
model.add(layers.Dense(300, input_dim=2000, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))
model.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['acc'])
history=model.fit(X_train,y_train, epochs=5, verbose=True, validation_data=(X_test,y_test), batch_size=256)
