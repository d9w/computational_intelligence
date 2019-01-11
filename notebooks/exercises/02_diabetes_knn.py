import matplotlib.pyplot as plt
from sklearn import neighbors
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split

diabetes = load_diabetes()

k = 10

X_train, X_test, y_train, y_test = train_test_split(diabetes.data, diabetes.target,
                                                    test_size=0.25)

knn = neighbors.KNeighborsRegressor(n_neighbors=k)
knn.fit(X_train, y_train)
train_score = knn.score(X_train, y_train)
test_score = knn.score(X_test, y_test)
print('k: %d, Train Acc: %.3f, Test Acc: %.3f' % (k, train_score, test_score))

y_pred_train = knn.predict(X_train)
y_pred_test = knn.predict(X_test)

x_axis = 3

plt.figure(figsize=(20, 5))
plt.subplot(1, 2, 1)
plt.plot(X_train[:, x_axis], y_train, 'o', label="data", markersize=10)
plt.plot(X_train[:, x_axis], y_pred_train, 's', label="prediction", markersize=4)
plt.title("KNN [train]")
plt.subplot(1, 2, 2)
plt.plot(X_test[:, x_axis], y_test, 'o', label="data", markersize=10)
plt.plot(X_test[:, x_axis], y_pred_test, 's', label="prediction", markersize=4)
plt.title("KNN [test]");


