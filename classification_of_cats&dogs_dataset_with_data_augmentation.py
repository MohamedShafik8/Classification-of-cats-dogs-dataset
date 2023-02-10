# -*- coding: utf-8 -*-
"""Classification of cats&dogs dataset with data augmentation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TsLUW2f104P4eQZNYxh9c4jcRB91CLul
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import tensorflow as tf
from tensorflow import keras

from google.colab import drive
drive.mount('/content/drive')



from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen= ImageDataGenerator(rescale=1./255,
                                  rotation_range=40,
                                  width_shift_range=0.2,
                                  height_shift_range=0.2,
                                  shear_range=0.2,
                                  zoom_range=0.2,
                                  horizontal_flip=True)
test_datagen= ImageDataGenerator(rescale=1./255)

train_generator=train_datagen.flow_from_directory('/content/drive/MyDrive/train',target_size = (150,150), batch_size =20,class_mode='binary')
validation_generator=test_datagen.flow_from_directory('/content/drive/MyDrive/test',target_size = (150,150), batch_size =20,class_mode='binary')

from tensorflow.keras import layers
from tensorflow.keras import models
from keras.models import * 

from keras.layers import *

model= Sequential()
model.add(Conv2D(filters = 32, kernel_size = (3, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(filters = 64, kernel_size = (3, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(filters = 128, kernel_size = (3, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(filters = 128, kernel_size = (3, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(512,activation = 'relu'))
model.add(Dense(128,activation = 'relu'))
model.add(Dense(1,activation = 'sigmoid'))

from tensorflow.keras import optimizers

model.compile(loss='binary_crossentropy',optimizer=optimizers.RMSprop(learning_rate=1e-4),metrics=['accuracy'])

model_fit = model.fit(train_generator,
            steps_per_epoch = 5,
            epochs = 20,
            validation_data = validation_generator,
            validation_steps=10)

plt.plot(model_fit.history['accuracy']) 
plt.title('Model Training Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Training Accuracy')

plt.legend(['Training'], loc='lower right')

model.save('model.h5')

from tensorflow.keras import backend as K
K.clear_session()
del model

