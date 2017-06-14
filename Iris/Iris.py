from sklearn.datasets import load_iris

iris  = load_iris()

print iris.feature_names

print iris.target_names

print iris.data[0]

print iris.data[149]

print iris.target[0],iris.target[50],iris.target[149]

for i in range(len(iris.target)):
    print "Example %d: label %s, features %s" % (i,iris.target[i],iris.data[i])

import numpy as np

test_idx = [0,50,100]

#training data
train_target = np.delete(iris.target,test_idx)
train_data = np.delete(iris.data,test_idx,axis=0)

#testing data
test_target = iris.target[test_idx] 
test_data = iris.data[test_idx]

from sklearn import tree
clf = tree.DecisionTreeClassifier()

clf = clf.fit(train_data,train_target)

print test_target

print clf.predict(test_data)


