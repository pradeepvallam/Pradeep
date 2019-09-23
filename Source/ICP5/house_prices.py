import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

train_df = pd.read_csv('E:\python\Python_Lesson5\Python_Lesson5\houseprices.csv', sep=',', usecols=(62,80))
#scatterplot to find the correlation between saleprice and garagearea
plt.scatter(train_df['SalePrice'], train_df['GarageArea'])
plt.title('original dataset')
plt.xlabel('GaurageArea')
plt.ylabel('SalePrice')
plt.show()

#using z-score method to remove the outliers
z = np.abs(stats.zscore(train_df))
threshold = 3

train_df_mod = train_df[(z < 3).all(axis=1)]
#new scatter plot after removing the outliers
plt.scatter(train_df_mod['SalePrice'], train_df_mod['GarageArea'])
plt.title('modified dataset')
plt.xlabel('GaurageArea')
plt.ylabel('SalePrice')
plt.show()