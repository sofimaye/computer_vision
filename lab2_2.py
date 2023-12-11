import matplotlib
matplotlib.use('TkAgg')  # Using a backend that supports interactivity
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import numpy as np
import itertools

# Setting up a cycle iterator for colors
colors_cycle = itertools.cycle(['red', 'green', 'blue', 'cyan', 'magenta', 'yellow'])

# Defining functions for 3D pyramid operations
def axonometric_projection(x, y, z):
    return x + 0.5 * z, y + 0.5 * z

def draw_line(ax, x0, y0, x1, y1, color='black'):
    ax.plot([x0, x1], [y0, y1], color=color)

def draw_pyramid(ax, vertices, colors):
    for (i, j), color in zip(itertools.combinations(range(len(vertices)), 2), colors):
        draw_line(ax, *vertices[i], *vertices[j], color=color)

def move_pyramid(vertices, dx, dy, dz):
    return [[x + dx, y + dy, z + dz] for x, y, z in vertices]

# Initial 3D pyramid vertices
original_vertices_3d = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [0.5, np.sqrt(3)/2, 0],
    [0.5, np.sqrt(3)/6, np.sqrt(6)/3]
])

# Initial line colors for the pyramid
colors = ['blue'] * 6

# Creating a figure and axis for drawing the pyramid
fig, ax_pyramid = plt.subplots()
ax_pyramid.set_aspect('equal')
ax_pyramid.set_xlim(-2, 3)
ax_pyramid.set_ylim(-2, 3)

# Drawing the pyramid
draw_pyramid(ax_pyramid, [axonometric_projection(*vertex) for vertex in original_vertices_3d], colors)

# Adding sliders for moving the pyramid
axcolor = 'lightgoldenrodyellow'
ax_slider_mvx = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
ax_slider_mvy = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
slider_mvx = Slider(ax_slider_mvx, 'Move X', -2.0, 2.0, valinit=0)
slider_mvy = Slider(ax_slider_mvy, 'Move Y', -2.0, 2.0, valinit=0)

# Adding a button for changing the line colors of the pyramid
ax_btn = plt.axes([0.8, 0.025, 0.1, 0.04])
btn_change_color = Button(ax_btn, 'Change Color', color=axcolor, hovercolor='0.975')

# Updating function for the sliders
def update(val):
    ax_pyramid.clear()
    ax_pyramid.set_aspect('equal')
    ax_pyramid.set_xlim(-2, 3)
    ax_pyramid.set_ylim(-2, 3)
    dx = slider_mvx.val
    dy = slider_mvy.val
    moved_vertices_3d = move_pyramid(original_vertices_3d, dx, dy, 0)
    draw_pyramid(ax_pyramid, [axonometric_projection(*vertex) for vertex in moved_vertices_3d], colors)
    fig.canvas.draw_idle()

slider_mvx.on_changed(update)
slider_mvy.on_changed(update)

# Changing color function for the button
def change_color(event):
    global colors
    colors = [next(colors_cycle) for _ in range(6)]
    update(None)

btn_change_color.on_clicked(change_color)

plt.show()

