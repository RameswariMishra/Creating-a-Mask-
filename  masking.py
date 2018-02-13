import Tkinter as tk
import numpy as np
from Tkinter import *
import cv2
from PIL import Image, ImageTk


class Masking():
    def __init__(self, root):
        self.root = root
        self.entry = tk.Entry(root)

        self.x = self.y = 0
        self.imgOrg = cv2.imread("/home/rameswari/Dropbox/Exampler-Inpainting/Original_Image.png", 1)
        h, w = self.imgOrg.shape[:2]
        self.imageMask = np.zeros((h, w))

        self.canvas = tk.Canvas(root, width=w, height=h, cursor="cross")
        self.canvas.grid(row=0, column=1)
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        self.start_x = None
        self.start_y = None
        self.curX = None
        self.curY = None

        self._draw_image()

        #self.startX = 20
        #self.endX = 50
        #self.startY = 20
        #self.endY = 50

        frame = Frame(self.root)
        frame.grid(row=0, column=0, sticky="n")

        self.Button1 = Button(frame, text="Creat Mask", command=self.btnClick).grid(row=3, column=1)
        self.rect = None



    def _draw_image(self):
        self.im = Image.open('Original_Image.png')
        self.tk_im = ImageTk.PhotoImage(self.im)
        self.canvas.create_image(0, 0, anchor="nw", image=self.tk_im)

    def on_button_press(self, event):
        # save mouse drag start position
        self.start_x = event.x
        self.start_y = event.y

        # create rectangle if not yet exist
        # if not self.rect:
        self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1, fill="black")

    def on_move_press(self, event):
        self.curX, self.curY = (event.x, event.y)

        # expand rectangle as you drag the mouse
        self.canvas.coords(self.rect, self.start_x, self.start_y, self.curX, self.curY)
        #self.startX = self.start_x
        #self.endX = curX
        #self.startY = self.start_y
        #self.endY = curY



    def on_button_release(self, event):
        pass

    def btnClick(self):

        for i in range(self.start_x, self.curX):
            for j in range(self.start_y, self.curY):
                self.imageMask[j,i] = 255
        cv2.imwrite("Masked_Image.png",self.imageMask)
        cv2.imshow("Masked Image", self.imageMask)
        cv2.waitKey()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    root = tk.Tk()
    gui = Masking(root)
    root.mainloop()