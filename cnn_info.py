import tensorflow as tf
import keras 
import os, sys

model_path = sys.argv[1];

model = keras.models.load_model(model_path);
model.evaluate()