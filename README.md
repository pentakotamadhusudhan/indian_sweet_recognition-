# indian_sweet_recognition

## Requirements
 - Python version :- 3.11.8
 - python -m venv venv
 - venv/Scripts/active
 - pip install -r requirements.txt


## create a validation data
open validation_data_generator.py file
update path of training_data_dir, validation_data_dir and test_data_dir 
<br> 
you can find the all train data and test data in download images folder  
<br>
``train_data_dir = downloaded_images\train'``<br>
``validation_data_dir = downloaded_images\validation'``<br>
``test_data_dir = downloaded_images\test'``<br>

after the update the paths. run the <strong>validation_data_generator.py</strong>  file.
in the validation directory you can see the folders with classes names and all the images are splited into 20% of them

## create model 
there's a file name <strong> creating_model_sweets.py </strong><br>
<br>``train_data_dir = sweets_classfications\downloaded_images\train'``
``validation_data_dir = sweets_classfications\downloaded_images\validation'``
``test_data_dir = sweets_classfications\downloaded_images\test'``<br>
once run the create_model_sweets.py it will create custome model using VGG16 
### VGG16 :
VGG16 is a pre-trained model is CNN(convitional neural network)
it have 16 layesrs deep.
VGG16 stands for 
V - Visual<br>
G - Geomarty<br>
G - Groups<br>
16 - 16layers of deep learning<br>
those  16layers are splited into groups shown below

<img src='https://media.geeksforgeeks.org/wp-content/uploads/20200219152327/conv-layers-vgg16.jpg'><br>
## flattening
In practice, we have to transform the image into very small numbers. For example, if we wanted to identify a dog we could say that the number close to zero identifies the dog and the number nearest to 1 identifies the cat.<br>



`` python manage.py runserver `` <br>
 http://localhost:8000

