import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


train_df = pd.read_csv('E:\python\Python_Lesson4\Python_Lesson4/glass.csv')

x = train_df.drop('Type',axis=1)
y = train_df['Type']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=0)

nb = GaussianNB()
nb.fit(x_train, y_train)

y_pred = nb.predict(x_test)


print(classification_report(y_test,y_pred))
print(accuracy_score(y_test,y_pred))