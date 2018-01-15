import matplotlib.pyplot as plt
from sklearn import neighbors
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()

k = 4

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target,
                                                    test_size=0.25)

knn = neighbors.KNeighborsClassifier(n_neighbors=k, weights='uniform')
knn.fit(X_train, y_train)
train_score = knn.score(X_train, y_train)
test_score = knn.score(X_test, y_test)
print('k: %d, Train Acc: %.3f, Test Acc: %.3f' % (k, train_score, test_score))

train_labels = knn.predict(X_train)
test_labels = knn.predict(X_test)

plt.figure(figsize=(20,10))
plt.subplot(2, 2, 1)
plt.scatter(X_train[:,0], X_train[:,1], c=y_train)
plt.title("Real labels [train]")
plt.subplot(2, 2, 2)
plt.scatter(X_train[:,0], X_train[:,1], c=train_labels)
plt.title("KNN [train]")
plt.subplot(2, 2, 3)
plt.scatter(X_test[:,0], X_test[:,1], c=y_test)
plt.title("Real labels [test]")
plt.subplot(2, 2, 4)
plt.scatter(X_test[:,0], X_test[:,1], c=test_labels)
plt.title("KNN [test]");
