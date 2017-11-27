import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import animation
import math

# First set up the figure and the axis
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])

rectangles = [None, None, None, None]
for i in range(4):
	rectangles[i] = patches.Rectangle((0.025 + i*0.25, 0.0), 0.2, 0.2)

for rect in rectangles:
	print(rect.get_x())

def init():
	for rect in rectangles:
		ax.add_patch(rect)
	return rectangles

def animate(i):
	for rect in rectangles:
		rect.set_y(0.5 + 0.5*math.sin(i*0.1))
	return rectangles

anim = animation.FuncAnimation(fig, animate, init_func=init, interval=10, blit=True)


plt.show()
