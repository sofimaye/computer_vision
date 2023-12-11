"""виявлення країв об'єктів"""
import cv2

# Завантаження зображення
image = cv2.imread("image_cars.png")

# Конвертація в RGB та інші попередні обробки
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_eq_channels = image_rgb.copy()

for channel in range(image_eq_channels.shape[2]):
    image_eq_channels[:, :, channel] = cv2.equalizeHist(image_eq_channels[:, :, channel])

image_gray = cv2.cvtColor(image_eq_channels, cv2.COLOR_RGB2GRAY)
image_eq_global = cv2.equalizeHist(image_gray)
image_blur = cv2.GaussianBlur(image_eq_global, (5, 5), 0)

# Виявлення країв та знаходження контурів
edges = cv2.Canny(image_blur, 50, 150)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Фільтрація та відображення контурів на оригінальному зображенні
for cnt in contours:
    area = cv2.contourArea(cnt)
    if 50 < area < 150:
        x, y, w, h = cv2.boundingRect(cnt)
        aspect_ratio = w / float(h)
        if 0.5 < aspect_ratio < 3:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Відображення лише кінцевого зображення з виділеними автомобілями
cv2.imshow("Detected Cars", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
