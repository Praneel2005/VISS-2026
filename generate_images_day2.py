import cv2
import numpy as np

print("Generating Day 2 Challenge Images...")

# ==========================================
# Q1: The "Smudge vs. Erase" Dilemma (Noise)
# ==========================================
# Create a base image with heavy salt-and-pepper noise
img1 = np.ones((300, 400), dtype=np.uint8) * 200
cv2.putText(img1, "CEVI LAB", (50, 160), cv2.FONT_HERSHEY_SIMPLEX, 2, 0, 5)

# Apply Salt and Pepper noise
noise = np.random.rand(*img1.shape)
img1[noise < 0.05] = 0    # Pepper (Black)
img1[noise > 0.95] = 255  # Salt (White)

cv2.imwrite("q1_noise.png", img1)
print("Saved: q1_noise.png")

# ==========================================
# Q2: The "Moving Bus" Sabotage (Matches)
# ==========================================
# Create a graphic showing two images with feature matching lines
img2 = np.zeros((300, 600, 3), dtype=np.uint8)
# Draw Image 1 and Image 2 boundaries
cv2.rectangle(img2, (10, 10), (290, 290), (200, 200, 200), 2)
cv2.rectangle(img2, (310, 10), (590, 290), (200, 200, 200), 2)

# Draw valid background inliers (Green, parallel-ish)
for _ in range(25):
    y = np.random.randint(50, 250)
    x1 = np.random.randint(50, 250)
    x2 = x1 + 300
    cv2.line(img2, (x1, y), (x2, y + np.random.randint(-10, 10)), (0, 200, 0), 1)

# Draw invalid outliers / moving bus (Red, crossing/skewed)
for _ in range(6):
    y1 = np.random.randint(150, 200)
    x1 = np.random.randint(100, 150)
    y2 = np.random.randint(220, 270) # Bus moved down and right
    x2 = x1 + 380 
    cv2.line(img2, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.putText(img2, "Feature Matches (Green=Background, Red=Moving Bus)", (30, 280), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
cv2.imwrite("q2_matches.png", img2)
print("Saved: q2_matches.png")

# ==========================================
# Q3: The Crouch Test (Hallway Projection)
# ==========================================
# Create a side-by-side comparison of a hallway perspective
def draw_hallway(vp_y, title):
    img = np.zeros((300, 300, 3), dtype=np.uint8)
    vp = (150, vp_y)
    # Draw walls (Perspective lines)
    cv2.line(img, (0, 0), vp, (255, 255, 255), 2)
    cv2.line(img, (300, 0), vp, (255, 255, 255), 2)
    cv2.line(img, (0, 300), vp, (255, 255, 255), 2)
    cv2.line(img, (300, 300), vp, (255, 255, 255), 2)
    # Draw horizon and vanishing point
    cv2.line(img, (0, vp_y), (300, vp_y), (0, 0, 255), 1)
    cv2.circle(img, vp, 6, (0, 255, 0), -1)
    # Title
    cv2.putText(img, title, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    return img

img3_A = draw_hallway(150, "Photo 1: Standing")
img3_B = draw_hallway(240, "Photo 2: Crouching") # VP drops lower in the image
img3_combined = np.hstack((img3_A, img3_B))

cv2.imwrite("q3_hallway.png", img3_combined)
print("Saved: q3_hallway.png")

# ==========================================
# Q4: The Invisible Epipoles (Stereo Rig)
# ==========================================
# Create a perfectly rectified stereo rig visual
img4 = np.zeros((300, 600, 3), dtype=np.uint8)
cv2.rectangle(img4, (10, 10), (290, 290), (255,255,255), 2)
cv2.rectangle(img4, (310, 10), (590, 290), (255,255,255), 2)

cv2.putText(img4, "Left Camera Sensor", (50, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)
cv2.putText(img4, "Right Camera Sensor", (350, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)

# Draw perfectly horizontal epipolar lines
for y in range(80, 280, 30):
    cv2.line(img4, (15, y), (285, y), (0, 0, 255), 1)
    cv2.line(img4, (315, y), (585, y), (0, 0, 255), 1)

# Draw an object to show disparity
cv2.circle(img4, (150, 140), 20, (255, 0, 0), -1) # Object in left center
cv2.circle(img4, (410, 140), 20, (255, 0, 0), -1) # Object shifted left in right frame

cv2.imwrite("q4_stereo.png", img4)
print("Saved: q4_stereo.png")
print("All Day 2 generation complete!")
