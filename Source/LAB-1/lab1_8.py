import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error


plt.style.use(style='seaborn-ticks')
plt.rcParams['figure.figsize'] = (10,7)

# reading the data from the world happiness report from 2015
# credit for dataset goes to Kaggle
happiness = pd.read_csv('2015.csv')

happiness.Happiness_Score.describe()

# skewing the data
print("Skew is: ", happiness.Happiness_Score.skew())
plt.hist(happiness.Happiness_Score, color='orange')
plt.show()

target = np.log(happiness.Happiness_Score)
print("Skew for target is: ", target.skew())
plt.hist(target, color='pink')
plt.show()

# features (numeric)
numeric_features = happiness.select_dtypes(include=[np.number])

ncorr = numeric_features.corr()

print(ncorr['Happiness_Score'].sort_values(ascending=False)[:10], '\n')
print(ncorr['Happiness_Score'].sort_values(ascending=False)[-10:])

# Nulls - there are no null values in this data, but if there were this would catch them and print the count
nulls = pd.DataFrame(happiness.isnull().sum().sort_values(ascending=False)[:25])
nulls.index.name = 'Nulls'
print(nulls)

happinessdata = happiness.select_dtypes(include=[np.number]).interpolate()
print(sum(happinessdata.isnull().sum()!=0))

# linear model
y_axis = np.log(happiness.Happiness_Score)
x_axis = happinessdata.drop(['Happiness_Score'], axis=1)
X_train, X_test, y_train, y_test = train_test_split(
                                    x_axis, y_axis, test_size=.33)
linearmodel = linear_model.LinearRegression()
model = linearmodel.fit(X_train, y_train)

# Results
print("R^2 is: ", model.score(X_test, y_test))
predictions = model.predict(X_test)
print('RMSE is: ', mean_squared_error(y_test, predictions))