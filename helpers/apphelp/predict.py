import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
import h5py
from keras.models import load_model
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from tensorflow.python.keras.backend import set_session
# import tensorflow as tf
import tensorflow.compat.v1 as tf

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.imagenet_utils import decode_predictions
# import matplotlib.pyplot as plt
import numpy as np
from keras.applications import vgg16
import datetime
import traceback
# from . import models

def predict(f):

    #get the file
    file_name = "pic.jpg"
    file_name_2 = default_storage.save(file_name, f)
    file_url = default_storage.url(file_name_2)
    file_url = file_url[1:]

    # with tf.Session():
    original = load_img(file_url, target_size=(224, 224))
    numpy_image = img_to_array(original)
    image_batch = np.expand_dims(numpy_image, axis=0)
    # prepare the image for the VGG model
    processed_image = vgg16.preprocess_input(image_batch.copy())

    # model = load_model('best_model.h5')
    ans = settings.MY_MODEL.predict(processed_image)
    classes_list = [
        '250ar-Money',
        '250en-Money',
        '500ar-Money',
        '500en-Money',
        '1000ar-Money',
        '1000en-Money',
        '5000ar-Money',
        '5000en-Money',
        '10000ar-Money',
        '10000en-Money',
        '25000ar-Money',
        '25000en-Money',
        '50000ar-Money',
        '50000en-Money',
        'Food Items',
        'Used Clothes',
        'Battery',
        'Metal',
        'Used Shoes',
        'Plastic',
        'Paper/Cardboard',
        'Glass',
        'New Clothes/Shoes',
        'Watches',
        'Sunglasses',
        'Handbags',
        'Belts',
        'Jewellery',
        'Daily Necessities'
    ]
    ans = np.argmax(ans)
    category = classes_list[ans]
    return ans, category