# Task 5 – Attention-GAN

## Overview

This task implements an attention-based Generative Adversarial Network (GAN) for generating grayscale landscape images. The model combines class conditioning with CLIP text embeddings and attention mechanisms to improve the relationship between the input text and generated images.

The model consists of a Generator and Discriminator, with self-attention and cross-attention mechanisms incorporated into the architecture.

## Dataset

The model is trained on a custom landscape image dataset.

### Preprocessing

- Images are converted to grayscale.
- Images are resized to `64 × 64`.
- Images are converted to PyTorch tensors.
- Pixel values are normalized.
- A DataLoader is used for training.

A sample of the processed dataset is visualized before training to verify the preprocessing pipeline.

## Model Architecture

### Self-Attention

A self-attention module is incorporated into the network to allow the model to capture relationships between different spatial regions of an image.

### CLIP Text Conditioning

The CLIP model is used to convert a text description into a sequence of text embeddings.

The text embedding produced by CLIP has the shape:

```text
[1, 77, 512]
These embeddings are used to condition the image generation process.
Cross-Attention
A cross-attention module connects the image features with the CLIP text embeddings. This allows the Generator to use information from the text representation while producing image features.

##Generator

The Generator takes:
Random latent noise
Class labels
CLIP text embeddings
and progressively upsamples the latent representation to generate a 64 × 64 grayscale image.

##Discriminator

The Discriminator evaluates generated and real images while also using class information to distinguish between real and generated samples.

##Training

The Generator and Discriminator are trained alternately using:
Binary Cross-Entropy Loss
Adam optimizer
Learning rate: 0.0002
Adam betas: (0.5, 0.999)
Epochs: 100

Training is performed using GPU acceleration when CUDA is available.
The training process records both Generator and Discriminator losses for each epoch.

##Results

After training, the Generator is evaluated using random latent noise, class labels, and CLIP text embeddings.
The generated output has the expected shape:
[batch_size, 1, 64, 64]
Final generated samples are visualized using Matplotlib for qualitative evaluation.

##Project Structure

Task5_Attention_Gan/
│
├── Task5_Attention_Gan.ipynb
├── README.md
│
└── outputs/
    └── download (1).png

##Conclusion

Task 5 demonstrates an attention-based conditional GAN that combines image features with CLIP text representations. The implementation covers dataset preprocessing, self-attention, cross-attention, text conditioning, GAN training, and final image generation.