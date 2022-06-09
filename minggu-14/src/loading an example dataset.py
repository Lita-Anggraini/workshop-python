#In[1]
from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()

#In[2]
print(digits.data)

#In[3]
digits.target

#In[4]
digits.images[0]

#In[5]
from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100.)

#In[6]
clf.fit(digits.data[:-1] ,digits.target[:-1])

#In[7]
clf.predict(digits.data[-1:])

#In[8]
import numpy as np
from sklearn import kernel_approximation
rng = np.random.RandomState(0)
X = rng.rand(10, 200)
X = np.array(X, dtype='float32')
X.dtype

#In[9]
transformer = kernel_approximation.RBFSampler()
X_new = transformer.fit_transform(X)
X_new.dtype

#In[10]
from sklearn import datasets
from sklearn.svm import SVC 
iris = datasets.load_iris() 
clf = SVC ()
clf.fit(iris.data, iris.target)

#In[11]
list(clf.predict(iris.data[:3]))

#In[12]
clf.fit(iris.data, iris.target_names[iris.target])

#In[13]
list(clf.predict(iris.data[:3]))

#In[14] 
import numpy as np
from sklearn.datasets import load_iris
from sklearn.svm import SVC 
X, y = load_iris(return_X_y=True)

#In[15]
clf = SVC ()
clf.set_params(kernel='linear').fit(X, y)

#In[16]
clf.predict(X[:5])

#In[17]
clf.set_params(kernel='rbf').fit(X, y)

#In[18]
clf.predict(X[:5])

#In[19]
from sklearn.svm import SVC 
from sklearn.multiclass import OneVsRestClassifier 
from sklearn.preprocessing import LabelBinarizer
X = [[1, 2], [2,4],[4,5],[3,2],[3,1]]
y = [0,0,1,1,2]
classif = OneVsRestClassifier(estimator=SVC(random_state=0))
classif.fit(X,y).predict(X)

#In[20]
y = LabelBinarizer().fit_transform(y)
classif.fit(X, y).predict(X)

#In[21]
from sklearn.preprocessing import MultiLabelBinarizer
y = [[0,1],[0,2],[1,3],[0,2,3],[2,4]]
y = MultiLabelBinarizer().fit_transform(y)
classif.fit(X,y).predict(X)
# %%
