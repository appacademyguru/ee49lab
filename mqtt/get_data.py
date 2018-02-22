import  numpy as np
import matplotlib.pyplot as plt

t = np.arrange(0., 5., 0.2)

plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.xlabel('Time')
plt.ylabel('Power')
plt.title('Power versus Time')
plt.show()
