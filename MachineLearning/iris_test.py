import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt

iris_file = 'C:/Users/Kevin/Google Drive/Master Wifo Uni Mannheim/Master Thesis/Resources/Datasets/Iris Data Set/iris.data'
iris = pd.read_csv(iris_file)

x = iris.iloc[:, :4].values
# x = iris.iloc[:, [2, 3]].values  #  use for plotting
y_nom = iris.iloc[:, 4].values
le = preprocessing.LabelEncoder()
le.fit(y_nom)
y = le.transform(y_nom)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=0)

classifier = SVC()
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

print(accuracy_score(y_test, y_pred))


def plot_decision_regions(X, y, classifier,
                          test_idx=None, resolution=0.02):
    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    # plot all samples
    X_test, y_test = X[test_idx, :], y[test_idx]
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1],
                    alpha=0.8, c=cmap(idx),
                    marker=markers[idx], label=cl)
    # highlight test samples
    if test_idx:
        X_test, y_test = X[test_idx, :], y[test_idx]
        plt.scatter(X_test[:, 0], X_test[:, 1], c='',
                    alpha=1.0, linewidth=1, marker='o',
                    s=55, label='test set')


x_combined = np.vstack((x_train, x_test))
y_combined = np.hstack((y_train, y_test))
"""
plot_decision_regions(X=x_combined, 
                      y=y_combined, 
                      classifier=classifier,
                      test_idx=range(y_train.size-1, y_train.size+y_test.size-1))
plt.xlabel('peteal length')
plt.ylabel('petal width')
plt.legend(loc='upper left')
plt.show()
"""