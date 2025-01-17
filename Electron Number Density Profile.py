#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats  # Although imported, 'stats' is not used in this script
import seaborn as sns # Set the aesthetic style of seaborn plots
sns.set()


# # Electron Number Density Profile ($\Delta=0.60$)

# In[2]:


# Create a figure with a specified size
plt.figure(figsize=(12, 8))

# Define parameters
delta = 0.60  # Delta value
kx = np.linspace(0.1, 2 * np.pi)  # Array of kx values between 0.1 and 2π
omegat = np.pi      # ωt = π
omegata = np.pi / 2 # ωt = π/2
omegatb = 0         # ωt = 0

# Calculate the normalized electron number density for different ωt values
nbyno = (1 + delta * np.cos(kx)) / (1 + delta * np.cos(kx) * (1 - np.cos(omegat)))
nbynoa = (1 + delta * np.cos(kx)) / (1 + delta * np.cos(kx) * (1 - np.cos(omegata)))
nbynob = (1 + delta * np.cos(kx)) / (1 + delta * np.cos(kx) * (1 - np.cos(omegatb)))

# Plot the results with different colors for each curve
plt.plot(kx, nbyno, 'r', label=r"$\omega t=\pi$")
plt.plot(kx, nbynoa, 'b', label=r"$\omega t=\pi /2$")
plt.plot(kx, nbynob, 'k', label=r"$\omega t=0$")

# Add legend
plt.legend(loc='best')

# Label the axes
plt.xlabel("kx", fontsize=16)
plt.ylabel(r"$\frac{n_{e}}{n_{0}}$", fontsize=16)

# Customize tick parameters
plt.tick_params(direction='in')
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)

# Add a title
plt.title(r"Electron Number Density Profile ($\Delta=0.60$)", fontsize=16)

# Save the plot as a PNG file with high resolution
plt.savefig('density0.60.png', dpi=600)

# Show the plot
plt.show()


# # Electron Number Density Profile ($\Delta=0.45$)

# In[3]:


# Create a figure with specific dimensions
plt.figure(figsize=(12, 8))

# Set the parameter delta to 0.45 (strength of modulation)
delta = 0.45

# Generate an array of kx values ranging from 0.1 to 2π
kx = np.linspace(0.1, 2 * np.pi)

# Define the angular frequencies
omegat = np.pi      # ωt = π
omegata = np.pi / 2 # ωt = π/2
omegatb = 0         # ωt = 0

# Calculate the normalized electron number density for ωt = π
nbyno = (1 + delta * np.cos(kx)) / (1 + delta * np.cos(kx) * (1 - np.cos(omegat)))

# Calculate the normalized electron number density for ωt = π/2
nbynoa = (1 + delta * np.cos(kx)) / (1 + delta * np.cos(kx) * (1 - np.cos(omegata)))

# Calculate the normalized electron number density for ωt = 0
nbynob = (1 + delta * np.cos(kx)) / (1 + delta * np.cos(kx) * (1 - np.cos(omegatb)))

# Plot the electron number density for each angular frequency with different colors
plt.plot(kx, nbyno, 'r', label=r"$\omega t=\pi$")      # Red curve for ωt = π
plt.plot(kx, nbynoa, 'b', label=r"$\omega t=\pi /2$")  # Blue curve for ωt = π/2
plt.plot(kx, nbynob, 'k', label=r"$\omega t=0$")       # Black curve for ωt = 0

# Add a legend to label the curves
plt.legend(loc='best')

# Label the x-axis
plt.xlabel("kx", fontsize=16)

# Label the y-axis with a LaTeX-style formula
plt.ylabel(r"$\frac{n_{e}}{n_{0}}$", fontsize=16)

# Adjust the appearance of tick marks
plt.tick_params(direction='in')

# Customize the font size of the tick labels
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)

# Add a title to the plot with the specific value of Δ
plt.title(r"Electron Number Density Profile ($\Delta=0.45$)", fontsize=16)

# Save the plot as a high-resolution PNG file
plt.savefig('density0.45.png', dpi=600)

# Optionally, display the plot
plt.show()


# # Electron Number Density Profile ($\Delta=0$)

# In[4]:


# Create a figure with a specified size for better visualization
plt.figure(figsize=(12, 8))

# Set the modulation strength delta to 0 (no modulation)
delta = 0

# Generate an array of kx values from 0.01 to 2π (avoiding zero to prevent division issues)
kx = np.linspace(0.01, 2 * np.pi)

# Define the angular frequencies
omegat = np.pi      # ωt = π
omegata = np.pi / 2 # ωt = π/2
omegatb = 0         # ωt = 0

# Calculate the normalized electron number density for ωt = π
nbyno = (1 + delta * np.cos(kx)) / (1 + delta * np.cos(kx) * (1 - np.cos(omegat)))

# Calculate the normalized electron number density for ωt = π/2
nbynoa = (1 + delta * np.cos(kx)) / (1 + delta * np.cos(kx) * (1 - np.cos(omegata)))

# Calculate the normalized electron number density for ωt = 0
nbynob = (1 + delta * np.cos(kx)) / (1 + delta * np.cos(kx) * (1 - np.cos(omegatb)))

# Plot the electron number density profiles for different angular frequencies
plt.plot(kx, nbyno, 'r', label=r"$\omega t=\pi$")      # Red curve for ωt = π
plt.plot(kx, nbynoa, 'b', label=r"$\omega t=\pi /2$")  # Blue curve for ωt = π/2
plt.plot(kx, nbynob, 'k', label=r"$\omega t=0$")       # Black curve for ωt = 0

# Add a legend to label the different curves
plt.legend(loc='best')

# Label the x-axis
plt.xlabel("kx", fontsize=16)

# Label the y-axis with a LaTeX-style mathematical expression
plt.ylabel(r"$\frac{n_{e}}{n_{0}}$", fontsize=16)

# Adjust the appearance of tick marks to point inward
plt.tick_params(direction='in')

# Customize the font size of the tick labels for better readability
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)

# Add a title to the plot indicating Δ = 0 (no modulation)
plt.title(r"Electron Number Density Profile ($\Delta=0$)", fontsize=16)

# Save the plot as a high-resolution PNG file
plt.savefig('density0.00.png', dpi=600)

# Optionally, display the plot (useful for interactive environments)
plt.show()


# In[ ]:




