# -*- coding: utf-8 -*-
"""CIND_860_Notebook1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ezy-8T6UQK6YhARpox7bHemE6Oj-cLIF
"""

from google.colab import drive
drive.mount('/content/drive')

import os
import shutil
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import VGG16
from tensorflow.keras.layers import Flatten, Dense, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from PIL import Image
import matplotlib.pyplot as plt

# from google.colab import drive
# drive.flush_and_unmount()

# Path to the dataset in Google Drive
data_path = '/content/drive/MyDrive/RealWaste'

# Initialize statistics
class_counts = {}
image_dimensions = []

# Iterate over each class directory
for class_dir in os.listdir(data_path):
    if not os.path.isdir(os.path.join(data_path, class_dir)):
        continue
    class_counts[class_dir] = 0
    for image_name in os.listdir(os.path.join(data_path, class_dir)):
        image_path = os.path.join(data_path, class_dir, image_name)
        with Image.open(image_path) as img:
            image_dimensions.append(img.size)
        class_counts[class_dir] += 1

# Calculate summary statistics
total_images = sum(class_counts.values())
min_dim = min(image_dimensions)
max_dim = max(image_dimensions)
mean_dim = np.mean(image_dimensions, axis=0).astype(int)
std_dev_dim = np.std(image_dimensions, axis=0).astype(int)

# Display the statistics
print(f"Total number of classes: {len(class_counts)}")
print(f"Total number of images: {total_images}")
print(f"Number of images per class: {class_counts}")
print(f"Image dimensions (WxH): Min {min_dim}, Max {max_dim}, Mean {mean_dim}, Std Dev {std_dev_dim}")

class_image_counts = {'Paper': 510, 'Cardboard': 461, 'Miscellaneous Trash': 495, 'Textile Trash': 318, 'Metal': 810, 'Vegetation': 436, 'Plastic': 921, 'Glass': 420, 'Food Organics': 411}

# Plotting
plt.figure(figsize=(10, 8))
plt.bar(class_image_counts.keys(), class_image_counts.values(), color='skyblue')
plt.xlabel('Class')
plt.ylabel('Number of Images')
plt.xticks(rotation=45, ha="right")
plt.title('Number of Images per Class')
plt.tight_layout()  # Adjust subplot parameters to give specified padding
plt.show()

def split_data(data_path, subset_percentage=0.3, test_size=0.3):
    class_dirs = [d for d in os.listdir(data_path) if os.path.isdir(os.path.join(data_path, d))]

    for class_dir in class_dirs:
        full_class_path = os.path.join(data_path, class_dir)
        image_files = [f for f in os.listdir(full_class_path) if os.path.isfile(os.path.join(full_class_path, f))]
        np.random.shuffle(image_files)  # Shuffle the list of files

        # Take a subset of the total images
        subset_size = int(len(image_files) * subset_percentage)
        image_subset = image_files[:subset_size]

        if len(image_subset) > 1:
            train_files, test_files = train_test_split(image_subset, test_size=test_size, random_state=42)

            train_class_dir = os.path.join(data_path, 'train', class_dir)
            test_class_dir = os.path.join(data_path, 'test', class_dir)
            os.makedirs(train_class_dir, exist_ok=True)
            os.makedirs(test_class_dir, exist_ok=True)

            for f in train_files:
                shutil.copy(os.path.join(full_class_path, f), os.path.join(train_class_dir, f))

            for f in test_files:
                shutil.copy(os.path.join(full_class_path, f), os.path.join(test_class_dir, f))
        else:
            print(f"Not enough images in {class_dir} to perform a split. Found {len(image_subset)} files.")

## only to be run to put images back to original folders from train and test


# # The original class directories are assumed to be at the same level as 'train' and 'test'
# classes = [d for d in os.listdir(data_path) if os.path.isdir(os.path.join(data_path, d)) and d not in ['train', 'test']]

# # Move files back to their original class folders
# for class_name in classes:
#     # Define paths for train and test folders for this class
#     train_class_path = os.path.join(data_path, 'train', class_name)
#     test_class_path = os.path.join(data_path, 'test', class_name)
#     original_class_path = os.path.join(data_path, class_name)

#     # Move files from train folder back to the original class folder
#     if os.path.exists(train_class_path):
#         for file_name in os.listdir(train_class_path):
#             shutil.move(os.path.join(train_class_path, file_name), os.path.join(original_class_path, file_name))

#     # Move files from test folder back to the original class folder
#     if os.path.exists(test_class_path):
#         for file_name in os.listdir(test_class_path):
#             shutil.move(os.path.join(test_class_path, file_name), os.path.join(original_class_path, file_name))

# Run the split function
split_data(data_path)

# Define your ImageDataGenerators
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    fill_mode='nearest'
)

test_datagen = ImageDataGenerator(rescale=1./255)

# Training and validation generators
train_generator = train_datagen.flow_from_directory(
    os.path.join(data_path, 'train'),
    target_size=(524, 524),
    batch_size=4,
    class_mode='categorical'
)

test_generator = test_datagen.flow_from_directory(
    os.path.join(data_path, 'test'),
    target_size=(524, 524),
    batch_size=4,
    class_mode='categorical'
)

# Number of classes
num_classes = len(os.listdir(os.path.join(data_path, 'train')))

print(num_classes)

# Build the VGG16 model
vgg16_base = VGG16(weights='imagenet', include_top=False, input_shape=(524, 524, 3))
vgg16_base.trainable = False

model = Sequential([
    vgg16_base,
    Flatten(),
    Dense(256, activation='relu'),
    Dense(num_classes, activation='softmax')
])

model.compile(optimizer=Adam(lr=1e-5), loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // train_generator.batch_size,
    epochs=5,
    validation_data=test_generator,
    validation_steps=test_generator.samples // test_generator.batch_size
)

# Save the model to Google Drive
model.save('/content/drive/My Drive/Models/vgg16_waste_classifier_model1.keras')
