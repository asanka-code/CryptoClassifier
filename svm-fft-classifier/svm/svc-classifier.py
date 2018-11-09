from sklearn import svm

###############################################################################
# need a function to load data from .npy trace files into the X 2d array and fill
# the relevant element in Y array.


###############################################################################
# need a function to load test data from .npy trace file


###############################################################################
# need a function to decide which is the classification result based on the max
# value of the 'dec' array.



###############################################################################
# need a function to plot the results, confusion matrix, etc 



# training samples
X = [[0,0], [1,1], [2,2], [3,3]]
Y = [0, 1, 2, 3]

# classifier
clf = svm.SVC(gamma='scale', decision_function_shape='ovr')

# training
clf.fit(X, Y) 

# testing
dec = clf.decision_function([[1,1]])
print dec.shape[1] # 4 classes
print dec
dec = clf.decision_function([[2.5,2.9]])
print dec.shape[1] # 4 classes
print dec


