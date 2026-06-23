import os

image_folder = "Task1_SD_Finetuning/dataset/landscapes"

for filename in os.listdir(image_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        txt_file = os.path.join(image_folder, os.path.splitext(filename)[0] + ".txt")

        with open(txt_file, "w", encoding="utf-8") as f:
            f.write("beautiful natural landscape photography")
print("Caption generation complete.")
