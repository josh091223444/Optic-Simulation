import numpy as np
import matplotlib.pyplot as plt

wavelength = 500e-9 
a = 0.2e-3

theta = np.linspace(-0.01, 0.01, 2000)

def intensity(theta, wavelength, a):
     beta =(np.pi * a * np.sin(theta)) / wavelength
     return (np.sinc(beta / np.pi)) ** 2

I = intensity(theta, wavelength, a)

plt.figure()
plt.plot(theta, I)
plt.title("Single Slit Diffraction Pattern")
plt.xlabel("Angle (rad)")
plt.ylabel("Intensity")
plt.grid(True)
plt.show()