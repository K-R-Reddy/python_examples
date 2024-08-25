#Labelled
from sklearn import tree
#types of cars based on Horsepower and no of seats
features=[[100,4],[120,7],[400,2],[800,1],[50,4],[50,7]]
labels=["seden","suv","Super_car","F1","Mini_car","Mini_van"]
#DCT is  supervised algorithm
clf=tree.DecisionTreeClassifier()
clf=clf.fit(features,labels)
#predection part
prediction=clf.predict([[50,6]])
print(prediction)