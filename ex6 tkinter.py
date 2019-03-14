from tkinter import *
import cv2
import numpy as np

def videoupload(): #파일 오픈 구현할 
    filename = askopenfilename(parent=root) 
    f = open(filename) 
    f.read()


def process():
    if RadioVariaty.get()==1:
        img =cv2.imread('input.jpg')
        
        image_gs = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

        face_list = face_cascade.detectMultiScale(image_gs, scaleFactor=1.1, minNeighbors=1, minSize=(50,50))
        if len(face_list) == 0:
            print("no face")

        color = (0, 0, 255)
        for (x,y,w,h) in face_list:
            face_img = img[y:y+h, x:x+w]
            face_img = cv2.resize(face_img, (w//10, h//10))
            face_img = cv2.resize(face_img, (w, h), interpolation=cv2.INTER_AREA)
            img[y:y+h, x:x+w] = face_img
        cv2.imwrite('output.jpg', img)
    elif RadioVariaty.get()==2:
        img =cv2.imread('Pedestrians.jpg')
        
        image_gs = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier("haarcascade_fullbody.xml")

        face_list = face_cascade.detectMultiScale(image_gs, scaleFactor=1.1, minNeighbors=1, minSize=(50,50))
        if len(face_list) == 0:
            print("no person")

        color = (0, 0, 255)
        for (x,y,w,h) in face_list:
            face_img = img[y:y+h, x:x+w]
            face_img = cv2.resize(face_img, (w//10, h//10))
            face_img = cv2.resize(face_img, (w, h), interpolation=cv2.INTER_AREA)
            img[y:y+h, x:x+w] = face_img
        cv2.imwrite('output.jpg', img)


    #elif RadioVariaty.get()==3:

    #elif RadioVariaty.get()==4:

    #elif RadioVariaty.get()==5:

    #elif RadioVariaty.get()==6:




        
window.title("seunghun chae")
window.geometry("640x400+100+100")#너비*높이, 초기 x, y좌
window.resizable(True, True)#상하, 좌우

button1 = Button(window, text="video upload", command=videoupload)
button1.pack()
entry1 = Entry(window)
entry1.insert(0,"video address")
entry1.pack()
label = Label(window, text="option")
label.pack()
RadioVariaty=IntVar()
radio1=Radiobutton(window, text="face detection - image", value=1, variable=RadioVariaty)
radio1.pack()
radio2=Radiobutton(window, text="person detection - image", value=2, variable=RadioVariaty)
radio2.pack()
radio3=Radiobutton(window, text="face detection - video", value=3, variable=RadioVariaty)
radio3.pack()
radio4=Radiobutton(window, text="person detection - video", value=4, variable=RadioVariaty)
radio4.pack()
radio5=Radiobutton(window, text="face detection - webcam", value=5, variable=RadioVariaty)
radio5.pack()
radio6=Radiobutton(window, text="person detection - webcam", value=6, variable=RadioVariaty)
radio6.pack()

button2 = Button(window, text="Convert", command=process)
button2.pack()



window.mainloop()
