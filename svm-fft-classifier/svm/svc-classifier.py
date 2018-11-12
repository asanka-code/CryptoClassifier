from sklearn import svm
import numpy as np
import os

trainingTraces = "./input-traces"
testTraces = "./test-traces"


###############################################################################
# need a function to load data from .npy trace files into the X 2d array and fill
# the relevant element in Y array.
def loadDataToXY():
    pathToNpyFiles = trainingTraces

    # A dictionary to encode the crypto algorithm label with a number 
    cryptoDict = dict()
    # A variable to keep a unique number for each crypto algorithm
    cryptoAlgoCounter = 0
    
    X = []
    Y = [] 

    listOfFiles = os.listdir(pathToNpyFiles)  

    print("number of traces: %d" % len(listOfFiles))

    for fileName in listOfFiles:
        #print (fileName)
        cryptoName, sequenceNumber, extension = fileName.split(".")    
        
        if cryptoName not in cryptoDict:
            cryptoDict[cryptoName] = cryptoAlgoCounter
            cryptoAlgoCounter = cryptoAlgoCounter + 1
            
        fftloaded = np.load(pathToNpyFiles+"/"+fileName)
        fftTrace = fftloaded.tolist()
        X.extend([fftTrace])
        Y.append(cryptoDict[cryptoName])
            
        #if len(X)==50:
        #    break

    print("cryptoDict=", cryptoDict)
    #print("type(X)=", type(X))
    #print("len(X)=", len(X))
    #print("type(Y)=", type(Y))
    #print("len(Y)=", len(Y))
    #print("Y=",Y)       
    return X, Y

    
###############################################################################
# need a function to load test data from .npy trace file
def loadTestData():
    pathToNpyFiles = testTraces
    
    Xtest = []
    Ytest = []
    
    listOfFiles = os.listdir(pathToNpyFiles)  

    print("number of traces: %d" % len(listOfFiles))

    for fileName in listOfFiles:
        #print (fileName)
        cryptoName, sequenceNumber, extension = fileName.split(".")    
        
        #print("cryptoName=%s" % cryptoName)
        fftloaded = np.load(pathToNpyFiles+"/"+fileName)
        fftTrace = fftloaded.tolist()
        Xtest.extend([fftTrace])
        Ytest.append(cryptoName)
        
    return Xtest, Ytest


###############################################################################
# need a function to decide which is the classification result based on the max
# value of the 'dec' array.



###############################################################################
# need a function to plot the results, confusion matrix, etc 



# training samples
print("Loading data...")
X, Y = loadDataToXY()

print("Training classifier...")
# classifier
clf = svm.SVC(gamma='scale', decision_function_shape='ovr')

# training
clf.fit(X, Y) 

print("Testing...")
# testing
Xtest, Ytest = loadTestData()
for i in range(0,len(Xtest)):
    print(i)
    print("Ytest[i]=", Ytest[i])
    dec = clf.decision_function([Xtest[i]])
    print("decision vector=", dec)


#testTrace = loadTestData()
#dec = clf.decision_function([testTrace])
#print("decision vector=", dec)


