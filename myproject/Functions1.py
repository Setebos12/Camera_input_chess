
from PIL import Image, ImageTk
import numpy as np

def crop_image(im):
    images = []
    x = 2000/6
    y = 667/2
    for i in range(6):
        images.append(im.crop((i*x, 0, x*(i+1), y)))
    images.append(im.crop((i * x, y, (i + 1) * x, y*2)))
    return images



def resize_and_crop1(image_array, size=(224, 224)):
    # Tworzenie obiektu Image z tablicy NumPy
    image = Image.fromarray(image_array)
    width, height = image.size
    min_dim = min(width, height)
    left = (width - min_dim) // 2

    #1.35
    #1.4
    image = image.crop((left, 0, height+1.376*left, height))

    image = image.resize(size, Image.LANCZOS)


    return image

def model_prediction(model,class_names,camera):
    ret, frame = camera.read()
    frame = resize_and_crop1(frame, (224, 224))


    image = np.asarray(frame, dtype=np.float32).reshape(1, 224, 224, 3)
    image = (image / 127.5) - 1

    # Predicts the model
    prediction = model.predict(image)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]
    num = int(class_name[0])
    return num
        