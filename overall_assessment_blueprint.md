# Computer Vision Summer School (VISS-2026)
## Overall Assessment Blueprint (30 Questions)

This document contains the framed questions, formats, and expected answers for the overall assessment covering all core computer vision topics taught in the course.

---

## 📸 Section A: Image Formation, Pinhole Camera Model & Image Transforms

### Question 1: Human Visual System (Fovea vs. Peripheral Sampling)
*   **Type:** Conceptual (True/False & Explanation)
*   **Heading:** `Question 1: Fovea vs. Peripheral Vision Sampling`
*   **Question Text:** "The human retina does not sample light uniformly. The fovea contains a dense packing of cone photoreceptors, while rod density peaks in the periphery. According to the Nyquist-Shannon sampling theorem, if a high-frequency spatial pattern (like a fine-striped shirt) is projected onto your peripheral retina, what optical phenomenon occurs, and why doesn't this happen when you look at it directly?"
*   **Expected Answer:** Aliasing (or spatial moiré patterns) occurs in peripheral vision because the peripheral rods are spaced too far apart (spatial sampling rate is below the Nyquist rate of the signal). Foveal vision has a much higher density of cones (higher sampling rate), satisfying the Nyquist theorem and resolving the fine details without aliasing.

### Question 2: Optimal Pinhole Diameter (Diffraction vs. Geometric Blur)
*   **Type:** Numerical Calculation
*   **Heading:** `Question 2: The Optimal Pinhole Trade-Off`
*   **Question Text:** "In a pinhole camera, if the pinhole is too large, the image is blurred by geometric projection. If the pinhole is too small, the image is blurred due to light wave diffraction. Rayleigh's criterion suggests the optimal pinhole diameter $d$ can be approximated by $d \approx 1.9 \sqrt{f \lambda}$, where $f$ is the distance to the sensor and $\lambda$ is the wavelength of light. Calculate the optimal pinhole diameter (in millimeters) for green light ($\lambda = 550 \text{ nm}$) when the camera sensor is placed exactly $10 \text{ cm}$ behind the pinhole. Show your calculations."
*   **Expected Answer:** 
    *   $f = 10 \text{ cm} = 0.1 \text{ m}$
    *   $\lambda = 550 \text{ nm} = 5.5 \times 10^{-7} \text{ m}$
    *   $d \approx 1.9 \sqrt{0.1 \times (5.5 \times 10^{-7})} = 1.9 \sqrt{5.5 \times 10^{-8}} = 1.9 \times (2.345 \times 10^{-4}) \approx 4.456 \times 10^{-4} \text{ m} \approx \mathbf{0.45 \text{ mm}}$ (or $\approx 0.446 \text{ mm}$).

### Question 3: Field of View (FOV) Scaling
*   **Type:** Mathematical / Conceptual
*   **Heading:** `Question 3: Field of View (FOV) Scaling`
*   **Question Text:** "You are shooting a scene. You decide to swap your camera sensor for one that is exactly twice as wide (doubling the sensor width $W$). To keep the composition unchanged, you simultaneously swap your lens for one with double the focal length (doubling $f$). Using the horizontal FOV formula $\text{FOV} = 2 \arctan\left(\frac{W}{2f}\right)$, state whether your Field of View increases, decreases, or stays exactly the same. Prove your answer mathematically."
*   **Expected Answer:** Stays exactly the same. 
    $\text{FOV}_{new} = 2 \arctan\left(\frac{2W}{2(2f)}\right) = 2 \arctan\left(\frac{2W}{4f}\right) = 2 \arctan\left(\frac{W}{2f}\right) = \text{FOV}_{old}$.

### Question 4: Spatial vs. Amplitude Resolution
*   **Type:** Conceptual (Multiple Choice & Explanation)
*   **Heading:** `Question 4: Spatial vs. Amplitude Resolution`
*   **Question Text:** "An image is degraded in two separate experiments: (A) It is downsampled by a factor of 8 without pre-filtering, and (B) It is re-quantized from 8-bit (256 levels) to 1-bit (2 levels). Identify which experiment produces 'false contouring' and which experiment produces 'spatial aliasing' (jagged edges). Explain the physical causes."
*   **Expected Answer:** Experiment A (downsampling) produces spatial aliasing (jagged edges) because high-frequency details are folded back into low frequencies due to undersampling. Experiment B (1-bit quantization) produces false contouring because the step size between quantization levels becomes large enough to create visible boundaries in smooth gradient areas.

### Question 5: Contrast Stretching Transformation
*   **Type:** Numerical Calculation
*   **Heading:** `Question 5: Linear Contrast Stretching`
*   **Question Text:** "You want to perform linear contrast stretching on a normalized gray-scale image. The active pixel intensities range from a minimum of $r_{min} = 0.2$ to a maximum of $r_{max} = 0.6$. The target output range is $s_{min} = 0$ to $s_{max} = 1.0$. Write the linear mapping formula $s = T(r)$ and calculate the exact output value $s$ for an input pixel intensity of $r = 0.3$."
*   **Expected Answer:** 
    *   Formula: $s = \frac{r - r_{min}}{r_{max} - r_{min}} \times (s_{max} - s_{min}) + s_{min} = \frac{r - 0.2}{0.6 - 0.2} = \frac{r - 0.2}{0.4} = 2.5(r - 0.2)$
    *   For $r = 0.3$: $s = 2.5(0.3 - 0.2) = 2.5(0.1) = \mathbf{0.25}$ (or $25\%$).

### Question 6: Discrete Histogram Equalization Limits
*   **Type:** Conceptual / Theoretical
*   **Heading:** `Question 6: Can Histogram Equalization Yield a Perfectly Flat Histogram?`
*   **Question Text:** "In continuous probability theory, applying the cumulative distribution function (CDF) transform maps any distribution to a perfectly uniform flat distribution. Why is it mathematically impossible to obtain a perfectly flat, uniform histogram when applying histogram equalization to a discrete, digital image? What happens to the gray levels?"
*   **Expected Answer:** Because a discrete image has a finite, fixed number of pixels and intensity levels. Histogram equalization can only map existing discrete bins to new levels; it cannot split pixels of the same initial intensity level into different bins. Consequently, the histogram bins are spread out but remain discrete, resulting in gaps rather than a flat continuous distribution.

### Question 7: Histogram Matching Mapping
*   **Type:** Conceptual (Mathematical Order)
*   **Heading:** `Question 7: Histogram Matching Core Steps`
*   **Question Text:** "In histogram matching (specification), we transform an input image $I_X$ so its histogram matches a target image $I_Y$. The mapping uses the intermediate mapping function $z = G^{-1}(S(r))$. Explain step-by-step what the variables $r$, $S(r)$, and $G(z)$ represent, and how the inverse function $G^{-1}$ completes the mapping."
*   **Expected Answer:** 
    1. $r$ represents the input intensity level.
    2. $S(r)$ is the CDF value of the input intensity level $r$ (equalizing the input).
    3. $G(z)$ is the CDF of the target histogram evaluated at output level $z$.
    4. $G^{-1}$ maps the equalized value $S(r)$ back to the target intensity scale by finding the target intensity level $z$ that satisfies $G(z) \approx S(r)$.

### Question 8: Geometric Transform Mapping Modes
*   **Type:** Matching Match-Up
*   **Heading:** `Question 8: Matching Transform Mapping & Interpolation`
*   **Question Text:** "Match the following image mapping concepts with their respective definitions:
    
    1. **Forward Mapping**  
    2. **Backward Mapping**  
    3. **Bilinear Interpolation**  
    4. **Nearest-Neighbor Interpolation**  

    **Definitions:**  
    A. Resolves destination pixel values by calculating a weighted average of the 4 closest source pixels.  
    B. Iterates through destination coordinates and applies the inverse transform to find corresponding source pixels, preventing holes.  
    C. Selects the single nearest pixel coordinate, causing jagged ('staircase') edges.  
    D. Iterates through source coordinates and projects them onto the destination grid, occasionally leaving 'holes' or unmapped pixels."
*   **Expected Answer:** 1-D, 2-B, 3-A, 4-C.

### Question 9: Histogram Recognition (Visual-Related)
*   **Type:** Visual Recognition (MCQ & Explanation)
*   **Heading:** `Question 9: Match the Histograms`
*   **Image:** `overall_q9_histograms.png`
*   **Question Text:** "Refer to the image above showing three input images (Image A, Image B, Image C) and three corresponding histograms (Histogram 1, Histogram 2, Histogram 3). Identify which histogram belongs to which image, and justify your choices based on their pixel distributions."
*   **Expected Answer:**
    *   Image A matches Histogram 1 (Low-contrast, dark image, with intensities clustered near 0).
    *   Image B matches Histogram 2 (High-contrast, bright image, with intensities clustered near 255).
    *   Image C matches Histogram 3 (Balanced, equalized/uniform contrast, with intensities spread evenly across the spectrum).

### Question 10: Aperture vs. Depth of Field (DoF)
*   **Type:** Conceptual (Optics)
*   **Heading:** `Question 10: Aperture and Depth of Field`
*   **Question Text:** "A photographer switches their camera aperture setting from $f/2.8$ to $f/16$ while adjusting exposure time to keep brightness constant. What happens to the Depth of Field (DoF) and the sharpness of background details? Explain the physical reason using the concept of 'circles of confusion'."
*   **Expected Answer:** The Depth of Field (DoF) increases, and the background details become sharper. This is because a smaller physical aperture (indicated by the larger f-number $f/16$) restricts the bundle of light rays entering the lens, resulting in narrower cones of light and smaller "circles of confusion" for out-of-focus background objects.

---

## 🧼 Section B: Image Filtering, Restoration & Registration

### Question 11: Linear Spatial Filters (Smoothing vs. Sharpening)
*   **Type:** Numerical Kernel Analysis
*   **Heading:** `Question 11: Linear Kernel Classification`
*   **Question Text:** "Consider the two spatial kernels:
    
    $$\text{Kernel 1} = \frac{1}{16}\begin{bmatrix} 1 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 1 \end{bmatrix}, \quad \text{Kernel 2} = \begin{bmatrix} 0 & -1 & 0 \\ -1 & 5 & -1 \\ 0 & -1 & 0 \end{bmatrix}$$
    
    Classify each kernel as a Low-pass filter (smoothing) or a High-pass filter (sharpening/edge enhancement). Justify your answer by calculating the sum of the coefficients and analyzing their center-to-edge weighting."
*   **Expected Answer:** 
    *   Kernel 1 is a **Low-pass filter** (smoothing). The coefficients sum to 1.0, and it is a Gaussian approximation where the center pixel is weighted highest, smoothing out high-frequency noise.
    *   Kernel 2 is a **High-pass filter** (sharpening/edge enhancement). The coefficients sum to 1.0, but the center has a large positive weight (+5) while neighboring pixels have negative weights (-1). This subtracts the average of the neighbors from the center, highlighting high-frequency transitions (edges).

### Question 12: Nonlinear Filtering (Outlier Median Logic)
*   **Type:** Conceptual Analysis
*   **Heading:** `Question 12: Why Median Filters Excel at Impulse Noise`
*   **Question Text:** "Explain why a non-linear $3 \times 3$ Median Filter is dramatically more effective at removing salt-and-pepper (impulse) noise than a linear $3 \times 3$ Box Filter, which instead smudges the noise. Answer using the mathematical properties of the mean vs. the median in the presence of extreme outliers."
*   **Expected Answer:** Salt-and-pepper noise produces extreme outlier values (0 or 255). A linear box filter averages all values in the neighborhood (mean), meaning an outlier will pull the average towards it, blurring and smudging the noise into adjacent pixels. A median filter sorts the intensities and selects the middle value; because impulse noise pixels are statistical outliers, they lie at the extremes of the sorted list and are completely discarded, restoring the clean background intensity.

### Question 13: Fourier Transform High/Low Frequencies
*   **Type:** Conceptual (Frequency Domain)
*   **Heading:** `Question 13: Edge Representations in the Fourier Spectrum`
*   **Question Text:** "You transform an image of a square room into the frequency domain using the Fast Fourier Transform (FFT). Where do the sharp boundaries of the walls show up in the Fourier magnitude spectrum: close to the center (origin) or far from the center? Explain what a Low-Pass Filter in the frequency domain physically does to these wall boundaries."
*   **Expected Answer:** The sharp boundaries of the walls correspond to rapid changes in intensity (high-frequency components) and show up far from the center (origin) in the Fourier spectrum. A frequency-domain Low-Pass Filter cuts off these high-frequency components far from the center, blurring and smoothing the sharp wall boundaries in the spatial domain.

### Question 14: Unsharp Masking Formulation
*   **Type:** Mathematical Formulation
*   **Heading:** `Question 14: Unsharp Masking Mechanics`
*   **Question Text:** "Unsharp masking is defined by the formula $g(x,y) = f(x,y) + k \cdot g_{mask}(x,y)$, where $f(x,y)$ is the input image and $k$ is a scaling factor. Write the mathematical formula for $g_{mask}(x,y)$ in terms of $f(x,y)$ and a blurred version $\bar{f}(x,y)$. Explain how adding this mask sharpens the edges."
*   **Expected Answer:** 
    *   Formula: $g_{mask}(x,y) = f(x,y) - \bar{f}(x,y)$.
    *   Explanation: The mask represents the high-frequency components (details/edges) of the image, obtained by subtracting the blurred image (low-frequencies) from the original. Adding these high frequencies back to the original image increases the contrast at sharp transitions (edges), sharpening the image.

### Question 15: Noise Models & Applications
*   **Type:** Conceptual (Match-Up)
*   **Heading:** `Question 15: Physical Causes of Noise Models`
*   **Question Text:** "Match the following noise models with their typical physical causes in imaging systems:
    
    1. **Gaussian Noise**  
    2. **Salt-and-Pepper Noise**  
    3. **Rayleigh Noise**  
    4. **Poisson (Shot) Noise**  

    **Physical Causes:**  
    A. Occurs due to photon quantization, especially prominent in low-light imaging.  
    B. Typically caused by thermal fluctuations in electronic circuits during capture.  
    C. Caused by transmission errors, faulty CCD sensor pixels, or analog-to-digital converter glitches.  
    D. Often models the noise envelope in range-imaging sensors, radar, and ultrasound scans."
*   **Expected Answer:** 1-B, 2-C, 3-D, 4-A.

### Question 16: Image Registration (Affine vs. Homography Degrees of Freedom)
*   **Type:** Numerical / Conceptual
*   **Heading:** `Question 16: Minimum Points for Registration`
*   **Question Text:** "You want to align two images. If you assume an **Affine** transformation model, what is the minimum number of matching point pairs required to solve for the matrix? If you assume a **Homography** (Projective) transformation, what is the minimum number of matching point pairs required? Explain in terms of the Degrees of Freedom (DoF) for each transformation."
*   **Expected Answer:** 
    *   An Affine transformation has **6 degrees of freedom** (2 translation, 2 scaling, 1 rotation, 1 shearing). Each point correspondence provides 2 independent equations (x and y mapping), so a minimum of **3 point correspondences** is required.
    *   A Homography (Projective) transformation has **8 degrees of freedom** (represented by a $3 \times 3$ matrix defined up to scale). Since each point correspondence provides 2 equations, a minimum of **4 point correspondences** is required.

### Question 17: Intensity-Based Registration Metric (Mutual Information)
*   **Type:** Conceptual
*   **Heading:** `Question 17: SSD vs. Mutual Information`
*   **Question Text:** "In intensity-based image registration, we align images by optimizing a global similarity metric. Why is the Sum of Squared Differences (SSD) metric completely unsuitable for aligning a brain MRI scan with a brain CT scan of the same patient, whereas Mutual Information (MI) works exceptionally well? Explain the core difference in what these metrics measure."
*   **Expected Answer:** SSD assumes that corresponding structures in both images have the same intensity values. MRI and CT scans are multi-modal, meaning the same brain tissue will have completely different gray-scale values in an MRI compared to a CT. Mutual Information does not assume identical intensities; instead, it measures the statistical dependency (information redundancy) between the joint histogram of the two images, identifying when structures line up regardless of their specific gray-scale values.

### Question 18: Feature-Based Scale Space (Difference of Gaussians)
*   **Type:** Conceptual
*   **Heading:** `Question 18: SIFT Scale Space Approximation`
*   **Question Text:** "In feature-based registration algorithms like SIFT, keypoints must be detected at multiple scales. SIFT uses a 'Difference of Gaussians' (DoG) pyramid to find stable keypoints. What mathematically rigorous operator does the DoG approximate, and why does SIFT use DoG instead of calculating that operator directly?"
*   **Expected Answer:** The DoG approximates the **Laplacian of Gaussian (LoG)** operator. SIFT uses DoG because it is computationally much more efficient: it can be calculated by simply subtracting adjacent smoothed images in the Gaussian pyramid scale space, avoiding the expensive second-order spatial derivatives required to calculate the Laplacian directly.

### Question 19: Frequency domain Filtering Mask Identification
*   **Type:** Visual Recognition (MCQ & Explanation)
*   **Heading:** `Question 19: Identify the Frequency Filter`
*   **Image:** `overall_q19_frequency.png`
*   **Question Text:** "Refer to the two frequency domain filter masks above. Describe what spatial frequencies Mask 1 and Mask 2 pass through. If you apply Mask 1 to an image, will the spatial domain result look blurry or sharpened? Explain."
*   **Expected Answer:** 
    *   Mask 1 is a **Low-Pass Filter** (passes low frequencies near the center and blocks high frequencies). Applying it results in a **blurry/smoothed** spatial image because high-frequency details (edges, noise) are removed.
    *   Mask 2 is a **High-Pass Filter** (blocks low frequencies in the center and passes high frequencies). Applying it results in a sharpened image containing only the edges/transitions.

### Question 20: Wiener Filter vs. Inverse Filter
*   **Type:** Conceptual (Image Restoration)
*   **Heading:** `Question 20: Wiener Filtering Noise Mitigation`
*   **Question Text:** "During image restoration, why does standard Inverse Filtering perform terribly in the presence of noise, and how does the Wiener Filter mathematically overcome this issue? Focus on the role of the noise-to-signal power spectrum ratio."
*   **Expected Answer:** Inverse filtering divides the degraded image's Fourier transform by the degradation function $H(u,v)$. At high frequencies where $H(u,v)$ is close to zero, this division amplifies the noise. The Wiener Filter models the noise and signal power spectra, adding a ratio term $S_\eta(u,v)/S_f(u,v)$ (noise-to-signal ratio) in the denominator. When the noise is high, this term dominates, preventing division by zero and suppressing noise amplification.

---

## 📐 Section C: Projective Geometry, Camera Models & Stereo

### Question 21: Homogeneous Coordinates Conversions
*   **Type:** Numerical / Conceptual
*   **Heading:** `Question 21: Conversions in Projective Space`
*   **Question Text:** "
    1. Convert the Homogeneous coordinate point $P = [8, 12, 4]^T$ into its Euclidean (Cartesian) coordinate counterpart.  
    2. In homogeneous coordinates, what physical geometric concept is represented by the point $Q = [2, -7, 0]^T$?"
*   **Expected Answer:** 
    1. Euclidean: Divide by the third coordinate $w=4 \implies [8/4, 12/4]^T = \mathbf{[2, 3]^T}$.
    2. Concept: A **point at infinity** in the direction of the vector $[2, -7]^T$ (representing parallel lines meeting at infinity in this direction).

### Question 22: Parallel Lines Intersection in Projective Space
*   **Type:** Mathematical Proof
*   **Heading:** `Question 22: Intersection of Parallel Lines`
*   **Question Text:** "In 2D projective geometry, parallel lines meet at infinity. Consider two parallel lines in Cartesian coordinates: $y = 2x + 1$ and $y = 2x + 3$. Convert these lines into homogeneous representations $l_1$ and $l_2$. Calculate their intersection point $x = l_1 \times l_2$ using the cross product, and prove that it lies on the line at infinity $l_\infty = [0, 0, 1]^T$."
*   **Expected Answer:** 
    *   Cartesian to Homogeneous: $2x - y + 1 = 0 \implies l_1 = [2, -1, 1]^T$ and $2x - y + 3 = 0 \implies l_2 = [2, -1, 3]^T$.
    *   Intersection: $x = l_1 \times l_2 = \begin{vmatrix} i & j & k \\ 2 & -1 & 1 \\ 2 & -1 & 3 \end{vmatrix} = i(-3 - (-1)) - j(6 - 2) + k(-2 - (-2)) = -2i - 4j + 0k \implies \mathbf{[-2, -4, 0]^T}$.
    *   Proof: The dot product with $l_\infty = [0, 0, 1]^T$ is $[-2, -4, 0] \cdot [0, 0, 1]^T = 0$. Since the dot product is 0, the intersection point lies on the line at infinity.

### Question 23: Vanishing Points & Horizon Shifts
*   **Type:** Conceptual / Geometrical
*   **Heading:** `Question 23: Vanishing Points and Camera Tilt`
*   **Question Text:** "You are standing on a street looking straight down a flat, level road. The parallel edges of the sidewalk meet at a vanishing point on the horizon line in your image. Keeping the camera in the exact same physical spot, you tilt the camera axis upwards by 15 degrees. In your new image, does the vanishing point of the sidewalk move UP, DOWN, or stay in the EXACT SAME pixel coordinate? Why?"
*   **Expected Answer:** **DOWN**. 
    *   Explanation: The vanishing point of horizontal parallel lines lies on the horizon. Tilting the camera upwards shifts the image sensor relative to the horizon, causing the horizon line (and everything on it) to move downward in the captured frame coordinates.

### Question 24: Pinhole Matrix Matrix Decompositions
*   **Type:** Conceptual (Camera Matrix)
*   **Heading:** `Question 24: Projective Matrix Transformations`
*   **Question Text:** "A camera projection matrix is defined as $P = K[R|t]$. You translate the camera physically to the right by $3 \text{ meters}$ and rotate it by $10 \text{ degrees}$ about its optical axis. Which component matrices of $P$ (Intrinsic matrix $K$, Extrinsic rotation $R$, or Extrinsic translation $t$) are modified by this action? Explain."
*   **Expected Answer:** The Extrinsic matrices $R$ (rotation) and $t$ (translation) are modified. The Intrinsic matrix $K$ remains unchanged because the physical hardware parameters of the camera (focal length, sensor pitch, optical center) were not adjusted.

### Question 25: Intrinsic Camera Matrix Parameters
*   **Type:** Conceptual (Matrix Elements)
*   **Heading:** `Question 25: Anatomy of the Intrinsic Matrix K`
*   **Question Text:** "Let the intrinsic camera matrix $K$ be represented as:
    
    $$K = \begin{bmatrix} f_x & s & x_0 \\ 0 & f_y & y_0 \\ 0 & 0 & 1 \end{bmatrix}$$
    
    Identify what physical parameters of the camera sensor/lens are represented by:
    1. $f_x$ and $f_y$ (and why they might differ slightly)  
    2. $x_0$ and $y_0$  
    3. $s$"
*   **Expected Answer:** 
    1. $f_x$ and $f_y$ represent the focal length in terms of pixel dimensions along the x and y axes. They differ if the sensor pixels are non-square (rectangular).
    2. $x_0$ and $y_0$ represent the coordinates of the principal point (the intersection of the optical axis with the sensor plane, in pixel coordinates).
    3. $s$ is the skew parameter, which is non-zero if the sensor's pixel axes are not perfectly perpendicular (almost always zero in modern sensors).

