import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.ndimage import uniform_filter1d


# Die Rohdaten werden eingelesen
data = np.load('ecg_data.npy')
m = np.zeros((13))
h= np.zeros((3))

# Tiefpass-Filter.
m[0]=1
m[6]=-2
m[12]=1
h[0]=1
h[1]=-2
h[2]=1
gefiltert_tp =signal.lfilter(m,h,data)

# Hochpass-Filter.
b = np.zeros((33))
a= np.zeros((2))
b[0]= - 1/32
b[16] = 1
b[17]= -1
b[32]=1/32
a[0]=1
a[1]=-1
gefiltert_hp =signal.lfilter(b,a,gefiltert_tp)

#Signal wird differenziert.
b= np.zeros((5))
b[0]=1/4
b[1]= 1/8
b[3]=-1/8
b[4]= - 1/4
gefiltert_def= signal.lfilter(b,1,gefiltert_hp)

#Signal quadrieren
quadriertes_signal= np.square(gefiltert_def)

#Signal integrieren
window_size = int(0.15 * 200.0)
integrated_signal = uniform_filter1d(quadriertes_signal, window_size)

# Die bearbeiteten Signale werden graphisch dargestellt 
fig, axs = plt.subplots(5, sharex=True, constrained_layout=True)
fig.suptitle('Pan & Tompkins Filter', fontsize='xx-large', weight='extra bold')
axs[0].plot(data)
axs[0].set_title('Rohes EKG')
axs[1].plot(gefiltert_hp)
axs[1].set_title('Gefiltertes EKG')
axs[2].plot(gefiltert_def)
axs[2].set_title('Differenziertes EKG')
axs[3].plot(quadriertes_signal)
axs[3].set_title('Quadriertes EKG')
axs[4].plot(integrated_signal)
axs[4].set_title('Integriertes EKG')
for ax in axs.flat:
    ax.set(xlabel='Zeit Sec')
    ax.set(ylabel='mV')
plt.show()


