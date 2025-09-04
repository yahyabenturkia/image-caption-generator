
# 🖼️ Image Caption Generator

## 🚀 Project Overview
This project is a full-featured **image caption generator** using a pre-trained **BLIP model**. It generates human-like captions for input images and overlays them on the images in a visually clear format.

---

## ✨ Features
- 📝 Generate captions for multiple images.
- 💾 Save captions to a text file.
- 🖌️ Overlay captions on images with a clean bottom black box.
- 🛠️ Modular Python codebase for easy extension.

---

## 🧰 Technologies Used
- Python 3.10+
- PyTorch
- HuggingFace Transformers
- PIL (Pillow)
- tqdm
- NumPy

Optional for notebooks:
- Jupyter Notebook / JupyterLab
- ipywidgets
- matplotlib

---

## 📂 Project Structure

````
image-caption-generator/
│
├── data/                         # Input images
├── notebooks/                    # Jupyter notebooks for testing & experimentation
├── src/                          # Source code
│   ├── preprocess.py             # Image preprocessing functions
│   ├── model.py                  # Load pre-trained BLIP model
│   ├── inference.py              # Generate captions for images
│   └── utils.py                  # Helper functions
├── outputs/                      # Generated captions and images
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
└── environment.yml               # Conda environment (optional)

````


## ⚡ Installation

1. Clone the repository:
````
git clone <your-repo-link>
cd image-caption-generator
````

2. (Optional) Create and activate a conda environment:

```
conda env create -f environment.yml
conda activate cv_project
```

3. Install dependencies:

```
pip install -r requirements.txt
```

---

## 🏃‍♂️ Usage

1. Add your input images to the `data/` folder.
2. Run inference to generate captions and overlay them on images:

```bash
python src/inference.py
```

3. Captions will be saved in `outputs/captions.txt` and images with overlaid captions in `outputs/results/`.

---

## 📓 Jupyter Notebooks (Optional)

* `01_data_preprocessing.ipynb` — Test and preprocess images.
* `02_model_inference.ipynb` — Generate captions interactively.

> To run notebooks correctly, install these optional dependencies:

```bash
pip install jupyter ipywidgets matplotlib
```

> Then launch Jupyter:

```bash
jupyter notebook
```

---

## 👨‍💻 Author

**Yahya Ben Turkia**

```
