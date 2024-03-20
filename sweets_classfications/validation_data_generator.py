from sklearn.model_selection import train_test_split
import os
import shutil

# Define paths to your dataset
original_data_dir = r'D:\projects\MLproject\classfication_sweets\india_sweet_predections\sweets_classfications\downloaded_images\original'
train_data_dir = r'D:\projects\MLproject\classfication_sweets\india_sweet_predections\sweets_classfications\downloaded_images\train'
validation_data_dir = r'D:\projects\MLproject\classfication_sweets\india_sweet_predections\sweets_classfications\downloaded_images\validation'


if not os.path.exists(validation_data_dir):
    os.makedirs(validation_data_dir)
validation_split = 0.2
class_names = os.listdir(original_data_dir)

for class_name in class_names:
    class_images = os.listdir(os.path.join(original_data_dir, class_name))
    train_images, val_images = train_test_split(class_images, test_size=validation_split, random_state=42)
    train_class_dir = os.path.join(train_data_dir, class_name)
    if not os.path.exists(train_class_dir):
        os.makedirs(train_class_dir)
    val_class_dir = os.path.join(validation_data_dir, class_name)
    if not os.path.exists(val_class_dir):
        os.makedirs(val_class_dir)
    for image in train_images:
        src = os.path.join(original_data_dir, class_name, image)
        dst = os.path.join(train_class_dir, image)
        shutil.copyfile(src, dst)
    for image in val_images:
        src = os.path.join(original_data_dir, class_name, image)
        dst = os.path.join(val_class_dir, image)
        shutil.copyfile(src, dst)
