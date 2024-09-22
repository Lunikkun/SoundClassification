import pickle
import matplotlib.pyplot as plt
import sys

history_data = sys.argv[1]
# Carica la storia salvata
with open(history_data, 'rb') as file_pi:
    history = pickle.load(file_pi)

# Grafico per la accuratezza
plt.plot(history['accuracy'], label='Training Accuracy')
plt.plot(history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.title('Training and Validation Accuracy')
plt.legend()
plt.show()

# Grafico per la perdita
plt.plot(history['loss'], label='Training Loss')
plt.plot(history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Training and Validation Loss')
plt.legend()
plt.show()
