from sklearn import svm
import numpy as np

###############################################################################
# need a function to load data from .npy trace files into the X 2d array and fill
# the relevant element in Y array.
def loadDataToXY():
    X = []
    Y = []    
    # loading 3DES data in a loop (file names should be enumerated like 1.npy, 2.pny)
    for i in range(0,5): # instead of range, take the number of .npy files
        fftloaded = np.load("3des.1.npy")
        fftTrace = fftloaded.tolist()
        #print("type(fftTrace)=", type(fftTrace))
        #print("len(fftTrace)=", len(fftTrace))
        X.extend([fftTrace])
        #print("type(X)=", type(X))
        #print("len(X)=", len(X))
        Y.append(0) # the label 3DES is represented by 0

    # loading AES data in a loop (file names should be enumerated like 1.npy, 2.pny)
    for i in range(0,5): # instead of range, take the number of .npy files
        fftloaded = np.load("aes.1.npy")
        fftTrace = fftloaded.tolist()
        #print("type(fftTrace)=", type(fftTrace))
        #print("len(fftTrace)=", len(fftTrace))
        X.extend([fftTrace])
        #print("type(X)=", type(X))
        #print("len(X)=", len(X))
        Y.append(1) # the label AES is represented by 0 
        
    # loading RSA data in a loop (file names should be enumerated like 1.npy, 2.pny)
    for i in range(0,5): # instead of range, take the number of .npy files
        fftloaded = np.load("fft-segment.npy")
        fftTrace = fftloaded.tolist()
        #print("type(fftTrace)=", type(fftTrace))
        #print("len(fftTrace)=", len(fftTrace))
        X.extend([fftTrace])
        #print("type(X)=", type(X))
        #print("len(X)=", len(X))
        Y.append(2) # the label RSA is represented by 0  
        
    print("type(X)=", type(X))
    print("len(X)=", len(X))
    print("type(Y)=", type(Y))
    print("len(Y)=", len(Y))
    print("Y=",Y)   
    return X, Y
    
###############################################################################
# need a function to load test data from .npy trace file
def loadTestData():
    fftloaded = np.load("3des.1.npy")
    fftTrace = fftloaded.tolist()
    return fftTrace



###############################################################################
# need a function to decide which is the classification result based on the max
# value of the 'dec' array.



###############################################################################
# need a function to plot the results, confusion matrix, etc 



# training samples
print("Loading data...")
X, Y = loadDataToXY()
#X = [[0,0], [1,1], [2,2], [3,3]]
#Y = [0, 1, 2, 3]
#print("type(X)=", type(X))
#print("type(Y)=", type(Y))

print("Training classifier...")
# classifier
clf = svm.SVC(gamma='scale', decision_function_shape='ovr')

# training
clf.fit(X, Y) 

print("Testing...")
# testing
testTrace = loadTestData()
dec = clf.decision_function([testTrace])
#dec = clf.decision_function([[1,1]])
#print dec.shape[1] # 4 classes
print("decision vector=", dec)
#dec = clf.decision_function([[2.5,2.9]])
#print dec.shape[1] # 4 classes
#print dec


