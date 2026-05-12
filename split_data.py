import os
import random
import shutil

# Paths
source_dir = 'all_images'
train_img_dir = 'final_data/train/images'
train_lab_dir = 'final_data/train/labels'
test_img_dir = 'final_data/test/images'
test_lab_dir = 'final_data/test/labels'

# 1. Find all files that have BOTH a .jpg and a .txt
all_files = os.listdir(source_dir)
images = [f for f in all_files if f.endswith('.jpg')]
valid_pairs = []

for img in images:
    label = img.replace('.jpg', '.txt')
    if label in all_files:
        valid_pairs.append(img)

# 2. Shuffle them so the AI gets a mix of everything
random.shuffle(valid_pairs)

# 3. Calculate the 80/20 split
split_index = int(len(valid_pairs) * 0.8)
train_pairs = valid_pairs[:split_index]
test_pairs = valid_pairs[split_index:]

def move_files(pairs, img_dest, lab_dest):
    for img in pairs:
        # Move Image
        shutil.move(os.path.join(source_dir, img), os.path.join(img_dest, img))
        # Move Label
        label = img.replace('.jpg', '.txt')
        shutil.move(os.path.join(source_dir, label), os.path.join(lab_dest, label))

# 4. Run the move
print(f"Moving {len(train_pairs)} pairs to Train...")
move_files(train_pairs, train_img_dir, train_lab_dir)

print(f"Moving {len(test_pairs)} pairs to Test...")
move_files(test_pairs, test_img_dir, test_lab_dir)

print("Done! Your data is perfectly split.")