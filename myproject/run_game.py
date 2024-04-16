from keras.models import load_model
from PIL import Image
from Functions1 import crop_image
import numpy as np
import cv2
from game import game
models = []
classes = []
models.append(load_model("Path to model1", compile=False))
classes.append(open("Path to classes1", "r").readlines())
models.append(load_model("Path to model2", compile=False))
classes.append(open("Path to classes2", "r").readlines())
im = Image.open("png images")
images = crop_image(im)
np.set_printoptions(suppress=True)
camera = cv2.VideoCapture(0)
api_token = "lichess_api_key"
game(api_token,models,classes,images,camera)
