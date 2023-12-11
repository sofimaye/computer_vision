import matplotlib.pyplot as plt
import numpy as np
import itertools

def axonometric_projection(x, y, z):
    return x + 0.5 * z, y + 0.5 * z

def draw_line(ax, x0, y0, x1, y1, color='black'):
    ax.plot([x0, x1], [y0, y1], color=color)

def draw_pyramid(ax, vertices, colors):
    for (i, j), color in zip(itertools.combinations(range(len(vertices)), 2), colors):
        draw_line(ax, *vertices[i], *vertices[j], color=color)

def move_pyramid(vertices, dx, dy, dz):
    return [[x + dx, y + dy, z + dz] for x, y, z in vertices]

# Визначення вершин піраміди
original_vertices_3d = np.array([[0, 0, 0], [1, 0, 0], [0.5, np.sqrt(3)/2, 0], [0.5, np.sqrt(3)/6, np.sqrt(6)/3]])

# Кольори для кожного растра
colors_cycle = itertools.cycle(['red', 'green', 'blue', 'cyan', 'magenta', 'yellow'])

# Параметри руху
dx, dy, dz = 0.1, 0.1, 0.1  # Зміщення піраміди

# Створення графічного вікна
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-1, 2)
ax.set_ylim(-1, 2)

# Динамічне переміщення піраміди
for _ in range(10):  # 10 кроків руху
    colors = [next(colors_cycle) for _ in range(6)]
    moved_vertices_3d = move_pyramid(original_vertices_3d, dx, dy, dz)
    draw_pyramid(ax, [axonometric_projection(*vertex) for vertex in moved_vertices_3d], colors)
    original_vertices_3d = moved_vertices_3d  # Оновлення вершин для наступного кроку

plt.show()
