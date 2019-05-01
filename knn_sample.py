import sqlite3
conn = sqlite3.connect('temp.db')
import numpy as np
import matplotlib.pyplot as plt

# In die Datenbank schreiben
c = conn.cursor()

c.execute("INSERT INTO temp (c_value) VALUES (25.9)")
c.execute("SELECT * FROM temp")
werte = c.fetchall()
print(werte)
B=np.array(werte)
print(B)

plt.plot(B)
plt.show()

# print (c.fetchone())
for zeile in c.execute("SELECT * FROM temp"):
  print(zeile)
conn.commit()
conn.close()


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
