import cv2
import matplotlib.pyplot as plt

# Завантаження зображення
image = cv2.imread('processed_image.png')  # Замініть 'your_image.jpg' на ім'я вашого зображення

# Перетворення зображення в відтінки сірого
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Бінаризація зображення (можна вибрати потрібний поріг)
_, binary = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

# Знаходження контурів
contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Створення копії зображення для виділення контурів на ньому
contour_image = image.copy()

# Виділення контурів на зображенні
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 3)

# Виведення зображення з контурами
plt.imshow(cv2.cvtColor(contour_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
