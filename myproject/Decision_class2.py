import tkinter as tk
from PIL import ImageTk
import cv2
import numpy as np
import time
from Functions1 import model_prediction,crop_image
from PIL import Image, ImageTk

def check_Queen(prev,pop):
    if not(0 in prev):
        return False
    if not(5 in pop):
        return False
    return True


class Pieces(tk.Frame):
    def __init__(self, parent, images,model,classes,camera):
        tk.Frame.__init__(self, parent)
        
        self.photo = ImageTk.PhotoImage(images[0])
        self.label = tk.Label(image=self.photo)
        self.label.pack()

        self.model = model
        self.classes = classes
        self.images = images
        self.camera = camera
    def run(self):
        prev = -1
        count = 0
        images1 = self.images
        prev_pawn = [-1, -1, -1]
        curr_king = [-1, -1, -1]
        while True:
            
            
            num = model_prediction(self.model,self.classes,self.camera)
            #num = int(input())
            prev_pawn.pop(0)
            prev_pawn.append(curr_king[0])
            curr_king.pop(0)
            curr_king.append(num)
            if check_Queen(prev_pawn,curr_king):
                self.destroy()
                return 1

            if num == prev:
                count += 1
            else:
                count = 0
            prev = num
            

            if count == 4 and prev != 6:
                self.destroy()
                return prev
                break
            elif count == 4 and prev == 6:
                count = 0
                prev = -1
            if num > 6:
                num = 6
            self.photo = ImageTk.PhotoImage(images1[num])
            self.label.configure(image=self.photo)
            self.label.image = self.photo


            # Listen to the keyboard for presses.
            keyboard_input = cv2.waitKey(1)

            # 27 is the ASCII for the esc key on your keyboard.
            if keyboard_input == 27:
                break
            self.update() 
            time.sleep(0.4)
        self.destroy()