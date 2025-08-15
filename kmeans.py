import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
data = pd.read_csv("Mall_Customers.csv")
features = data.select_dtypes(include=[np.number])
pca = PCA(n_components=2)
features_2d = pca.fit_transform(features)
inertia_values = []
k_values = range(2, 11)
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(features)
    inertia_values.append(kmeans.inertia_)

plt.plot(k_values, inertia_values, marker='o')
plt.title("Elbow Method - Optimal K")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.show()
optimal_k = 5
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
cluster_labels = kmeans.fit_predict(features)
data['Cluster'] = cluster_labels
score = silhouette_score(features, cluster_labels)
print(f"Silhouette Score: {score:.4f}")
plt.scatter(features_2d[:, 0], features_2d[:, 1], c=cluster_labels, cmap='rainbow', edgecolors='k')
plt.title("K-Means Clustering (PCA Visualization)")
plt.xlabel("PCA Feature 1")
plt.ylabel("PCA Feature 2")
plt.show()
data.to_csv("Clustered_Customers.csv", index=False)
print("Clustered data saved to 'Clustered_Customers.csv'")
