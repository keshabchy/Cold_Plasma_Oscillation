#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats  # Although imported, 'stats' is not used in this script
import seaborn as sns # Set the aesthetic style of seaborn plots
sns.set()


# In[2]:


from astropy import constants as const
print(const.m_e)
print(const.e)


# # Electric Field Profile ($\Delta$=0.60)

# In[3]:


# Define physical constants
m = 9.1 * 10**(-31)  # Mass of the electron in kilograms
e = 1.6 * 10**(-19)  # Charge of the electron in coulombs

# Calculate the mass-to-charge ratio of the electron
me = m / e  # m/e

# Define the natural frequency squared (ω₀²) based on the plasma frequency formula
w02 = (4 * np.pi * 10**14 * e**2) / m  # ω₀² = (4π × 10¹⁴ × e²) / m

# Define parameters for modulation and spatial variation
delta = 0.60  # Modulation strength
kx = np.linspace(0.01, 2 * np.pi)  # Wave vector (kx) array from 0.01 to 2π
k = 1  # Wave number (assumed constant)

# Define angular frequencies at different times
w0t = 0         # ωt = 0
w1t = np.pi / 2 # ωt = π/2
w2t = np.pi     # ωt = π

# Calculate the electric field for different angular frequencies
E = -me * w02 * delta * np.sin(kx) * np.cos(w0t) / k   # Electric field for ωt = 0
E1 = -me * w02 * delta * np.sin(kx) * np.cos(w1t) / k  # Electric field for ωt = π/2
E2 = -me * w02 * delta * np.sin(kx) * np.cos(w2t) / k  # Electric field for ωt = π

# Create a figure for the plot
plt.figure(figsize=(12, 8))

# Plot the electric field profiles for different angular frequencies
plt.plot(kx, E, 'k', label=r"$\omega t=0$")        # Black curve for ωt = 0
plt.plot(kx, E1, 'r', label=r"$\omega t=\pi/2$")   # Red curve for ωt = π/2
plt.plot(kx, E2, 'b', label=r"$\omega t=\pi$")     # Blue curve for ωt = π

# Add a legend to label the curves
plt.legend(loc='best')

# Add labels for the axes
plt.xlabel('kx', fontsize=16)                     # Label for the x-axis
plt.ylabel('Electric field', fontsize=16)         # Label for the y-axis

# Customize the appearance of tick marks
plt.tick_params(direction='in')                   # Tick marks pointing inward
plt.xticks(size=16)                               # Font size for x-axis ticks
plt.yticks(size=16)                               # Font size for y-axis ticks

# Add a title to the plot
plt.title('Electric Field Profile ($\Delta$=0.60)', fontsize=16)

# Save the plot as a high-resolution PNG file
plt.savefig('electricfield0.60.png', dpi=600)

# Optionally display the plot (useful for interactive environments)
plt.show()


# # Electric Field Profile ($\Delta$=0.45)

# In[4]:


# Define physical constants
m = 9.1 * 10**(-31)  # Mass of the electron in kilograms
e = 1.6 * 10**(-19)  # Charge of the electron in coulombs

# Calculate the mass-to-charge ratio of the electron
me = m / e  # m/e

# Define the natural frequency squared (ω₀²) based on the plasma frequency formula
w02 = (4 * np.pi * 10**14 * e**2) / m  # ω₀² = (4π × 10¹⁴ × e²) / m

# Define modulation strength and spatial variation
delta = 0.45  # Modulation strength
kx = np.linspace(0.01, 2 * np.pi)  # Wave vector (kx) array from 0.01 to 2π

# Define wave number and angular frequencies
k = 1          # Wave number (assumed constant)
w0t = 0        # ωt = 0
w1t = np.pi / 2 # ωt = π/2
w2t = np.pi    # ωt = π

# Calculate the electric field for different angular frequencies
E = -me * w02 * delta * np.sin(kx) * np.cos(w0t) / k   # Electric field for ωt = 0
E1 = -me * w02 * delta * np.sin(kx) * np.cos(w1t) / k  # Electric field for ωt = π/2
E2 = -me * w02 * delta * np.sin(kx) * np.cos(w2t) / k  # Electric field for ωt = π

