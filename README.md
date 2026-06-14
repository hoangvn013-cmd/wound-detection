# Wound Detection and Classification Using Deep Learning

A deep learning project for automatic wound image classification using Transfer Learning with ResNet-50.

---

## Overview

This project aims to develop an Artificial Intelligence system capable of identifying and classifying wound images into different severity levels. The model leverages a pretrained ResNet-50 architecture and applies transfer learning techniques to achieve high classification performance on medical image datasets.

The project covers the complete machine learning workflow, including:

* Data preprocessing
* Dataset annotation processing
* Data augmentation
* Model training
* Model evaluation
* Performance visualization

---

## Objectives

* Automatically classify wound images based on severity.
* Apply transfer learning using a pretrained ResNet-50 model.
* Evaluate model performance using standard classification metrics.
* Visualize training and testing results.

---

## Dataset Preparation

The dataset consists of:

* Wound images (.jpg, .png)
* XML annotation files

### Data Processing Steps

1. Load wound images.
2. Parse XML annotation files.
3. Extract wound labels.
4. Generate metadata.
5. Split data into:

   * Training Set (70%)
   * Validation Set (20%)
   * Test Set (10%)

---

## Image Preprocessing

The following preprocessing techniques are applied:

* Image resizing
* Normalization
* Random horizontal flipping
* Random rotation
* Data augmentation

These techniques help improve model generalization and reduce overfitting.

---

## Model Architecture

The project uses **ResNet-50**, a convolutional neural network pretrained on the ImageNet dataset.

### Transfer Learning Strategy

* Load pretrained ImageNet weights.
* Replace the final fully connected layer.
* Fine-tune the network on wound image data.

### Frameworks

* PyTorch
* Torchvision

---

## Training Configuration

| Parameter     | Value              |
| ------------- | ------------------ |
| Model         | ResNet-50          |
| Optimizer     | Adam               |
| Learning Rate | 0.0001             |
| Loss Function | CrossEntropyLoss   |
| Batch Size    | 32                 |
| Epochs        | 20                 |
| Hardware      | GPU (Google Colab) |

---

## Evaluation Metrics

Model performance is evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

The project also generates:

* Classification Reports
* Training Accuracy Curves
* Validation Accuracy Curves
* Loss Curves

---

## Results

The pretrained ResNet-50 model significantly improves classification performance by leveraging knowledge learned from ImageNet.

Benefits include:

* Faster convergence
* Reduced training time
* Improved classification accuracy
* Better feature extraction capability

---

## Technologies Used

* Python
* PyTorch
* Torchvision
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-Learn
* Google Colab

---

## Project Structure

```text
Wound-Classification/
│
├── imgs/
│   ├── image_01.jpg
│   ├── image_02.jpg
│   └── ...
│
├── annotations/
│   ├── image_01.xml
│   ├── image_02.xml
│   └── ...
│
├── metadata_wound.csv
│
├── Ai_nhan_dien_vet_thuong_va_phan_loai.ipynb
│
└── README.md
```

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/your-username/wound-classification.git
cd wound-classification
```

Install dependencies:

```bash
pip install torch torchvision pandas numpy matplotlib seaborn scikit-learn tqdm
```

---

## Usage

Open the Jupyter Notebook:

```bash
jupyter notebook Ai_nhan_dien_vet_thuong_va_phan_loai.ipynb
```

Run all cells sequentially:

1. Data preprocessing
2. Dataset creation
3. Model initialization
4. Training
5. Evaluation
6. Visualization

---

## Future Improvements

* Implement wound segmentation.
* Deploy the model as a web application using Streamlit.
* Support real-time wound assessment.
* Expand the dataset with additional wound categories.
* Integrate explainable AI techniques (Grad-CAM).

---

## Author

**Hoang Ngo Viet**

Student at Hanoi University of Science (VNU-HUS)

---

## License

This project is developed for educational and research purposes.
