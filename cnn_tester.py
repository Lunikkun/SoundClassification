import PIL.Image
import tensorflow as tf
import sys, os
import keras, PIL
import numpy as np
source_path = sys.argv[1]
img = sys.argv[2];

model = keras.models.load_model(source_path);
img = PIL.Image.open(img).convert('RGB');
img = img.resize(size=[256,256]);

img_array = keras.preprocessing.image.img_to_array(img, dtype='float32');
img_array = tf.expand_dims(img_array, axis=0)

converted = tf.convert_to_tensor(img_array)

prediction = model.predict(converted);

for hyp in prediction[0]:
    print(hyp)