import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import VGG16
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.models import Model
from keras.models import Sequential



train_data_dir = r'D:\projects\MLproject\classfication_sweets\india_sweet_predections\sweets_classfications\downloaded_images\train'
validation_data_dir = r'D:\projects\MLproject\classfication_sweets\india_sweet_predections\sweets_classfications\downloaded_images\validation'
test_data_dir = r'D:\projects\MLproject\classfication_sweets\india_sweet_predections\sweets_classfications\downloaded_images\test'

img_width, img_height = 128, 128
batch_size = 32
epochs = 10   # number of epochs for training
num_classes = 6  # no.of classes in your dataset or types of datasets

# Data augmentation
train_datagen = ImageDataGenerator(
    rescale=1.0/255.0,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

test_datagen = ImageDataGenerator(rescale=1.0/255.0)

# Data generators
train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical'
)

validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical'
)

# Load pre-trained   model
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(img_width, img_height, 3))

# from keras.layers import Conv2D
# from keras.layers import MaxPooling2D
# from keras.models import Sequential

# model = Sequential()
# x =model.add(Conv2D(32,(3,3),activation='relu',padding='same',input_shape=(img_width, img_height)))
# x = model.add(Conv2D(32,(3,3),activation='relu',padding='same',input_shape=(img_width, img_height)))(x)
# x = MaxPooling2D((2,2),stride=(2,2))(x)


for layer in base_model.layers:
    layer.trainable = False

# Add new fully connected layers
x = Flatten()(base_model.output)
x = Dense(256, activation='relu')(x)
output = Dense(num_classes, activation='softmax')(x)

# Create the model
model = Model(inputs=base_model.input, outputs=output)

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
# history = model.fit(
#     train_generator,
#     steps_per_epoch=train_generator.samples // batch_size,
#     epochs=epochs,
#     validation_data=validation_generator,
#     validation_steps=validation_generator.samples // batch_size
# )

model = Sequential()
model.add(Dense(5, input_dim=2, activation='relu', kernel_initializer='he_uniform'))
model.add(Dense(5, activation='relu', kernel_initializer='he_uniform'))
model.add(Dense(3, activation='softmax'))

history = model.fit(
    train_generator,
    epochs=epochs,
    validation_data=validation_generator
)


# Evaluate the model
test_generator = test_datagen.flow_from_directory(
    test_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical',
    shuffle=False
)

score = model.evaluate(test_generator)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

# Model 
model.save('indain_sweets_models2_final.h5')

import matplotlib.pyplot as plt

##  -------- Graph -------
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Loss Curve')
plt.legend()
plt.show()

# Plot accuracy curve
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.title('Accuracy Curve')
plt.legend()

plt.savefig("acccuracy_epoch.png", format='png', facecolor='g', bbox_inches="tight",
            pad_inches=0.3, transparent=True)

plt.show()