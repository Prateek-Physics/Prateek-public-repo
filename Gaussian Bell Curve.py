# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 12:58:35 2024

@author: kotil
"""
%matplotlib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the Gaussian function
def gaussian(x, y, sigma):
    return (1 / ( sigma**2)) * np.exp(- (x**2 + y**2) / (2 * sigma**2))

# Parameters
sigma = 1.0

# Create a grid of (x, y) values
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
x, y = np.meshgrid(x, y)

# Compute the Gaussian function values
z = gaussian(x, y, sigma)

# Create a figure and a 3D Axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(x, y, z, cmap='viridis')

# Labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Gaussian Surface')

plt.show()
