import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

train_df = pd.read_csv('E:\python\lab\lab_bankdataset.csv')

#handling null values
data = train_df.dropna(axis = 0, how ='any')
#encoding the dataset for categorical values
df = pd.get_dummies(data, prefix_sep='_', drop_first=True)
corr_matrix = df.corr() #there are no columns which are highly correlated to target variable so none are dropped

x = df.drop("y_yes",axis=1)
y = df["y_yes"]
#splitting training and test data
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=0)
#naivebayes method
nb = GaussianNB()
nb.fit(x_train, y_train)
y_pred_naivebayes = nb.predict(x_test)

#SVM method
svc = LinearSVC()
svc.fit(x_train, y_train)
y_pred_svm = svc.predict(x_test)

#KNN method
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train)
y_pred_knn = knn.predict(x_test)
#correlation matrix and heat wave
print(corr_matrix["y_yes"].sort_values(ascending=False))
sns.heatmap(corr_matrix)
plt.show()
#classification report
print("classification report for naivebayes:",classification_report(y_test,y_pred_naivebayes))
print("classification report for svm:",classification_report(y_test,y_pred_svm))
print("classification report for knn:",classification_report(y_test,y_pred_knn))

#confusion matrix
print("confusion matrix for naivebayes:",confusion_matrix(y_test,y_pred_naivebayes))
print("confusion matrix for svm:",confusion_matrix(y_test,y_pred_svm))
print("confusion matrix for knn:",confusion_matrix(y_test,y_pred_knn))

#accuracy score
print("accuracy score for naivebayes:",accuracy_score(y_test,y_pred_naivebayes))
print("accuracy score for svm:",accuracy_score(y_test,y_pred_svm))
print("accuracy score for KNN:",accuracy_score(y_test,y_pred_knn))


