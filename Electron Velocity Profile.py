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


# # Electron Velocity Profile ($\Delta$=0.60)

# In[3]:


# Define physical constants
m = 9.1 * 10**(-31)  # Mass of the electron in kilograms
e = 1.6 * 10**(-19)  # Charge of the electron in coulombs

# Create a figure for the plot
plt.figure(figsize=(12, 8))  # Set figure size to 12x8 inches

# Calculate the natural angular frequency squared (ω₀²) and take its square root (ω₀)
w0 = (4 * np.pi * 10**14 * e**2) / m  # ω₀² = (4π × 10¹⁴ × e²) / m
w02 = np.sqrt(w0)                     # ω₀ = √(ω₀²)

# Set modulation strength
delta = 0.60  # Modulation strength, Δ

# Define wave number
k = 1  # Wave number (assumed constant)

# Generate wave vector values (kx) from 0.01 to 2π
kx = np.linspace(0.01, 2 * np.pi)  # Avoid starting at 0 to prevent division by zero

# Define angular frequencies (ωt) for different phases
omegat = 0               # ωt = 0
omegat1 = np.pi / 2      # ωt = π/2
omegat2 = (3 * np.pi) / 2 # ωt = 3π/2

# Calculate the electron velocity for different phases
ve = w02 * delta * np.sin(kx) * np.sin(omegat) / k    # Velocity for ωt = 0
ve1 = w02 * delta * np.sin(kx) * np.sin(omegat1) / k  # Velocity for ωt = π/2
ve2 = w02 * delta * np.sin(kx) * np.sin(omegat2) / k  # Velocity for ωt = 3π/2

# Plot the velocity profiles with different colors for each phase
plt.plot(kx, ve, 'k', label=r"$\omega t=0$")            # Black curve for ωt = 0
plt.plot(kx, ve1, 'b', label=r"$\omega t=\pi/2$")       # Blue curve for ωt = π/2
plt.plot(kx, ve2, 'r', label=r"$\omega t=3\pi/2$")      # Red curve for ωt = 3π/2

# Add a legend to label the curves
plt.legend(loc='best')  # Automatically choose the best location for the legend

# Label the axes
plt.xlabel('kx', fontsize=16)        # Label for the x-axis
plt.ylabel('Velocity', fontsize=16)  # Label for the y-axis

# Customize the appearance of tick marks
plt.tick_params(direction='in')      # Make tick marks point inward
plt.xticks(size=16)                  # Set font size for x-axis ticks
plt.yticks(size=16)                  # Set font size for y-axis ticks

# Add a title to the plot indicating Δ = 0.60
plt.title('Electron Velocity Profile ($\Delta$=0.60)', fontsize=16)

# Save the plot as a high-resolution PNG file
plt.savefig('velocity0.60.png', dpi=600)  # Save the plot with 600 DPI resolution

# Optionally display the plot (useful for interactive environments)
plt.show()


# # Electron Velocity Profile ($\Delta$=0.45)

# In[4]:


# Define physical constants
m = 9.1 * 10**(-31)  # Mass of the electron in kilograms
e = 1.6 * 10**(-19)  # Charge of the electron in coulombs

# Create a figure for the plot
plt.figure(figsize=(12, 8))  # Set figure size to 12x8 inches

# Calculate the natural angular frequency squared (ω₀²) and its square root (ω₀)
w0 = (4 * np.pi * 10**14 * e**2) / m  # ω₀² = (4π × 10¹⁴ × e²) / m
w02 = np.sqrt(w0)                     # ω₀ = √(ω₀²)

# Set modulation strength
delta = 0.45  # Modulation strength, Δ

# Define wave number
k = 1  # Wave number (assumed constant)

# Generate wave vector values (kx) from 0.01 to 2π
kx = np.linspace(0.01, 2 * np.pi)  # Avoid starting at 0 to prevent division by zero

# Define angular frequencies (ωt) for different phases
omegat = 0               # ωt = 0
omegat1 = np.pi / 2      # ωt = π/2
omegat2 = (3 * np.pi) / 2 # ωt = 3π/2

# Calculate the electron velocity for different phases
ve = w02 * delta * np.sin(kx) * np.sin(omegat) / k    # Velocity for ωt = 0
ve1 = w02 * delta * np.sin(kx) * np.sin(omegat1) / k  # Velocity for ωt = π/2
ve2 = w02 * delta * np.sin(kx) * np.sin(omegat2) / k  # Velocity for ωt = 3π/2

