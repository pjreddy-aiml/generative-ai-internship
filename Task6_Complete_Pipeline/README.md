# Task 6 – Complete Text-to-Image Generation Pipeline

## Overview

This task integrates the major components developed throughout the project into a complete text-to-image generation pipeline.

The pipeline accepts a natural-language description, preprocesses and tokenizes the text, generates CLIP-based text embeddings, and uses those embeddings to condition a GAN for image generation.

## Pipeline

```text
Text Prompt
     ↓
Text Preprocessing
     ↓
CLIP Tokenization
     ↓
CLIP Text Encoder
     ↓
Text Embeddings
     ↓
Text-Conditioned GAN
     ↓
Generated Image
     ↓
Visualization & Output

##Dataset

A custom landscape image dataset is used for training.
Image Preprocessing
Images are converted to grayscale.
Images are resized to 64 × 64.
Images are converted to PyTorch tensors.
Pixel values are normalized to the [-1, 1] range.
A PyTorch DataLoader is used for batch-based training.
Text Processing
The input text description is processed using the CLIP tokenizer.
The tokenizer converts the natural-language prompt into a sequence of 77 tokens, including the required attention information.
Example:
Input:
"a beautiful landscape with mountains, trees and a blue sky"

Tokenized shape:
[1, 77]
Text Embedding
A pretrained CLIP text encoder converts the tokenized prompt into numerical text representations.
The resulting text embedding has the shape:
[1, 77, 512]
These embeddings provide the textual conditioning information used by the Generator.
GAN Architecture

#Generator
The Generator combines:
Random latent noise
CLIP text embeddings
The text representation is projected into a smaller feature space and combined with the latent noise vector. The resulting representation is progressively upsampled to generate a 64 × 64 grayscale image.

#Discriminator
The Discriminator receives:
Real or generated images
CLIP text embeddings
It extracts image features, combines them with the text representation, and predicts whether the image is real or generated.
Training
The Generator and Discriminator are trained using adversarial training.

##Configuration

Image size: 64 × 64
Latent dimension: 100
Text embedding dimension: 512
Batch size: 2
Epochs: 50
Loss function: Binary Cross-Entropy
Optimizer: Adam
Learning rate: 0.0002
Adam betas: (0.5, 0.999)
GPU acceleration: CUDA when available

##Results

After training, the Generator successfully produced text-conditioned images with the expected output shape:
[4, 1, 64, 64]
The generated images are visualized using Matplotlib and saved as:
outputs/text_conditioned_generated_images.png

##Project Structure

Task6_Text_to_Image_Pipeline/
│
├── Task6_Text_to_Image_Pipeline.ipynb
├── README.md
│
└── outputs/
    └── text_conditioned_generated_images.png

##Conclusion

Task 6 integrates text preprocessing, CLIP-based text embedding creation, and GAN-based image generation into a single end-to-end text-to-image pipeline.
The completed implementation demonstrates how a natural-language prompt can be processed into text embeddings and used as conditioning information for generating images through a GAN.