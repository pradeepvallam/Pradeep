import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn import metrics
warnings.filterwarnings("ignore")

sns.set(color_codes=True)

# reading the data
glass = pd.read_csv('glass.csv')
x = glass.iloc[:, 1:]
x = x.apply(lambda x: x.fillna(x.mean()), axis=0)

# fit the data model into scaler
scaler = StandardScaler()
scaler.fit(x)
x_scaler = scaler.transform(x)

# building the model - 4 is the best number of clusters according to elbow method
kclusters = 4
km = KMeans(n_clusters=kclusters)
km.fit(x_scaler)


# predict the cluster for each data point
y_cluster_kmeans = km.predict(x_scaler)
score = metrics.silhouette_score(x_scaler, y_cluster_kmeans)
print("The Silhouette Score is: ", score)

# elbow plot visualized
wcss = []
for i in range(1,12):
    kmeans = KMeans(n_clusters=i, max_iter=300, random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

plt.plot(range(1,12),wcss)
plt.title("Elbow Method")
plt.xlabel("# of clusters")
plt.ylabel("WCSS")
plt.show()