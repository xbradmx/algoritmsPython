  # Data loading and preprocessing
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.utils import to_categorical
import numpy as np

#def load_mnist():           # - Download and load the dataset
  # Loads the MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()



def preprocess_data():      # - Normalize pixel values (0-255 → 0-1) and flatten 28*28 image
  global x_train, x_test, y_train, y_test
  x_train = x_train / 255.0
  x_test = x_test / 255.0
  ####
  # plt.imshow(x_train[0].reshape(28, 28), cmap='gray')
  # plt.title(f"Label: {y_train[0]}")
  # plt.show()
  #####

  

  x_train = x_train.reshape(60000, 784)
  x_test = x_test.reshape(10000, 784)
  
  #plt.title(f"Label: {np.argmax(y_train[0])}")


def one_hot_encode():       # - Convert labels (5 → [0,0,0,0,0,1,0,0,0,0])
  global x_train, x_test, y_train, y_test
  y_train = to_categorical(y_train)
  y_test = to_categorical(y_test)
  print("x_train shape:", x_train.shape)
  print("y_train shape:", y_train.shape)


def create_batches():       #- Group data for efficient training 
  pass


def testing_mnist():
  # load_mnist()
  # for x in range(1,10):
  plt.imshow(x_train[2], cmap='gray')
  plt.title(f"Label: {y_train[2]}")
  plt.show()



preprocess_data()
one_hot_encode()

#testing_mnist()
