import sklearn

features = [[100,"smooth"],[200,"bumpy"],[120,"smooth"],[220,"bumpy"],[110,"smooth"],[240,"bumpy"]]

labels = ["apple","orange","apple","orange","apple","orange"]

#smooth=0, apple=0
#bumpy=1,orange=1
features = [[100,0],[200,1],[120,0],[220,1],[110,0],[240,1]]
labels = [0,1,0,1,0,1]

from sklearn import tree
clf = tree.DecisionTreeClassifier()

clf = clf.fit(features,labels)

print clf.predict([[160,0]])