# Plot the velocity profiles with different colors for each phase
plt.plot(kx, ve, 'k', label=r"$\omega t=0$")             # Black curve for ωt = 0
plt.plot(kx, ve1, 'b', label=r"$\omega t=\pi/2$")        # Blue curve for ωt = π/2
plt.plot(kx, ve2, 'r', label=r"$\omega t=3\pi/2$")       # Red curve for ωt = 3π/2

# Add a legend to label the curves
plt.legend(loc='best')  # Automatically choose the best location for the legend

# Label the axes
plt.xlabel('kx', fontsize=16)        # Label for the x-axis
plt.ylabel('Velocity', fontsize=16)  # Label for the y-axis

# Customize the appearance of tick marks
plt.tick_params(direction='in')      # Make tick marks point inward
plt.xticks(size=16)                  # Set font size for x-axis ticks
plt.yticks(size=16)                  # Set font size for y-axis ticks

# Add a title to the plot indicating Δ = 0.45
plt.title('Electron Velocity Profile ($\Delta$=0.45)', fontsize=16)

# Save the plot as a high-resolution PNG file
plt.savefig('velocity0.45.png', dpi=600)  # Save the plot with 600 DPI resolution

# Optionally display the plot (useful for interactive environments)
plt.show()


# # Electron Velocity Profile ($\Delta$=0)

# In[5]:


# Define physical constants
m = 9.1 * 10**(-31)  # Mass of the electron in kilograms
e = 1.6 * 10**(-19)  # Charge of the electron in coulombs

# Create a figure for the plot
plt.figure(figsize=(12, 8))  # Set figure size to 12x8 inches

# Calculate the natural angular frequency squared (ω₀²) and its square root (ω₀)
w0 = (4 * np.pi * 10**14 * e**2) / m  # ω₀² = (4π × 10¹⁴ × e²) / m
w02 = np.sqrt(w0)                     # ω₀ = √(ω₀²)

# Set modulation strength
delta = 0  # Modulation strength, Δ (set to 0 for no modulation)

# Define wave number
k = 1  # Wave number (assumed constant)

# Generate wave vector values (kx) from 0.01 to 2π
kx = np.linspace(0.01, 2 * np.pi)  # Avoid starting at 0 to prevent division by zero

# Define angular frequencies (ωt) for different phases
omegat = 0               # ωt = 0
omegat1 = np.pi / 2      # ωt = π/2
omegat2 = (3 * np.pi) / 2 # ωt = 3π/2

# Calculate the electron velocity for different phases
ve = w02 * delta * np.sin(kx) * np.sin(omegat) / k    # Velocity for ωt = 0
ve1 = w02 * delta * np.sin(kx) * np.sin(omegat1) / k  # Velocity for ωt = π/2
ve2 = w02 * delta * np.sin(kx) * np.sin(omegat2) / k  # Velocity for ωt = 3π/2

# Plot the velocity profiles with different colors for each phase
plt.plot(kx, ve, 'k', label=r"$\omega t=0$")            # Black curve for ωt = 0
plt.plot(kx, ve1, 'b', label=r"$\omega t=\pi/2$")       # Blue curve for ωt = π/2
plt.plot(kx, ve2, 'r', label=r"$\omega t=3\pi/2$")      # Red curve for ωt = 3π/2

# Add a legend to label the curves
plt.legend(loc='best')  # Automatically choose the best location for the legend

# Label the axes
plt.xlabel('kx', fontsize=16)        # Label for the x-axis
plt.ylabel('Velocity', fontsize=16)  # Label for the y-axis

# Customize the appearance of tick marks
plt.tick_params(direction='in')      # Make tick marks point inward
plt.xticks(size=16)                  # Set font size for x-axis ticks
plt.yticks(size=16)                  # Set font size for y-axis ticks

# Add a title to the plot indicating Δ = 0 (no modulation)
plt.title('Electron Velocity Profile ($\Delta$=0)', fontsize=16)

# Save the plot as a high-resolution PNG file
plt.savefig('velocity0.00.png', dpi=600)  # Save the plot with 600 DPI resolution

# Optionally display the plot (useful for interactive environments)
plt.show()


# In[ ]:




