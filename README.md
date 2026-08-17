# CEVI Lab Summer School - Day 1 Visual Challenge

This workspace contains a daily engagement tracking module for **Session 1: Image Transforms & Camera Models**. It focuses on helping students visually understand the difference between **forward mapping** and **backward mapping** under rotation.

---

## 🛠️ Step 1: Generate Visual Assets
To generate the comparison images, you will need to run the Python script.

### Requirements:
Install OpenCV and NumPy (if not already installed):
```bash
pip install opencv-python numpy
```

### Run the Script:
Execute the generator:
```bash
python generate_images.py
```
This will produce two images in the current directory:
*   `image_A_forward.png`: Exposes discretization gaps (holes) caused by forward mapping.
*   `image_B_backward.png`: Demonstrates solid pixels with aliased stair-stepping (jagged edges) caused by Nearest Neighbor backward mapping.

---

## 📬 Step 2: Configure the Formspree Endpoint
To receive students' responses, set up a form collector:
1. Go to [Formspree](https://formspree.io/) and create a free account.
2. Create a new form project and obtain your unique API endpoint (e.g., `https://formspree.io/f/xbjnqypz`).
3. Open `index.html` and replace `YOUR_FORMSPREE_ENDPOINT_HERE` with your actual Formspree form URL in the `action` attribute:
   ```html
   <form action="https://formspree.io/f/YOUR_ENDPOINT_ID" method="POST">
   ```

---

## 🌐 Step 3: Deploy to GitHub Pages
To host this submission page for free:
1. **Create a GitHub Repository:** Create a new public or private repository on GitHub (e.g., `cevi-day1-challenge`).
2. **Commit and Push:** Initialize git in this directory, add the files, and push them to your repository:
   ```bash
   git init
   git add index.html image_A_forward.png image_B_backward.png
   git commit -m "Deploy Day 1 Challenge"
   git branch -M main
   git remote add origin https://github.com/your-username/cevi-day1-challenge.git
   git push -u origin main
   ```
3. **Enable GitHub Pages:**
   * Go to your repository settings page on GitHub.
   * Under the **Code and automation** sidebar section, click **Pages**.
   * Under **Build and deployment**, set the Source to **Deploy from a branch**.
   * Choose the `main` branch and `/ (root)` folder, then click **Save**.
   * Within a few minutes, your site will be live at: `https://your-username.github.io/cevi-day1-challenge/`.
