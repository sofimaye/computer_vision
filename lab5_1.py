import cv2

def process_image(img):
    image = cv2.imread(img)
    if image is None:
        return "The image cannot be loaded. Please check the file path."

    # Корекція кольорів
    # Перетворення в RGB, якщо зображення у форматі BGR.
    corrected_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Вирівнювання гістограми для кожного каналу кольору
    for channel in range(corrected_image.shape[2]):
        corrected_image[:, :, channel] = cv2.equalizeHist(corrected_image[:, :, channel])

    # Фільтрація (видалення шуму)
    # Використання більшого розміру ядра для гауссового розмиття для більш сильного ефекту
    filtered_image = cv2.GaussianBlur(corrected_image, (9, 9), 0)

    # Додаткова опція: можливість застосування фільтра медіанного розмиття для видалення "соль-перець" шуму
    median_blurred = cv2.medianBlur(corrected_image, 5)

    # Збереження обробленого зображення можна також зберегти median_blurred
    processed_image_path = 'processed_image.png'
    cv2.imwrite(processed_image_path, filtered_image)

    return processed_image_path

# Для запуску функції, потрібно буде передати шлях до  зображення:
processed_image = process_image('dzz.webp')
