from datasets import load_dataset

dataset = load_dataset("jet-universe/top_landscape")
print(dataset)
sample = dataset["train"][0]
print("\nkeys:", sample.keys())
print("\nSample:")
print(sample)
