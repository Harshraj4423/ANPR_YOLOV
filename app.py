import tkinter as tk  
import customtkinter as ck
import torch
import cv2
import time
from PIL import Image , ImageTk
from detection2 import main
from tkinter import filedialog

window = tk.Tk()

window.title("ANPR")
window.maxsize(1000, 750)
bg = ImageTk.PhotoImage(file = "bg41.jpg")
label1 = tk.Label(window , image= bg)
label1.place(x=0 , y=0)

str = "D:/ANPR_YOLOV/yolov7/work/3.jpg"
ck.set_appearance_mode("dark")




def open_win_diag():
   # Create a dialog boxs
   file=filedialog.askopenfilename(initialdir="D:\ANPR_YOLOV\yolov7\3.jpg")
   display_img(file)

def display_img(str):
   
   #Right Image 
   image  = main(str)
   #image = cv2.imread(str)
   imgarr = Image.fromarray(image)
   imgtk = ImageTk.PhotoImage(imgarr)
   tk.Label(right_frame, image=imgtk).grid(row=0,column=0, padx=0, pady=0)
   right_frame.config(image = imgtk)

def real_time():
   main(vid_path=0,vid_out="webcam_facemask_result.mp4")

#Left Frame init
left_frame = tk.Frame(window, width=200, height=250, bg='skyblue')
left_frame.grid(row=0, column=0, padx=30, pady=0)



top_frame = tk.Frame(left_frame, width=200, height=210, bg='skyblue')
top_frame.grid(row=0, column=0, padx=0, pady = 0)
bot_frame = tk.Frame(left_frame, width=200, height=70, bg='skyblue')
bot_frame.grid(row=1, column=0, padx=0, pady=0)


#Right Frame init 
right_frame = tk.Frame(window, width=800, height=400, bg='skyblue')
right_frame.grid(row=0, column=1, padx=60, pady=35)
   

#Right Image 
image = main(str)
imgarr = Image.fromarray(image)
imgtk = ImageTk.PhotoImage(imgarr)


#For left frame 
logo = Image.open("work/beluga.jpg")
logo = logo.resize((200,200))
imgtk_left = ImageTk.PhotoImage(logo)



#display image 
tk.Label(right_frame, image=imgtk).grid(row=0,column=0, padx=0, pady=0)
tk.Label(top_frame, image=imgtk_left).grid(row=1, column=0, padx=0, pady=0)


#buttons
button1 = tk.Button(bot_frame, text = 'open', fg ='red', font = 'TimesNewRoman',activebackground='red',relief='raised',command=open_win_diag)
button1.place(x=35,y=15)
button2 = tk.Button(bot_frame, text = 'realtime', fg ='blue', font = 'TimesNewRoman',activebackground='blue',relief='raised', command=real_time)
button2.place(x=105,y=15)

window.mainloop()