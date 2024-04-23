import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp, spectrogram
fs = 1000 # Sampling frequency
seconds=120
t = np.linspace(0, seconds, seconds * fs)  # Time array
T=[]
T_N=293
T_cap=473
for i,ts in enumerate(t):
    if i==0:
        T.append(T_N)
        continue
    T_N=T_N+(T_cap-T_N)/(fs*25)
    T.append(T_N)
plt.plot(t,T)
plt.show()
k=0.25*T[-1]/(2*np.pi)
signal=np.sin(T*t/k)
plt.plot(t,signal)
plt.xlim(119,120)
plt.show()
nes=2**13
f, t_spec, Sxx = spectrogram(signal, window='hann',fs=fs, nperseg=nes, nfft=nes,scaling='spectrum')

plt.ylim(0,10)
plt.pcolormesh(t_spec, f, 10*np.log10(Sxx))
plt.colorbar()
plt.show()