### Question 26: Lens Distortion Physics
*   **Type:** Matching Match-Up
*   **Heading:** `Question 26: Barrel, Pincushion, and Tangential Distortion`
*   **Question Text:** "Match the following optical distortions with their physical causes and behaviors:
    
    1. **Radial (Barrel) Distortion**  
    2. **Radial (Pincushion) Distortion**  
    3. **Tangential Distortion**  

    **Descriptions:**  
    A. Occurs because the lens elements are not perfectly parallel to the image sensor plane, causing asymmetric warping.  
    B. Magnification increases with distance from the optical axis; straight lines are bent inward toward the center.  
    C. Magnification decreases with distance from the optical axis; straight lines bend outward away from the center, typical in wide-angle lenses."
*   **Expected Answer:** 1-C, 2-B, 3-A.

### Question 27: Rectified Epipolar Slope
*   **Type:** Conceptual (Stereo rig)
*   **Heading:** `Question 27: Rectified Stereo Epipolar Constraints`
*   **Question Text:** "In a perfectly rectified stereo rig (identical parallel cameras looking straight ahead), the epipoles are shifted to infinity. Describe the orientation (vertical, horizontal, or skewed) and the mathematical slope of the epipolar lines in both image planes. How does this simplify the stereo correspondence search?"
*   **Expected Answer:** The epipolar lines are **perfectly horizontal** with a mathematical slope of **0**. This simplifies the stereo correspondence search because matching points are guaranteed to lie on the same horizontal scanline ($y = y'$), reducing a 2D search space to a 1D line search.

### Question 28: Disparity-to-Depth Calculations
*   **Type:** Numerical Calculation
*   **Heading:** `Question 28: Calculating Distance from Disparity`
*   **Question Text:** "A rectified stereo camera rig has a baseline (distance between camera centers) of $B = 12 \text{ cm}$. Both lenses have a focal length of $f = 600 \text{ pixels}$. After matching features, a specific 3D point is projected with a coordinate of $x_L = 400 \text{ pixels}$ in the left image and $x_R = 375 \text{ pixels}$ in the right image. Calculate:
    1. The disparity $d$ in pixels.  
    2. The exact depth (distance) $Z$ of the 3D point from the camera rig in meters."
*   **Expected Answer:** 
    *   Disparity: $d = x_L - x_R = 400 - 375 = \mathbf{25 \text{ pixels}}$.
    *   Depth: $Z = \frac{f \cdot B}{d}$. 
        *   $B = 12 \text{ cm} = 0.12 \text{ m}$
        *   $Z = \frac{600 \cdot 0.12}{25} = \frac{72}{25} = \mathbf{2.88 \text{ meters}}$.

### Question 29: Identifying the Epipole (Visual-Related)
*   **Type:** Visual Identification (MCQ & Explanation)
*   **Heading:** `Question 29: Anatomy of Epipolar Geometry`
*   **Image:** `overall_q29_epipolar.png`
*   **Question Text:** "Refer to the diagram above. Identify which of the labels (Label A or Label B) represents the epipole of the Left camera's image plane. Define what an 'epipole' represents in terms of projection."
*   **Expected Answer:** Label A represents the epipole of the Left camera. An epipole represents the projection of one camera's optical center onto the other camera's image plane. In this case, the baseline line connecting $C_L$ and $C_R$ intersects the left image plane at Label A.

### Question 30: Homography vs. Fundamental Matrix
*   **Type:** Conceptual Matrix Differences
*   **Heading:** `Question 30: Planar vs. Non-Planar Stereo Mapping`
*   **Question Text:** "You are observing a scene with two cameras. 
    1. If the scene consists entirely of a flat 2D wall, what matrix (Homography $H$, or Fundamental matrix $F$) relates the coordinates of corresponding points in both images?  
    2. If the scene contains a 3D structure (like a rocky terrain), which matrix must be used to describe the geometric constraint between views?"
*   **Expected Answer:** 
    1. A **Homography matrix ($H$)** relates points between images when the scene is planar.
    2. A **Fundamental matrix ($F$)** (under epipolar constraint $x'^T F x = 0$) must be used when the scene contains general 3D structures.
