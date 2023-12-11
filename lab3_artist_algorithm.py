# Налаштуємо кольори та прозорість для кращої візуалізації граней
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


"""Використання алгоритму художника"""
def calculate_distance(face, view_point=[0, 0, 0]):
    # Розрахунок центру поверхні
    face_center = np.mean(face, axis=0)
    # Відстань від центру до точки огляду
    return np.linalg.norm(face_center - np.array(view_point))


def sort_faces_by_distance(faces, view_point=[0, 0, 0]):
    # Сортування поверхонь по відстані
    return sorted(faces, key=lambda face: calculate_distance(face, view_point), reverse=True)

def plot_pyramid_enhanced():
    # Вершини піраміди з трикутною основою
    vertices = np.array([[0, 0, 0], [1, 0, 0], [0.5, np.sqrt(3) / 2, 0], [0.5, np.sqrt(3) / 6, np.sqrt(6) / 3]])

    # Визначення граней піраміди
    faces = [[vertices[i] for i in [0, 1, 3]],
             [vertices[i] for i in [1, 2, 3]],
             [vertices[i] for i in [2, 0, 3]],
             [vertices[i] for i in [0, 1, 2]]]

    # Сортування граней
    sorted_faces = sort_faces_by_distance(faces)

    # Створення графічного вікна
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Кольори для кожної грані
    face_colors = ['skyblue', 'green', 'blue', 'yellow']

    # Додавання граней піраміди з кольорами і прозорістю
    for i, face in enumerate(sorted_faces):
        poly = Poly3DCollection([face], color=face_colors[i], alpha=0.5, edgecolors='black')
        ax.add_collection3d(poly)

    # Налаштування меж графіку
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_zlim([0, 1])

    # Назви осей
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

    # Налаштування кута огляду для кращого перегляду
    ax.view_init(elev=30, azim=30)

    # Показати графік
    plt.show()


plot_pyramid_enhanced()
