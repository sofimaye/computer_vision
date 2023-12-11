import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
def translate(vector, points):
    """
    Applying translation to a set of points.

    :param vector: Translation vector [dx, dy, dz].
    :param points: Array of points.
    :return: Translated points.
    """
    translation_matrix = np.array([[1, 0, 0, vector[0]],
                                   [0, 1, 0, vector[1]],
                                   [0, 0, 1, vector[2]],
                                   [0, 0, 0, 1]])
    translated_points = np.dot(points, translation_matrix)
    return translated_points


def scale(scaling_factors, points):
    """
    Applying scaling to a set of points.

    :param scaling_factors: Scaling factors [sx, sy, sz].
    :param points: Array of points.
    :return: Scaled points.
    """
    scaling_matrix = np.array([[scaling_factors[0], 0, 0, 0],
                               [0, scaling_factors[1], 0, 0],
                               [0, 0, scaling_factors[2], 0],
                               [0, 0, 0, 1]])
    scaled_points = np.dot(points, scaling_matrix)
    return scaled_points


def rotate(angle, axis, points):
    """
    Applying rotation to a set of points.

    :param angle: Rotation angle in degrees.
    :param axis: Axis of rotation ('x', 'y', or 'z').
    :param points: Array of points.
    :return: Rotated points.
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

    rotated_points = np.dot(points, rotation_matrix)
    return rotated_points


# Definining a cube with its vertices
cube_points = np.array([[0, 0, 0, 1],  # Point 1
                        [1, 0, 0, 1],  # Point 2
                        [1, 1, 0, 1],  # Point 3
                        [0, 1, 0, 1],  # Point 4
                        [0, 0, 1, 1],  # Point 5
                        [1, 0, 1, 1],  # Point 6
                        [1, 1, 1, 1],  # Point 7
                        [0, 1, 1, 1]])  # Point 8

# Example transformations
translated_cube = translate([2, 0, 0], cube_points)  # Translation cube by 2 units along the x-axis
scaled_cube = scale([2, 2, 2], cube_points)  # Scaling cube by a factor of 2
rotated_cube = rotate(45, 'z', cube_points)  # Rotating cube 45 degrees around the z-axis

print(translated_cube, scaled_cube, rotated_cube)

def plot_cube(points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Drawing the cube
    verts = [[points[0], points[1], points[2], points[3]],
             [points[4], points[5], points[6], points[7]],
             [points[0], points[1], points[5], points[4]],
             [points[2], points[3], points[7], points[6]],
             [points[1], points[2], points[6], points[5]],
             [points[4], points[7], points[3], points[0]]]

    ax.add_collection3d(Poly3DCollection(verts, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

    # Setting plot limits
    ax.set_xlim([0, 3])
    ax.set_ylim([0, 3])
    ax.set_zlim([0, 3])

    plt.show()

plot_cube(cube_points[:, :3])  # Original Cube
plot_cube(translated_cube[:, :3])  # Translated Cube
plot_cube(scaled_cube[:, :3])  # Scaled Cube
plot_cube(rotated_cube[:, :3])  # Rotated Cube


