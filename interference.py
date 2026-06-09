import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

wavelength = 500e-9 
d = 0.5e-3
theta = np.linspace(-0.01, 0.01, 2000)

def intensity(theta, wavelength, d):
    return np.cos((np.pi * d * np.sin(theta)) / wavelength) ** 2

I = intensity(theta, wavelength, d)

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

[line] = ax.plot(theta, I)
ax.set_title("Double Slit Interference Pattern")
ax.set_xlabel("Angle (rad)")
ax.set_ylabel("Intensity")
ax.grid(True)

ax_wavelength = plt.axes([0.2, 0.1, 0.65, 0.03])
ax_slit = plt.axes([0.2, 0.05, 0.65, 0.03])

slider_wavelength = Slider(
    ax_wavelength,
    "Wavelength (nm)",
    400,
    700,
    valinit=wavelength * 1e9
)

slider_slit = Slider(
    ax_slit,
    "Slit Separation (mm)",
    0.1,
    1.0,
    valinit=d * 1e3
)

def update(val):
    wavelength = slider_wavelength.val * 1e-9
    d = slider_slit.val * 1e-3

    I = intensity(theta, wavelength, d)
    line.set_ydata(I)
    fig.canvas.draw_idle()

slider_wavelength.on_changed(update)
slider_slit.on_changed(update)

plt.show()