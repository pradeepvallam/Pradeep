import pandas as pd
from sklearn import metrics

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

import seaborn as sns
sns.set(style="white", color_codes=True)
import warnings
warnings.filterwarnings("ignore")

dataset = pd.read_csv('E:\python\Python_Lesson6\Python_Lesson6\CC.csv')
#handling the null values
dataset[1:].fillna((dataset[1:].mean()),inplace=True)

x = dataset.drop(['CUST_ID'],axis=1)
print(x.shape)

nclusters = 3
seed = 0

km = KMeans(n_clusters=nclusters,random_state=seed)
km.fit(x)

y_cluster_kmeans = km.predict(x)
print(y_cluster_kmeans)

wcss = []
for i in range(1,15):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

plt.plot(range(1,15),wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()

score = metrics.silhouette_score(x, y_cluster_kmeans)
print(score)