# Create a figure for the plot
plt.figure(figsize=(12, 8))

# Plot the electric field profiles for different angular frequencies
plt.plot(kx, E, 'k', label=r"$\omega t=0$")        # Black curve for ωt = 0
plt.plot(kx, E1, 'r', label=r"$\omega t=\pi/2$")   # Red curve for ωt = π/2
plt.plot(kx, E2, 'b', label=r"$\omega t=\pi$")     # Blue curve for ωt = π

# Add a legend to label the curves
plt.legend(loc='best')

# Label the axes
plt.xlabel('kx', fontsize=16)                     # Label for the x-axis
plt.ylabel('Electric field', fontsize=16)         # Label for the y-axis

# Customize the appearance of tick marks
plt.tick_params(direction='in')                   # Tick marks pointing inward
plt.xticks(size=16)                               # Font size for x-axis ticks
plt.yticks(size=16)                               # Font size for y-axis ticks

# Add a title to the plot indicating Δ = 0.45
plt.title('Electric Field Profile ($\Delta$=0.45)', fontsize=16)

# Save the plot as a high-resolution PNG file
plt.savefig('electricfield0.45.png', dpi=600)

# Optionally display the plot (useful for interactive environments)
plt.show()


# # Electric Field Profile ($\Delta$=0)

# In[5]:


# Define physical constants
m = 9.1 * 10**(-31)  # Mass of the electron in kilograms
e = 1.6 * 10**(-19)  # Charge of the electron in coulombs

# Calculate the mass-to-charge ratio of the electron
me = m / e  # m/e

# Define the natural frequency squared (ω₀²) using the plasma frequency formula
w02 = (4 * np.pi * 10**14 * e**2) / m  # ω₀² = (4π × 10¹⁴ × e²) / m

# Set modulation strength to 0 (no modulation)
delta = 0  # Modulation strength, Δ

# Generate wave vector values (kx) from 0.01 to 2π
kx = np.linspace(0.01, 2 * np.pi)  # Avoid starting from 0 to prevent division errors

# Define wave number and angular frequencies
k = 1          # Wave number (assumed constant)
w0t = 0        # ωt = 0
w1t = np.pi / 2 # ωt = π/2
w2t = np.pi    # ωt = π

# Calculate the electric field profiles for different angular frequencies
E = -me * w02 * delta * np.sin(kx) * np.cos(w0t) / k   # Electric field for ωt = 0
E1 = -me * w02 * delta * np.sin(kx) * np.cos(w1t) / k  # Electric field for ωt = π/2
E2 = -me * w02 * delta * np.sin(kx) * np.cos(w2t) / k  # Electric field for ωt = π

# Create a figure with specified dimensions for visualization
plt.figure(figsize=(12, 8))

# Plot the electric field profiles with different colors for each angular frequency
plt.plot(kx, E, 'k', label=r"$\omega t=0$")        # Black curve for ωt = 0
plt.plot(kx, E1, 'r', label=r"$\omega t=\pi/2$")   # Red curve for ωt = π/2
plt.plot(kx, E2, 'b', label=r"$\omega t=\pi$")     # Blue curve for ωt = π

# Add a legend to differentiate the curves
plt.legend(loc='best')  # Automatically choose the best position for the legend

# Add labels for the x and y axes
plt.xlabel('kx', fontsize=16)                     # Label for the x-axis
plt.ylabel('Electric field', fontsize=16)         # Label for the y-axis

# Customize the tick marks on the axes
plt.tick_params(direction='in')                   # Make tick marks point inward
plt.xticks(size=16)                               # Set font size for x-axis ticks
plt.yticks(size=16)                               # Set font size for y-axis ticks

# Add a title indicating Δ = 0 (no modulation)
plt.title('Electric Field Profile ($\Delta$=0)', fontsize=16)

# Save the plot as a high-resolution PNG file
plt.savefig('electricfield0.00.png', dpi=600)

# Optionally display the plot (useful in interactive environments)
plt.show()


# In[ ]:




