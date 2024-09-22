import keras.api
import tensorflow as tf
import keras
import os
import sys 
import time as t
import pickle
source_dir = sys.argv[1];
train_dataset, validation_dataset = keras.preprocessing.image_dataset_from_directory(source_dir, validation_split=0.2, subset="both", seed=665, label_mode="categorical");
model = keras.models.Sequential()
model.add(keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(256, 256, 3)))
model.add(keras.layers.MaxPooling2D(2, 2))
model.add(keras.layers.Conv2D(128, (3, 3), activation='relu'))
model.add(keras.layers.MaxPooling2D(2, 2))
model.add(keras.layers.Conv2D(128, (3, 3), activation='relu'))
model.add(keras.layers.MaxPooling2D(2, 2))
model.add(keras.layers.Conv2D(128, (3, 3), activation='relu'))
model.add(keras.layers.MaxPooling2D(2, 2))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(1024, activation='relu'))
model.add(keras.layers.Dense(len(train_dataset.class_names), activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

checkpoint = keras.callbacks.ModelCheckpoint(filepath=os.path.join(os.getcwd(), os.path.basename(source_dir)+"_best.keras"), 
                             monitor='val_accuracy', 
                             save_best_only=True)

early_stopping = keras.callbacks.EarlyStopping(monitor='val_accuracy', patience=5, restore_best_weights=True)


hist = model.fit(train_dataset, epochs=50, validation_data=validation_dataset, 
                  callbacks=[checkpoint, early_stopping])

# Salva la storia in un file pickle
with open(os.path.join(os.getcwd(), os.path.basename(source_dir))+'training_history.pkl', 'wb') as file_pi:
    pickle.dump(hist.history, file_pi)

    #tf.saved_model.save(model, os.path.join(os.getcwd(), os.path.basename(source_dir)+"-Model"))
model.save(filepath=os.path.join(os.getcwd(), os.path.basename(source_dir)+"LAST_EPOCH.keras"))