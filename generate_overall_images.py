import cv2
import numpy as np
import matplotlib.pyplot as plt

print("Generating Overall Assessment Images...")

# ==========================================
# Q9: Histogram Recognition Image
# ==========================================
# Generate three distinct lighting images and their histograms
np.random.seed(42)
dark_img = np.random.normal(50, 15, (200, 200)).clip(0, 255).astype(np.uint8)
bright_img = np.random.normal(200, 15, (200, 200)).clip(0, 255).astype(np.uint8)
contrast_img = np.random.uniform(20, 230, (200, 200)).astype(np.uint8)

fig, axs = plt.subplots(2, 3, figsize=(12, 7))

# Dark Image
axs[0, 0].imshow(dark_img, cmap='gray', vmin=0, vmax=255)
axs[0, 0].set_title("Image A")
axs[0, 0].axis('off')
axs[1, 0].hist(dark_img.ravel(), bins=50, range=(0, 256), color='blue', alpha=0.7)
axs[1, 0].set_title("Histogram 1")
axs[1, 0].set_xlim(0, 255)

# Bright Image
axs[0, 1].imshow(bright_img, cmap='gray', vmin=0, vmax=255)
axs[0, 1].set_title("Image B")
axs[0, 1].axis('off')
axs[1, 1].hist(bright_img.ravel(), bins=50, range=(0, 256), color='orange', alpha=0.7)
axs[1, 1].set_title("Histogram 2")
axs[1, 1].set_xlim(0, 255)

# Balanced Contrast Image
axs[0, 2].imshow(contrast_img, cmap='gray', vmin=0, vmax=255)
axs[0, 2].set_title("Image C")
axs[0, 2].axis('off')
axs[1, 2].hist(contrast_img.ravel(), bins=50, range=(0, 256), color='green', alpha=0.7)
axs[1, 2].set_title("Histogram 3")
axs[1, 2].set_xlim(0, 255)

plt.tight_layout()
plt.savefig("overall_q9_histograms.png", dpi=150)
plt.close()
print("Saved: overall_q9_histograms.png")

# ==========================================
# Q19: Frequency Domain Filtering
# ==========================================
# Create Low Pass Mask and High Pass Mask
mask_size = 200
center = mask_size // 2
radius = 35

# Low pass mask (White circle on black background)
lpf = np.zeros((mask_size, mask_size), dtype=np.uint8)
cv2.circle(lpf, (center, center), radius, 255, -1)

# High pass mask (Black circle on white background)
hpf = np.ones((mask_size, mask_size), dtype=np.uint8) * 255
cv2.circle(hpf, (center, center), radius, 0, -1)

fig, axs = plt.subplots(1, 2, figsize=(8, 4))

axs[0].imshow(lpf, cmap='gray')
axs[0].set_title("Filter Mask 1 (Low-Pass)")
axs[0].axis('off')

axs[1].imshow(hpf, cmap='gray')
axs[1].set_title("Filter Mask 2 (High-Pass)")
axs[1].axis('off')

plt.tight_layout()
plt.savefig("overall_q19_frequency.png", dpi=150)
plt.close()
print("Saved: overall_q19_frequency.png")

# ==========================================
# Q29: Epipolar Geometry Diagram
# ==========================================
# Generate a schematic diagram using matplotlib
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 8)
ax.axis('off')

# Camera centers
ax.plot(1, 1, 'o', color='blue', markersize=10)
ax.text(0.6, 0.6, "C_L (Left Center)", fontsize=10, fontweight='bold', color='blue')

ax.plot(9, 1, 'o', color='red', markersize=10)
ax.text(8.4, 0.6, "C_R (Right Center)", fontsize=10, fontweight='bold', color='red')

# 3D point X
ax.plot(5, 7, 'o', color='green', markersize=10)
ax.text(5.2, 7.1, "X (3D Point)", fontsize=12, fontweight='bold', color='green')

# Draw baseline connecting camera centers
ax.plot([1, 9], [1, 1], '--', color='gray')
ax.text(5, 0.5, "Baseline", fontsize=10, color='gray')

# Draw left/right image planes as rectangles
# Left plane: x from 2 to 3.5, y from 2 to 4
ax.plot([2, 3.5, 3.5, 2, 2], [2, 2.5, 4.5, 4, 2], color='black', linewidth=2)
ax.text(1.7, 4.3, "Left Image Plane", fontsize=9)

# Right plane: x from 7.5 to 9, y from 2 to 4
ax.plot([6.5, 8, 8, 6.5, 6.5], [2.5, 2, 4, 4.5, 2.5], color='black', linewidth=2)
ax.text(7.6, 4.3, "Right Image Plane", fontsize=9)

# Draw rays from CL/CR to X
ax.plot([1, 5], [1, 7], color='blue', alpha=0.7)
ax.plot([9, 5], [1, 7], color='red', alpha=0.7)

# Intersection points (left and right image projections)
ax.plot([2.5], [3.25], 'o', color='blue', markersize=6)
ax.text(2.6, 3.1, "x_L", fontsize=10, fontweight='bold')

ax.plot([7.5], [3.25], 'o', color='red', markersize=6)
ax.text(7.1, 3.1, "x_R", fontsize=10, fontweight='bold')

# Epipoles (Intersection of baseline with image planes)
ax.plot([2.2], [1.3], 'o', color='purple', markersize=8)
ax.text(2.3, 1.4, "Label A", fontsize=10, fontweight='bold', color='purple')

ax.plot([7.8], [1.3], 'o', color='purple', markersize=8)
ax.text(7.1, 1.4, "Label B", fontsize=10, fontweight='bold', color='purple')

# Draw epipolar plane triangle (C_L - X - C_R)
ax.fill([1, 5, 9], [1, 7, 1], facecolor='yellow', alpha=0.1)
ax.text(4.5, 3.5, "Epipolar Plane", fontsize=10, color='purple', alpha=0.7)

# Draw epipolar lines on image planes
ax.plot([2.2, 2.5], [1.3, 3.25], color='purple', linewidth=1.5)
ax.plot([7.8, 7.5], [1.3, 3.25], color='purple', linewidth=1.5)

plt.tight_layout()
plt.savefig("overall_q29_epipolar.png", dpi=150)
plt.close()
print("Saved: overall_q29_epipolar.png")

print("All overall assessment images complete!")
