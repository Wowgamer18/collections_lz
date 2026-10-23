import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 6, 1)
x1 = np.arange(1, 6, 1)

y = x**2
y1 = x**3
y2 = np.exp(x)
y3 = np.log(x1)

plt.title("Графики функций: x^2, x^3, e^x, ln(x)", color = '#173554', fontstyle = "italic", fontweight = "bold")
plt.xlabel("Ось x")
plt.ylabel("Ось y")
plt.ylim(-4, 15)
plt.axhline(0, color = "black", linewidth = 1.5)
plt.axvline(0, color = "black", linewidth = 1.5)
ax = plt.gca()
ax.set_facecolor("#ebff91")
plt.gcf().set_facecolor("#ebff91")
plt.plot(x, y, label = "y = x^2", color = "blue", marker='o', markersize=4)
plt.plot(x, y1, label = "y = x^3", color = "green", marker='x', markersize=5)
plt.plot(x, y2, label = "y = e^x", color = "red", marker='^', markersize=5)
plt.plot(x1, y3, label = "y = ln(x)", color = "purple", marker='*', markersize=5)
plt.legend()
plt.show()