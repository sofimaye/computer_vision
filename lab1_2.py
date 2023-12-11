import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def translate(vector, point):
    """
    Applying translation to a single point.
    :param vector: Translation vector [dx, dy, dz].
    :param point: A single point.
    :return: Translated point.
    """
    translation_matrix = np.array([[1, 0, 0, vector[0]],
                                   [0, 1, 0, vector[1]],
                                   [0, 0, 1, vector[2]],
                                   [0, 0, 0, 1]])
    return np.dot(translation_matrix, point)

def scale(scaling_factors, point):
    """
    Applying scaling to a single point.

    :param scaling_factors: Scaling factors [sx, sy, sz].
    :param point: A single point.
    :return: Scaled point.
    """
    scaling_matrix = np.array([[scaling_factors[0], 0, 0, 0],
                               [0, scaling_factors[1], 0, 0],
                               [0, 0, scaling_factors[2], 0],
                               [0, 0, 0, 1]])
    return np.dot(scaling_matrix, point)

def rotate(angle, axis, point):
    """
    Applying rotation to a single point.

    :param angle: Rotation angle in degrees.
    :param axis: Axis of rotation ('x', 'y', or 'z').
    :param point: A single point.
    :return: Rotated point.
    """
    angle = np.radians(angle)
    if axis == 'x':
        rotation_matrix = np.array([[1, 0, 0, 0],
                                    [0, np.cos(angle), -np.sin(angle), 0],
                                    [0, np.sin(angle), np.cos(angle), 0],
                                    [0, 0, 0, 1]])
    elif axis == 'y':
        rotation_matrix = np.array([[np.cos(angle), 0, np.sin(angle), 0],
                                    [0, 1, 0, 0],
                                    [-np.sin(angle), 0, np.cos(angle), 0],
                                    [0, 0, 0, 1]])
    elif axis == 'z':
        rotation_matrix = np.array([[np.cos(angle), -np.sin(angle), 0, 0],
                                    [np.sin(angle), np.cos(angle), 0, 0],
                                    [0, 0, 1, 0],
                                    [0, 0, 0, 1]])
    else:
        raise ValueError("Invalid axis. Choose 'x', 'y', or 'z'.")

    return np.dot(rotation_matrix, point)

# Defining a cube with its vertices
cube_points = np.array([[0, 0, 0, 1],  # Point 1
                        [1, 0, 0, 1],  # Point 2
                        [1, 1, 0, 1],  # Point 3
                        [0, 1, 0, 1],  # Point 4
                        [0, 0, 1, 1],  # Point 5
                        [1, 0, 1, 1],  # Point 6
                        [1, 1, 1, 1],  # Point 7
                        [0, 1, 1, 1]]) # Point 8

# Applying transformations to each point of the cube separately
transformed_cube = []
for point in cube_points:
    point = translate([2, 0, 0], point)  # Translate
    point = scale([2, 2, 2], point)      # Scale
    point = rotate(45, 'z', point)       # Rotate
    transformed_cube.append(point)

transformed_cube = np.array(transformed_cube)

def plot_cube(points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Draw the cube
    verts = [[points[0, :3], points[1, :3], points[2, :3], points[3, :3]],
             [points[4, :3], points[5, :3], points[6, :3], points[7, :3]],
             [points[0, :3], points[1, :3], points[5, :3], points[4, :3]],
             [points[2, :3], points[3, :3], points[7, :3], points[6, :3]],
             [points[1, :3], points[2, :3], points[6, :3], points[5, :3]],
             [points[4, :3], points[7, :3], points[3, :3], points[0, :3]]]

    ax.add_collection3d(Poly3DCollection(verts, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

    # Setting plot limits
    ax.set_xlim([0, 4])
    ax.set_ylim([0, 4])
    ax.set_zlim([0, 4])

    plt.show()

# Plotting the original and transformed cubes
plot_cube(cube_points[:, :3])         # Original Cube
plot_cube(transformed_cube[:, :3])    # Transformed Cube
