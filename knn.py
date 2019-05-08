import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,4*np.pi,1)
y = np.sin(x)
print(x)

plt.title("Werte")
plt.plot(x,y, 'bo')
plt.show()


# Nearest Neighbor
interpol_x = np.arange(0, 4*np.pi,0.1)
for i in interpol_x: # Testpunkte
  distance = 999999  # Distanz auf Maximum setzen
  for k in x:
      if (abs(k - i) < distance):
          interpol_y[i] = y[k]

plt.plot(interpol_x, interpol_y)
plt.show()
