# Task 4: Text Preprocessing using Hugging Face Transformers

## Objective

The objective of this task is to preprocess natural language text descriptions using the Hugging Face Transformers library. The software tokenizes input text and converts it into encoded numerical embeddings that can be used as inputs for text-to-image generation models.

## Technologies Used

- Python
- PyTorch
- Hugging Face Transformers
- CLIP Tokenizer
- CLIP Text Encoder

## Project Workflow

1. Load the pre-trained CLIP tokenizer and text encoder.
2. Accept a text description from the user.
3. Tokenize the input text.
4. Generate contextual text embeddings.
5. Save the generated embeddings for downstream text-to-image applications.

## Project Structure

```
Task4_Text_Preprocessing/
│
├── Task4_Text_Preprocessing.ipynb
├── outputs/
│   └── text_embeddings.pt
└── README.md
```

## Sample Input

```
A beautiful snowy mountain landscape with pine trees.
```

## Sample Output

- Tokenized input IDs
- Attention mask
- Text embedding tensor

Example embedding shape:

```
torch.Size([1, 77, 512])
```

## Result

The implementation successfully converts natural language descriptions into tokenized and encoded representations using the Hugging Face CLIP model. The generated embeddings are suitable for use as input features in text-to-image generation pipelines.
