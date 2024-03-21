# import numpy as np
# from tensorflow.keras.preprocessing import image
# from tensorflow.keras.models import load_model

# # Load the saved model
# # model = load_model(r"D:\projects\MLproject\classfication_sweets\india_sweet_predections\sweets_classfications\indain_sweets_models2.h5")
# model = load_model(r"D:\projects\MLproject\classfication_sweets\india_sweet_predections\sweets_classfications\indain_sweets_models2_final.h5")
# # Function to preprocess the image
# def preprocess_image(img_path, target_size=(128, 128)):
#     img = image.load_img(img_path, target_size=target_size)
#     img_array = image.img_to_array(img)
#     img_array = np.expand_dims(img_array, axis=0)
#     return img_array

# # Function to perform prediction
# def predict_image(model=model, img_path=None):
#     img_array = preprocess_image(img_path)
#     # prediction
#     predictions = model.predict(img_array)
#     print(predictions)
#     # Get the predicted class index
#     predicted_class = np.argmax(predictions)
#     print(predicted_class)
#     return predicted_class

# class_names = ['gulab jamun','jalebi','kajja','Kaju katli','kalakand','modak','cake']
# # Example usage
# # image_path = r"D:\projects\MLproject\classfication_sweets\india_sweet_predections\sweets_classfications\downloaded_images\train\kalakand\kalakand_29.jpeg"  # Replace with the path to your image
# # predicted_class = predict_image(model, image_path)
# # print("Predicted class index:", predicted_class)
# # print("Predicted class :", class_names[predicted_class])







import os
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

# Load the saved model
test_dir = r'D:\projects\MLproject\classfication_sweets\india_sweet_predections\sweets_classfications\downloaded_images\test'
model = load_model(r"D:\projects\MLproject\classfication_sweets\india_sweet_predections\sweets_classfications\indain_sweets_models2_final.h5")

# Function to preprocess the image
def preprocess_image(img_path, target_size=(128, 128)):
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0  # Normalize image data
    img_array = img_array.reshape((1,) + img_array.shape)
    return img_array

# Function to perform prediction
def predict_image(model, img_path):
    img_array = preprocess_image(img_path)
    predictions = model.predict(img_array)
    predicted_class = predictions.argmax(axis=-1)[0]
    return predicted_class

class_names = ['gulab juman','jelabi','kajja','kajjukatli','kalakand','modak']

# Initialize lists to store true and predicted labels
true_labels = []
predicted_labels = []

# Iterate through test images and make predictions
for class_name in class_names:
    class_dir = os.path.join(test_dir, class_name)
    for img_name in os.listdir(class_dir):
        img_path = os.path.join(class_dir, img_name)
        true_labels.append(class_names.index(class_name))
        predicted_labels.append(predict_image(model, img_path))

# Compute confusion matrix
conf_matrix = confusion_matrix(true_labels, predicted_labels)

# Plot confusion matrix as heatmap
plt.figure(figsize=(10, 8))
sns.set(font_scale=1.2)  # Adjust font size if necessary
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=class_names, yticklabels=class_names)

# Add labels and title
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title('Confusion Matrix')

# Show plot
plt.show()
