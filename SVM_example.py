#SVM example from http://scikit-learn.org/stable/modules/svm.html#svm-regression

from sklearn import svm
X = [[0, 0], [1, 1]]
y = [0, 1]
clf = svm.SVC()
clf.fit(X, y)

# want to create user entry of values to test as test vector
# also file entry of the training data
# below to allow printing of the results and running the code as a script

test_vector = [[2., 2.]]
result = clf.predict(test_vector)
print(f"Testing test_vector value of {test_vector}")
print(f"Predicts category of result as {result}")

