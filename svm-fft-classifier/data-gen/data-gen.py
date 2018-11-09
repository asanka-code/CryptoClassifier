import seciqlib
import numpy as np

window = 0.08 # Caution: feature vector lenth depends on this window size
windowStep = 0.3

###############################################################################
# 3DES
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



###############################################################################
# AES
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


