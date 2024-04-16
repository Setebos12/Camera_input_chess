import cv2
import numpy as np
import tkinter as tk
import time
from PIL import Image, ImageTk
from Functions1 import model_prediction

def change_to_ord(l):
    ans = []
    for x1 in l:
        ans.append([chr(ord('a') + x1[0]), chr(ord('a') + x1[1])])
    return ans

def change_colors(limes):
    color_dict = {'a': 'h', 'b': 'g', 'c': 'f', 'd': 'e','e':'d' ,'f':'c','g':'b','h':'a','i':chr(ord('a') - 1)}
    result = []
    for sublist in limes:
        modified_sublist = [color_dict[item] for item in sublist]
        result.append(modified_sublist)
    return result

class Chessboard1(tk.Frame):
    def __init__(self, parent,model,classes, highlight_side="None",selected_squares=["a2","b2","c3"],camera=None,color=0):
        tk.Frame.__init__(self, parent)
        self.highlight_side = highlight_side
        self.selected_squares = selected_squares
        self.cord = [0, 8, 0, 8]
        self.model = model[1]
        self.classes = classes[1]
        self.color = color
        self.create_chessboard_frame()
        self.camera = camera

        self.model1 = model[0]
        self.classes1 = classes[0]
        
    
    def create_chessboard_frame(self):
        self.chessboard_frame = tk.Frame(self)
        self.chessboard_frame.pack()
        colors = ["white", "gray"]
        rows = "87654321"          
        columns = "abcdefgh"
        if self.color == 0:
          rows = "12345678"
          columns = "hgfedcba"
        count = 0
        square = "A1"
        xx = min(abs(8-self.cord[2]),abs(8-self.cord[3]))
        yy = max(abs(8-self.cord[2]),abs(8-self.cord[3]))
        if self.color == 0:
          xx = self.cord[2]
          yy = self.cord[3]
        for row in range(xx, yy):
            for col in range(self.cord[0], self.cord[1]):
                square_color = colors[(row + col) % 2]
                if self.color == 0:
                    square_color = colors[(row + col) % 2]
                square_name = columns[col] + rows[row]
                if square_name in self.selected_squares:
                    label = tk.Label(self.chessboard_frame, text=square_name, bg=square_color)
                    
                    square = square_name
                    count+=1 
                else:
                    label = tk.Label(self.chessboard_frame, bg=square_color)
                label.grid(row=row, column=col)
                label.square_name = square_name
                label.config(font=("Arial",64))
                label.config(width=2,height=1,padx=0,pady=0)
        return count, square

    def highlight_squares(self, decision):
        limes = self.divide_range(self.cord[0], self.cord[1])
        limes = change_to_ord(limes)
        colors_h = ["#79ad87","#b07168","#799eb5"]
        for widget in self.chessboard_frame.winfo_children():
            if isinstance(widget, tk.Label) and widget.cget("text") in self.selected_squares and hasattr(widget, "square_name"):
                if decision != "None":
                    colors = ["white", "gray"]
                    row = ord(widget.square_name[0])-97
                    column = int(widget.square_name[1])-1
                    square_color = colors[(row + column+1) % 2]
                    col = square_color
                    if self.color == 1:
                      if limes[0][0] <= widget.square_name[0] < limes[0][1]:
                          widget.config(bg=colors_h[2] if decision == "left" else col)
                      elif limes[1][0] <= widget.square_name[0] < limes[1][1]:
                          widget.config(bg=colors_h[1] if decision == "middle" else col)
                      elif limes[2][0] <= widget.square_name[0] <= limes[2][1]:
                          widget.config(bg=colors_h[0] if decision == "right" else col)
                    else:
                      limes1 = change_colors(limes)
                      
                      if limes1[0][0] >= widget.square_name[0] > limes1[0][1]:
                          widget.config(bg=colors_h[2] if decision == "left" else col)
                      elif limes1[1][0] >= widget.square_name[0] > limes1[1][1]:
                          widget.config(bg=colors_h[1] if decision == "middle" else col)
                      elif limes1[2][0] >= widget.square_name[0] > limes1[2][1]:
                          widget.config(bg=colors_h[0] if decision == "right" else col)

    def highlight_squares1(self, decision):
        limes = self.divide_range(self.cord[2], self.cord[3])
        colors_h = ["#79ad87","#b07168","#799eb5"]
        for widget in self.chessboard_frame.winfo_children():
            if isinstance(widget, tk.Label) and widget.cget("text") in self.selected_squares and hasattr(widget, "square_name"):
                if decision != "None":
                    colors = ["white", "gray"]
                    row = ord(widget.square_name[0])-97
                    column = int(widget.square_name[1])-1
                    square_color = colors[(row + column+1) % 2]
                    col = square_color
                    if self.color == 1:
                      if limes[0][0] <= int(widget.square_name[1])-1 < limes[0][1]:
                          widget.config(bg=colors_h[2] if decision == "left" else col)
                      elif limes[1][0] <= int(widget.square_name[1])-1 < limes[1][1]:
                          widget.config(bg=colors_h[1] if decision == "middle" else col)
                      elif limes[2][0] <= int(widget.square_name[1])-1 <= limes[2][1]:
                          widget.config(bg=colors_h[0] if decision == "right" else col)
                    else:
                      if limes[0][0] <= int(widget.square_name[1])-1 < limes[0][1]:
                          widget.config(bg=colors_h[0] if decision == "right" else col)
                      elif limes[1][0] <= int(widget.square_name[1])-1 < limes[1][1]:
                          widget.config(bg=colors_h[1] if decision == "middle" else col)
                      elif limes[2][0] <= int(widget.square_name[1])-1 <= limes[2][1]:
                          widget.config(bg=colors_h[2] if decision == "left" else col)

    def divide_range(self, x1, x2):
        limes = []
        interval_size = x2 - x1
        increment = interval_size // 3
        if interval_size % 3 == 0:
            limes.append([x1, x1 + increment])
            limes.append([x1 + increment, x1 + 2 * increment])
            limes.append([x1 + 2 * increment, x2])
        elif interval_size % 3 == 1:
            increment += 1
            limes.append([x1, x1 + increment])
            limes.append([x1 + increment, x1 + 2 * increment - 1])
            limes.append([x1 + 2 * increment - 1, x2])
        else:
            increment += 1
            limes.append([x1, x1 + increment])
            limes.append([x1 + increment, x1 + 2 * increment - 1])
            limes.append([x1 + 2 * increment - 1, x2])
        
        return limes

    def define_square(self):
        des = ['left', 'middle', 'right', 'left', 'middle', 'right']
        count = 0
        prev = -1
        while True:
            count = 0
            prev = -1

            self.chessboard_frame.destroy()
            counter_check, square_to_go = self.create_chessboard_frame()
            self.update()
            
            if counter_check <= 1:
                print(square_to_go)
                self.destroy()
                return square_to_go
                break

            while count < 2:
                #decision = int(input())
                #decision1 = 0
                decision=model_prediction(self.model,self.classes,self.camera)
                decision1=model_prediction(self.model1,self.classes1,self.camera)

                if decision1 == 3:
                    decision = 5



                if decision == prev:
                    count += 1
                else:
                    if decision < 3:
                        self.highlight_squares1("None")
                        self.highlight_squares(des[decision])
                    elif decision < 6:
                        self.highlight_squares("None")
                        self.highlight_squares1(des[decision])
                    else:
                        self.highlight_squares1("None")
                        self.highlight_squares("None")
                    count = 0
                prev = decision
                self.update()
                time.sleep(0.4)
            
            if prev < 3:
                limes = self.divide_range(self.cord[0], self.cord[1])
                self.cord[0] = limes[prev][0]
                self.cord[1] = limes[prev][1]
                print(self.cord[2], ": " , self.cord[1])
            elif prev < 6:
                limes = self.divide_range(self.cord[2], self.cord[3])
                if self.color == 0:
                  if prev == 3:
                      prev = 5
                  elif prev == 5:
                      prev = 3
                prev %= 3
                #if prev == 0:
                #    prev = 2
               # elif prev == 2:
                #    prev = 0
                print(limes[prev])
                self.cord[2] = limes[prev][0]
                self.cord[3] = limes[prev][1]
            
