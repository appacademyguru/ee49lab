import pickle
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np

import pickle


with open('wigglesc.pkl', 'rb') as f:
    data = pickle.load(f)
x=data['time']
y=data['cos']
plt.plot(x, y, label='time')
plt.show()
