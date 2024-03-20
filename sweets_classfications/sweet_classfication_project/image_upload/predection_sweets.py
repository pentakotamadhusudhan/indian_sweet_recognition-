import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

# Load the saved model
# model = load_model(r"D:\projects\MLproject\classfication_sweets\india_sweet_predections\sweets_classfications\indain_sweets_models2.h5")
model = load_model(r"D:\projects\MLproject\classfication_sweets\india_sweet_predections\sweets_classfications\indain_sweets_models2_final.h5")
# Function to preprocess the image
def preprocess_image(img_path, target_size=(128, 128)):
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Function to perform prediction
def predict_image(model=model, img_path=None):
    img_array = preprocess_image(img_path)
    # prediction
    predictions = model.predict(img_array)
    print(predictions)
    # Get the predicted class index
    predicted_class = np.argmax(predictions)
    print(predicted_class)
    return predicted_class

class_names = ['gulab jamun','jalebi','kajja','Kaju katli','kalakand','modak','cake']
# Example usage
# image_path = r"D:\projects\MLproject\classfication_sweets\india_sweet_predections\sweets_classfications\downloaded_images\train\kalakand\kalakand_29.jpeg"  # Replace with the path to your image
# predicted_class = predict_image(model, image_path)
# print("Predicted class index:", predicted_class)
# print("Predicted class :", class_names[predicted_class])
