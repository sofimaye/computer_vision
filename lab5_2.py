
#кластеризація
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import cv2
import numpy as np

# Load the image from the file
image = cv2.imread('processed_image.png')
if image is None:
    raise ValueError("The image cannot be loaded. Please check the file path.")

# Convert to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Reshape the image data into a 2D array of pixels
pixels = image_rgb.reshape((-1, 3))

# Normalize the pixel values
scaler = StandardScaler()
pixels_scaled = scaler.fit_transform(pixels)

# Set a fixed number of clusters for simplicity
n_clusters = 5
kmeans = KMeans(n_clusters=n_clusters, n_init=10, random_state=0).fit(pixels_scaled)

# Restore the original scale of cluster centers
cluster_centers_original_scale = scaler.inverse_transform(kmeans.cluster_centers_)

# Create an image with the clustered data
clustered = cluster_centers_original_scale[kmeans.labels_].reshape(image_rgb.shape).astype(np.uint8)
np.save('clustered_image.npy', clustered)
# Display the clustered image
plt.imshow(clustered)
plt.axis('off')
plt.show()
