import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np


def plot_pyramid():
    # Вершини піраміди з трикутною основою
    vertices = np.array([[0, 0, 0], [1, 0, 0], [0.5, np.sqrt(3)/2, 0], [0.5, np.sqrt(3)/6, np.sqrt(6)/3]])

    # Визначення граней піраміди
    faces = [[vertices[i] for i in [0, 1, 3]],
             [vertices[i] for i in [1, 2, 3]],
             [vertices[i] for i in [2, 0, 3]],
             [vertices[i] for i in [0, 1, 2]]]

    # Створення графічного вікна
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Додавання граней піраміди
    poly3d = [Poly3DCollection(faces, color='skyblue', linewidths=1, edgecolors='r')]
    for poly in poly3d:
        ax.add_collection3d(poly)

    # Налаштування меж графіку
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_zlim([0, 1])

    # Назви осей
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

    # Показати графік
    plt.show()

# Виконання функції для відображення піраміди
plot_pyramid()
