import cv2
import numpy as np
import math

size = 400
img = np.zeros((size, size), dtype=np.uint8)
img[::20, :] = 255
img[:, ::20] = 255
cv2.putText(img, "CEVI LAB", (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 1.5, 255, 3)

out_forward = np.zeros((size, size), dtype=np.uint8)
angle = math.radians(45)
cos_a, sin_a = math.cos(angle), math.sin(angle)
cx, cy = size // 2, size // 2

for y in range(size):
    for x in range(size):
        x_c, y_c = x - cx, y - cy
        x_new = int(x_c * cos_a - y_c * sin_a) + cx
        y_new = int(x_c * sin_a + y_c * cos_a) + cy
        if 0 <= x_new < size and 0 <= y_new < size:
            out_forward[y_new, x_new] = img[y, x]

cv2.imwrite('image_A_forward.png', out_forward)

M = cv2.getRotationMatrix2D((cx, cy), 45, 1.0)
out_backward = cv2.warpAffine(img, M, (size, size), flags=cv2.INTER_NEAREST)
cv2.imwrite('image_B_backward.png', out_backward)
print("Images generated successfully!")
