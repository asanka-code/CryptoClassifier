import seciqlib
import numpy as np

window = 0.08

# Saving FFT vectors to *.npy files
# =================================

# 3DES
data = seciqlib.getData("./iq-data/3DES/3des-6.cfile")
fftdata = seciqlib.getNormalizedFFTVector(data, 0.53, window)
# save an FFT vector to a *.npy file and load it back
print("fftdata=", fftdata)
print("len(fftdata)=", len(fftdata))
print("max(fftdata)=", max(fftdata))
np.save("3des.1", fftdata)

'''
print("\n Loading...\n")
fftloaded = np.load("1.npy")
print("fftloaded=", fftloaded)
print("len(fftloaded)=", len(fftloaded))
print("max(fftloaded)=", max(fftloaded))
print("\n Converting to Python list...\n")
fftTrace = fftloaded.tolist()
print("type(fftTrace)=", type(fftTrace))
print("len(fftTrace)=", len(fftTrace))
print("max(fftTrace)=", max(fftTrace))
'''

# AES
data = seciqlib.getData("./iq-data/AES/aes-2.cfile")
fftdata = seciqlib.getNormalizedFFTVector(data, 7.40, window)
# save an FFT vector to a *.npy file and load it back
print("fftdata=", fftdata)
print("len(fftdata)=", len(fftdata))
print("max(fftdata)=", max(fftdata))
np.save("aes.1", fftdata)
