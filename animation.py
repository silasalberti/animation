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

frames = {
	'glide_in': (1, 2),
	'glide_in_2': (2, 2.8),
	'end': (15,20)
}

TIME_UNIT = 100

def frame(identifier):
	def interpolation(i):
		if i > frames[identifier][1]*TIME_UNIT:
			return 1
		elif i < frames[identifier][0]*TIME_UNIT:
			return 0
		else:
			return (i/TIME_UNIT - frames[identifier][0])/(frames[identifier][1] - frames[identifier][0])
	return interpolation

# Animation Setup
objects = []

def init():
	# Rectangles
	for i in range(4):
		objects.append(patches.Rectangle((0.025 + i*0.25, 1.0), 0.2, 0.2))
	# Arrows
	for i in range(3):
		objects.append(patches.Arrow(0.225 + 0.25*i, 1.025, 0.05, 0, width=0.05, color='black'))
		objects[4+i].set_alpha(0)
	# Queue-Rectangle
	objects.append(patches.Rectangle((0.2, 1.0), 0.6, 0.15, color='green'))
	# Head/Tail-Arrows
	objects.append(patches.FancyArrowPatch((0.2, 1.025), (-0.2, 0.2), connectionstyle="arc3,rad=.5", color='red'))

	for obj in objects:
		ax.add_patch(obj)
	return objects

def animate(i):
	# Rectangles
	objects[0].set_y(1.0 - 0.8*frame('glide_in')(i))
	objects[1].set_y(1.0 - 0.8*frame('glide_in')(i))
	objects[2].set_y(1.0 - 0.8*frame('glide_in')(i))
	objects[3].set_y(1.0 - 0.8*frame('glide_in')(i))
	# Arrows
	ax.patches.remove(objects[4])
	objects[4] = patches.Arrow(0.225, 1.025 - 0.8*frame('glide_in')(i), 0.05, 0, width=0.05, color='black')
	ax.add_patch(objects[4])
	ax.patches.remove(objects[5])
	objects[5] = patches.Arrow(0.225+0.25, 1.025 - 0.8*frame('glide_in')(i), 0.05, 0, width=0.05, color='black')
	ax.add_patch(objects[5])
	ax.patches.remove(objects[6])
	objects[6] = patches.Arrow(0.225+0.5, 1.025 - 0.8*frame('glide_in')(i),0.05, 0, width=0.05, color='black')
	ax.add_patch(objects[6])
	# Queue-Rectangle
	objects[7].set_y(1.0 - 0.4*frame('glide_in_2')(i))
	# Head/Tail-Arrows
	ax.patches.remove(objects[8])
	objects[8] = patches.FancyArrowPatch((0.2, 1.025 - 0.4*frame('glide_in_2')(i)), (-0.05, 0.2), connectionstyle="arc3,rad=.5", color='red')
	ax.add_patch(objects[8])

	return objects

anim = animation.FuncAnimation(fig, animate, init_func=init, interval=1, blit=True)

plt.show()
