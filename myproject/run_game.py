from keras.models import load_model
from PIL import Image
from Functions1 import crop_image
import numpy as np
import cv2
from game import game
models = []
classes = []
models.append(load_model("/Users/krzysztofrutkowski/Desktop/Models1/keras_model.h5", compile=False))
classes.append(open("/Users/krzysztofrutkowski/Desktop/Models1/labels.txt", "r").readlines())
models.append(load_model("/Users/krzysztofrutkowski/Desktop/Models2/keras_model.h5", compile=False))
classes.append(open("/Users/krzysztofrutkowski/Desktop/Models2/labels.txt", "r").readlines())
im = Image.open("/Users/krzysztofrutkowski/Downloads/Obrazek3.png")
images = crop_image(im)
np.set_printoptions(suppress=True)
camera = cv2.VideoCapture(0)
api_token = "lip_7kIouXh4yvanAQQXoaP2"
game(api_token,models,classes,images,camera)