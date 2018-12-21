import seciqlib
import numpy as np
import csv

configFileName = "config.txt"
pathToNpyFiles = "../input-traces"
defaultStartingSequence = 0

window = 0.08 # Caution: feature vector lenth depends on this window size
windowStep = 0.3


###############################################################################
# need a function which reads a config file containing a list of ".cfile" names
# and the cryptographic algorithm name in two columns to call another function
# in a loop which generates ".npy" data segment files with the relevant
# cryptographic algorithm name and the sequence number.
def generateSamples(configFileName, pathToNpyFiles):
    # a dictionary to dynamically keep the starting sequence number of each crypto sample
    crytoDict =	{
    "none": defaultStartingSequence
    }

    # read a line from the config file and extract the file name and crypto name to two variables
    with open(configFileName) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # if the crypto algorithm was encountered for the first time, set the next sequence number to default
            if row['cryto_algorithm'] not in crytoDict:
                crytoDict[row['cryto_algorithm']] = defaultStartingSequence
                
            nextSequence = genNpySamples(int(crytoDict[row['cryto_algorithm']]), row['file_name'], row['cryto_algorithm'], pathToNpyFiles)
            # update the next sequence number of the crypto algorithm
            crytoDict[row['cryto_algorithm']] = nextSequence
    return 1



###############################################################################
# need a function which takes a config file name and a starting sequence to
# generate ".npy" data segment files with the relevant cryptographic algorithm
# name and the sequence number.
def genNpySamples(startSequence, cFileName, cryptoName, pathToNpyFiles):
    #print("genNpySamples()")
    data = seciqlib.getData(cFileName)
    duration = seciqlib.getTimeDuration(data)
    offset = 0
    traceCounter = startSequence
    while (offset+window)<=duration:
        fftdata = seciqlib.getNormalizedFFTVector(data, offset, window)    
        np.save(pathToNpyFiles+"/"+cryptoName+"."+str(traceCounter), fftdata)    
        print("len(fftdata)=", len(fftdata))
        print("offset=", offset)
        offset = offset + windowStep
        traceCounter = traceCounter + 1
    return traceCounter




generateSamples(configFileName, pathToNpyFiles)





###############################################################################
# 3DES
'''
traceCounter = 0
traceName = "./input-traces/3DES/3des"

data = seciqlib.getData("./iq-data/3DES/3des-6.cfile")
duration = seciqlib.getTimeDuration(data)
offset = 0
while (offset+window)<=duration:
    fftdata = seciqlib.getNormalizedFFTVector(data, offset, window)    
    np.save(traceName+"."+str(traceCounter), fftdata)    
    print("len(fftdata)=", len(fftdata))
    print("offset=", offset)
    offset = offset + windowStep
    traceCounter = traceCounter + 1
    

data = seciqlib.getData("./iq-data/3DES/3des-6.cfile")
duration = seciqlib.getTimeDuration(data)
offset = 0
while (offset+window)<=duration:
    fftdata = seciqlib.getNormalizedFFTVector(data, offset, window)    
    np.save(traceName+"."+str(traceCounter), fftdata)    
    print("len(fftdata)=", len(fftdata))
    print("offset=", offset)
    offset = offset + windowStep
    traceCounter = traceCounter + 1
'''


###############################################################################
# AES
'''
traceCounter = 0
traceName = "./input-traces/AES/aes"

data = seciqlib.getData("./iq-data/AES/aes-2.cfile")
duration = seciqlib.getTimeDuration(data)
offset = 0
while (offset+window)<=duration:
    fftdata = seciqlib.getNormalizedFFTVector(data, offset, window)    
    np.save(traceName+"."+str(traceCounter), fftdata)    
    print("len(fftdata)=", len(fftdata))
    print("offset=", offset)
    offset = offset + windowStep
    traceCounter = traceCounter + 1
    

data = seciqlib.getData("./iq-data/AES/aes-2.cfile")
duration = seciqlib.getTimeDuration(data)
offset = 0
while (offset+window)<=duration:
    fftdata = seciqlib.getNormalizedFFTVector(data, offset, window)    
    np.save(traceName+"."+str(traceCounter), fftdata)    
    print("len(fftdata)=", len(fftdata))
    print("offset=", offset)
    offset = offset + windowStep
    traceCounter = traceCounter + 1
'''



