import numpy as np
import matplotlib.pyplot as plt

# PLOT SAMPLE FUNKTION

# Bereich und FUnktion angeben
x = np.linspace(0, 3*np.pi, 500)
# x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)

# Plot erstellen
plt.title('Sinus')
plt.plot(x,y)
plt.show()

c_werte =[20, 21, 22, 25, 20, 15, 13, 10, 10, 18, 19]
C=np.array(c_werte)

plt.plot(C)
plt.show()
