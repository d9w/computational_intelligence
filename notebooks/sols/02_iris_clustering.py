from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3)
clusters = kmeans.fit_predict(iris.data)

x_index = 0
y_index = 1

kmeans = KMeans(n_clusters=3)
labels = kmeans.fit_predict(iris.data)
plt.scatter(iris.data[:, x_index], iris.data[:, y_index], c=labels);
