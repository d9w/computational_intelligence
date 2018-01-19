import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

iris = datasets.load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7)

# Encode class labels as binary vector (with exactly ONE bit set to 1, and all others to 0)
Y_train_OneHot = np.eye(4)[y_train]
Y_test_OneHot = np.eye(4)[y_test]

clf = MLPClassifier(hidden_layer_sizes=(4,), solver='sgd', 
                    batch_size=4, learning_rate_init=0.005,
                    max_iter=500, shuffle=True)
clf.fit(X_train, Y_train_OneHot)
print("Number of layers: ", clf.n_layers_)
print("Number of outputs: ", clf.n_outputs_)
h = np.argmax(clf.predict(X_train), axis=1)
fig, ax = plt.subplots(1, 2, figsize=(16, 6))
ax[0].scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap="viridis")
ax[0].set_title("Data");
ax[1].scatter(X_train[:, 0], X_train[:, 1], c=h, cmap="viridis")
ax[1].set_title("Prediction");
print("Train accuracy: ", clf.score(X_train, Y_train_OneHot), " test accuracy:", clf.score(X_test,Y_test_OneHot))
