import numpy as np
import cv2
from matplotlib import pyplot as plt

# Завантаження зображення з файлу
clustered = cv2.imread('processed_image.png')
if clustered is None:
    raise ValueError("The image cannot be loaded. Please check the file path.")

# Перетворення в зображення в відтінки сірого
gray_image = cv2.cvtColor(clustered, cv2.COLOR_BGR2GRAY)
print("Grayscale conversion completed.")

# Порогова обробка
block_size = 15
offset = 5
_, binary_adaptive = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print("Adaptive thresholding completed.")

# Визначення відстані
distance = cv2.distanceTransform(binary_adaptive, cv2.DIST_L2, 3)
print("Distance transform completed.")

# Знаходження локальних максимумів
local_maxi_plot = np.zeros_like(distance, dtype=bool)
local_maxi_plot[np.unravel_index(distance.argmax(), distance.shape)] = True
print("Peak detection completed.")

# Створення маркерів для водоспадної сегментації
_, markers = cv2.connectedComponents(local_maxi_plot.astype(np.uint8))
print("Markers creation completed.")

# Водоспадна сегментація
labels_ws = cv2.watershed(cv2.cvtColor(clustered, cv2.COLOR_BGR2RGB), markers)
print("Watershed segmentation completed.")

# Відображення результату сегментації
plt.imshow(labels_ws, cmap='nipy_spectral')
plt.axis('off')
plt.show()

# Відображення маски порогової обробки
plt.imshow(binary_adaptive, cmap='gray')
plt.title('Binary Adaptive')
plt.axis('off')
plt.show()

# Відображення трансформованої відстані
plt.imshow(distance, cmap='gray')
plt.title('Distance Transform')
plt.axis('off')
plt.show()

# Відображення локальних максимумів
plt.imshow(local_maxi_plot, cmap='gray')
plt.title('Local Maxima')
plt.axis('off')
plt.show()

# Відображення маркерів
plt.imshow(markers, cmap='nipy_spectral')
plt.title('Markers')
plt.axis('off')
plt.show()

