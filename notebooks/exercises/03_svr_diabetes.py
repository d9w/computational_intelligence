import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

diabetes = datasets.load_diabetes()
feature = 3

X = diabetes.data
y = diabetes.target

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.25,
                                                    random_state=1234)
# Fit regression model
svr_lin = SVR(kernel='linear')
svr_rbf = SVR(kernel='rbf', gamma=0.1)
svr_poly = SVR(kernel='poly', degree=2)
y_lin = svr_lin.fit(X_train, y_train).predict(X_train)
y_rbf = svr_rbf.fit(X_train, y_train).predict(X_train)
y_poly = svr_poly.fit(X_train, y_train).predict(X_train)

print("Linear train error: ", mean_squared_error(y_train, y_lin),
      " test error: ", mean_squared_error(y_test, svr_lin.predict(X_test)))

print("RBF train error: ", mean_squared_error(y_train, y_rbf),
      " test error: ", mean_squared_error(y_test, svr_rbf.predict(X_test)))

print("Polynomial train error: ", mean_squared_error(y_train, y_poly),
      " test error: ", mean_squared_error(y_test, svr_rbf.predict(X_test)))

plt.figure(figsize=(20,10))
plt.scatter(X_train[:, feature], y_train, color='darkorange', label='data')
plt.scatter(X_train[:, feature], y_lin, color='c', label='Linear model')
plt.scatter(X_train[:, feature], y_rbf, color='navy', label='RBF model')
plt.scatter(X_train[:, feature], y_poly, color='cornflowerblue', label='Polynomial model')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Support Vector Regression')
plt.legend()
plt.show()
