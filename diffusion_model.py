import os
from PIL import Image, ImageEnhance
import random

# Define directories for resized and augmented images
categories = ['glioma', 'meningioma', 'notumor', 'pituitary']
final_train_dir = 'data/final_train_data'
final_test_dir = 'data/final_test_data'
augmented_train_dir = 'data/augmented_train_data'

# Create directories for resized and augmented images
os.makedirs(final_train_dir, exist_ok=True)
os.makedirs(final_test_dir, exist_ok=True)
os.makedirs(augmented_train_dir, exist_ok=True)

def resize_images(source_dir, target_dir):
    total_resized = 0
    total_errors = 0

    for category in categories:
        category_path = os.path.join(source_dir, category)
        save_path = os.path.join(target_dir, category)
        os.makedirs(save_path, exist_ok=True)

        files = os.listdir(category_path)
        for img_name in files:
            img_path = os.path.join(category_path, img_name)
            try:
                img = Image.open(img_path)
                if img.mode in ['L', 'RGBA']:
                    img = img.convert('RGB')
                img = img.resize((224, 224))
                img.save(os.path.join(save_path, img_name))
                total_resized += 1
            except Exception as e:
                print(f"Error resizing image {img_path}: {e}")
                total_errors += 1

    print(f"Resizing completed: {total_resized} images resized successfully, {total_errors} errors encountered.")

def augment_image(img):
    try:
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(random.uniform(0.7, 1.3))
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(random.uniform(0.7, 1.3))
        img = img.rotate(random.randint(-10, 10))
        return img
    except Exception as e:
        print(f"Error during image augmentation: {e}")
        return None

def augment_images(source_dir, target_dir, augmentation_ratio=0.25):
    total_augmented = 0
    total_errors = 0

    for category in categories:
        category_path = os.path.join(source_dir, category)
        save_path = os.path.join(target_dir, category)
        os.makedirs(save_path, exist_ok=True)

        files = os.listdir(category_path)
        num_augments = int(augmentation_ratio * len(files))

        for img_name in files:
            img_path = os.path.join(category_path, img_name)
            try:
                img = Image.open(img_path)
                if img is None:
                    print(f"Failed to load image: {img_path}")
                    total_errors += 1
                    continue

                for i in range(num_augments // len(files) + 1):
                    augmented = augment_image(img)
                    if augmented is not None:
                        augmented.save(os.path.join(save_path, f"aug_{i}_{img_name}"))
                        total_augmented += 1
                    else:
                        total_errors += 1
            except Exception as e:
                print(f"Error processing image {img_path}: {e}")
                total_errors += 1

    print(f"Augmentation completed: {total_augmented} images augmented successfully, {total_errors} errors encountered.")

# Example usage
if __name__ == "__main__":
    # Resize images
    resize_images('data/original_dataset/Training', final_train_dir)
    resize_images('data/original_dataset/Testing', final_test_dir)

    # Augment training images
    augment_images(final_train_dir, augmented_train_dir)
