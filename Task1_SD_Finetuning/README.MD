# Task 1 - Stable Diffusion Fine-Tuning

## Objective
Fine-tune a Stable Diffusion model using a custom landscape image dataset and generate new landscape images using the trained LoRA weights.

## Project Structure

Task1_SD_Finetuning/
 dataset/
 outputs/
 training/
 Task1_finetuning.ipynb
 lora-landscape-output.zip
 README.md

## Dataset

- Dataset Type: Landscape Images
- Number of Images: 50
- Image-Caption Format:
   image.jpg
   image.txt

Each image has a corresponding caption stored in a text file.

## Model
Base Model:
stable-diffusion-v1-5/stable-diffusion-v1-5
Training Method:
LoRA Fine-Tuning using Hugging Face Diffusers

## Training Configuration

Resolution: 512 × 512
Batch Size: 1
Gradient Accumulation Steps: 4
Learning Rate: 1e-4
Scheduler: Constant
Training Steps: 500
Mixed Precision: FP16


## Results

The fine-tuned LoRA successfully generates landscape images while preserving the style learned from the custom dataset.
Generated sample images are available in the outputs folder.

## Requirements

Python
PyTorch
Diffusers
Transformers
Accelerate
PEFT
Safetensors
Datasets
## Files

Task1_finetuning.ipynb
Notebook containing the complete fine-tuning workflow.

dataset/
Training images and captions.

outputs/
Generated images after fine-tuning.
lora-landscape-output.zip
Exported trained LoRA weights.
