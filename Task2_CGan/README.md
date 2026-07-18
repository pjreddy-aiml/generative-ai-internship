# Task 2 – Conditional Generative Adversarial Network (CGAN)

## Objective
The objective of this project is to build a Conditional Generative Adversarial Network (CGAN) capable of generating simple grayscale images based on class labels. The model learns to generate a circle when provided with the "circle" label and a square when provided with the "square" label.

## Dataset
A custom synthetic dataset was created using Python. It consists of grayscale images of:
- Circle
- Square

Each image has a resolution of **64 × 64** pixels.

## Methodology
- Generated a labeled dataset of circles and squares.
- Loaded and preprocessed the dataset using PyTorch.
- Built a Conditional Generator and Discriminator.
- Trained the CGAN using Binary Cross Entropy (BCE) loss and the Adam optimizer.
- Generated images conditioned on class labels to evaluate the model.

## Technologies Used
- Python
- PyTorch
- Torchvision
- Matplotlib
- Google Colab

## Results
The trained CGAN successfully learned the relationship between class labels and generated images. The model was able to produce different outputs for circles and squares, demonstrating the concept of conditional image generation.

## Project Structure

Task2_CGan/
├── dataset/
├── outputs/
├── training/
├── models/
├── Task2_CGan.ipynb
└── README.md
