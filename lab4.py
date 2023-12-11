from skimage import io, filters, measure
from skimage.color import rgb2gray
from skimage.feature import canny
from skimage.transform import probabilistic_hough_line
import matplotlib.pyplot as plt

# Завантаження зображення
image = io.imread('image_cars.png')
# Перетворення зображення у відтінки сірого
gray_image = rgb2gray(image)

# Використання фільтру Canny для виявлення країв
edges = canny(gray_image, sigma=3)

# Виявлення ліній на зображенні за допомогою алгоритму Хафа
lines = probabilistic_hough_line(edges, threshold=10, line_length=5, line_gap=3)

# Створення фігуру для відображення результатів
fig, ax = plt.subplots(figsize=(10, 5))

# Показати оригінальне зображення
ax.imshow(image, cmap=plt.cm.gray)

# Показати виявлені лінії
for line in lines:
    p0, p1 = line
    ax.plot((p0[0], p1[0]), (p0[1], p1[1]), 'b')

# Відключити вісі
ax.set_axis_off()
plt.tight_layout()
# Показати результат
plt.show()
