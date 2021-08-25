import tkinter as tk
from PIL import ImageTk
import time

x = 800

def slider():
    global x # 799
    global image1
    global image2
    x = x-1
    if x==0:
        x=800
        time.sleep(1)
        # swapping images
        temp = image1
        image1 = image2
        image2 = temp

        lbl1.config(image=image1)
        lbl2.config(image=image2)
    lbl2.place(x=x,y=0)
    lbl2.after(2,slider)

# window

root = tk.Tk()
root.title('Image Slider (Happy Engineers Day from BB)')
root.geometry('800x400+400+200')

image1 = ImageTk.PhotoImage(file='1.png')
image2 = ImageTk.PhotoImage(file='2.png')

lbl1 = tk.Label(root,image=image1,bd=0)
lbl1.place(x=0,y=0)

lbl2 = tk.Label(root,image=image2,bd=0)
lbl2.place(x=800,y=0)

root.bind("<space>",lambda event: slider())
root.mainloop()