import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from sklearn.feature_extraction.text import CountVectorizer
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical
from sklearn.preprocessing import LabelEncoder

from keras.models import load_model
data = ["A lot of good things are happening. We are respected again throughout the world, and that's a great thing.@realDonaldTrump"]
max_fatures = 2000
tokenizer = Tokenizer(num_words=max_fatures, split=' ')
tokenizer.fit_on_texts(data)
new_data = tokenizer.texts_to_sequences(data)

new_data = pad_sequences(new_data,maxlen=28)

model = load_model('model.h5')
result=model.predict(X);
print(result)

