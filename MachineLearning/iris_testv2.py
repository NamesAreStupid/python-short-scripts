import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn.model_selection import StratifiedKFold

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

kf = StratifiedKFold(n_splits=10, shuffle=True, random_state=1)
for k, (train, test) in kf.split(x_train, y_train):
    print(k)

y_pred = classifier.predict(x_test)

print(accuracy_score(y_test, y_pred))
