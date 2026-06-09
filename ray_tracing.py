import numpy as np
import matplotlib.pyplot as plt


object_x = -10
object_height = 2

lens_x = 0
f = 5

rays_y = np.linspace(0, object_height, 5)


object_distance = abs(object_x - lens_x)

image_distance = 1 / (1/f - 1/object_distance)
image_x = lens_x + image_distance


magnification = -image_distance / object_distance
image_height = object_height * magnification


plt.figure()


for y0 in rays_y:

  
    x1 = np.linspace(object_x, lens_x, 100)
    y1 = np.linspace(y0, y0, 100)

    
    x2 = np.linspace(lens_x, image_x, 100)
    y2 = np.linspace(y0, image_height, 100)

    plt.plot(x1, y1, 'r')
    plt.plot(x2, y2, 'r')


plt.plot([object_x, object_x], [0, object_height], 'g', linewidth=3)


plt.axvline(lens_x, color='b', linestyle='--')


plt.axvline(image_x, color='purple', linestyle='--')

plt.title("Physically Correct Thin Lens Ray Tracing")
plt.xlabel("Distance")
plt.ylabel("Height")
plt.grid(True)

plt.show()