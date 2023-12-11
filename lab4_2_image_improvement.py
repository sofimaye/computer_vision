import cv2
"""images improvement for OpenCV"""

# Loading the image
image = cv2.imread("image_cars.png")

# Converting image to RGB (OpenCV loads images in BGR)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Applying Histogram Equalization to each color channel
image_eq_channels = image_rgb.copy()
for channel in range(image_eq_channels.shape[2]):
    image_eq_channels[:, :, channel] = cv2.equalizeHist(image_eq_channels[:, :, channel])

# Converting to grayscale for further processing like histogram equalization on brightness and filtering
image_gray = cv2.cvtColor(image_eq_channels, cv2.COLOR_RGB2GRAY)

# Global Histogram Equalization on the grayscale image
image_eq_global = cv2.equalizeHist(image_gray)

# Applying Gaussian Blur to reduce noise and improve edge detection
image_blur = cv2.GaussianBlur(image_eq_global, (5, 5), 0)

# Displaying the images after each step using OpenCV's imshow function
cv2.imshow('Original Image in RGB', image_rgb)
cv2.imshow('Color Equalized Image', image_eq_channels)
cv2.imshow('Global Histogram Equalized Image', image_eq_global)
cv2.imshow('Blurred Image for Noise Reduction', image_blur)

# Waiting for a key press and then destroy all image windows
cv2.waitKey(0)
cv2.destroyAllWindows()
