import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
train = pd.read_csv('E:\python\Python_Lesson5\Python_Lesson5\winequality-red.csv')

##handling missing value
data = train.dropna(axis = 0, how ='any')
##Build a linear model
y = np.log(train.quality)
X = data.drop(['quality'], axis=1)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
                                    X, y, random_state=42, test_size=.33)

from sklearn import linear_model
lr = linear_model.LinearRegression()
model = lr.fit(X_train, y_train)

##Evaluate the performance and visualize results
print ("R^2 is: \n", model.score(X_test, y_test))
predictions = model.predict(X_test)
from sklearn.metrics import mean_squared_error
print ('RMSE is: \n', mean_squared_error(y_test, predictions))

##visualize

actual_values = y_test
plt.scatter(predictions, actual_values, alpha=.75,
            color='b') #alpha helps to show overlapping data
plt.xlabel('Predicted quality')
plt.ylabel('Actual quality')
plt.title('Linear Regression Model')
plt.show()

#using correlation matrix and generating heatwave
corr_matrix = data.corr()
sns.heatmap(corr_matrix)
plt.show()

