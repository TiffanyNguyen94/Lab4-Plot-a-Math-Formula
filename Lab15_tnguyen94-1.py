"""
Program: Lab 15, Heart  Curve Plot
Author: Tiffany Nguyen
Purpose: This program will plot a heart-shaped curve using a mathmatic formula.
Date: November 22, 2026

Math equation: (x^{2}+y^{2}-25)^{3}-25x^{2}y^{3}=0
"""

import matplotlib.pyplot as plt
import math

x_values = []
y_values = []

for i in range(-200, 201):
    x_values.append(i * 0.05)
    y_values.append(i * 0.05)

z_values = []

for y in y_values:
    row = []
    for x in x_values:
        z = (x**2 + y**2 - 25)**3 - 25 * x**2 * y**3
        row.append(z)
    z_values.append(row)


plt.contour(x_values, y_values, z_values,
            levels=[0], colors="red", linewidths=2)


plt.title("Heart Curve")
plt.xlabel("X Values")
plt.ylabel("Y Values")


plt.grid(True)
plt.axis("equal")


plt.savefig("heart_curve.png")
plt.show()

