import numpy as np

# Вершини піраміди з трикутною основою
vertices = np.array([[0, 0, 0], [1, 0, 0], [0.5, np.sqrt(3)/2, 0], [0.5, np.sqrt(3)/6, np.sqrt(6)/3]])

# Кут нахилу площини зображення (в радіанах)
theta = np.radians(45)

# Матриця проекції
M = np.array([
    [1/np.sqrt(2), -1/np.sqrt(2), 0, 0],
    [1/np.sqrt(2), 1/np.sqrt(2), 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

# Додамо стовпець з одиницями до матриці вершин
vertices_homogeneous = np.column_stack((vertices, np.ones(vertices.shape[0])))

# Виконання проекції
projected_vertices = np.dot(vertices_homogeneous, M.T)

# Відобразимо координати після проекції
print("Projected Vertices:")
print(projected_vertices)
