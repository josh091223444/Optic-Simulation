import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

wavelength_init = 500e-9
d_init = 0.5e-3
a_init = 0.2e-3

theta = np.linspace(-0.01, 0.01, 2000)

def intensity(theta, wavelength, d, a):

    interference = np.cos((np.pi * d * np.sin(theta)) / wavelength) ** 2

    beta = (np.pi * a * np.sin(theta)) / wavelength
    diffraction = (np.sinc(beta / np.pi)) ** 2

    return interference * diffraction


I = intensity(theta, wavelength_init, d_init, a_init)

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

[line] = ax.plot(theta, I)

ax.set_title("Interference + Diffraction (Interactive)")
ax.set_xlabel("Angle (rad)")
ax.set_ylabel("Intensity")
ax.grid(True)

ax_wavelength = plt.axes([0.2, 0.15, 0.65, 0.03])
ax_slit_sep = plt.axes([0.2, 0.10, 0.65, 0.03])
ax_slit_width = plt.axes([0.2, 0.05, 0.65, 0.03])

slider_wavelength = Slider(
    ax_wavelength,
    "Wavelength (nm)",
    400,
    700,
    valinit=wavelength_init * 1e9
)

slider_d = Slider(
    ax_slit_sep,
    "Slit spacing (mm)",
    0.1,
    1.0,
    valinit=d_init * 1e3
)

slider_a = Slider(
    ax_slit_width,
    "Slit width (mm)",
    0.05,
    0.5,
    valinit=a_init * 1e3
)


def update(val):

    wavelength = slider_wavelength.val * 1e-9
    d = slider_d.val * 1e-3
    a = slider_a.val * 1e-3

    I = intensity(theta, wavelength, d, a)

    line.set_ydata(I)
    fig.canvas.draw_idle()

slider_wavelength.on_changed(update)
slider_d.on_changed(update)
slider_a.on_changed(update)

plt.show()