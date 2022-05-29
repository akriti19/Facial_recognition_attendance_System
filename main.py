from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
from student import Student

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #first image
        img = Image.open(r"C:\Users\Akriti\OneDrive\Desktop\Facial Recognition Project\pictures\face_scan1.jpg")
        img=img.resize((450,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second image
        img1 = Image.open(r"C:\Users\Akriti\OneDrive\Desktop\Facial Recognition Project\pictures\face_scan.jpg")
        img1=img1.resize((450,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=450,y=0,width=500,height=130)

        #third image
        img2 = Image.open(r"C:\Users\Akriti\OneDrive\Desktop\Facial Recognition Project\pictures\face_scan2.jpg")
        img2=img2.resize((450,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=900,y=0,width=500,height=130)

    
        #bg image
        #img3 = Image.open(r"C:\Users\Akriti\OneDrive\Desktop\Facial Recognition Project\pictures\bg_image.jpg")
        #img3=img3.resize((1500,7000),Image.ANTIALIAS)
        #self.photoimg3=ImageTk.PhotoImage(img3)
        #bg_lbl=Label(self.root,image=self.photoimg3)
        #bg_lbl.place(x=1,y=6,width=1000,height=500)

        title_lbl=Label(text="FACE RECOGNITION ATTENDANCE SYSTEM" , font=("times new roman" , 35 , "bold"), bg = "white" , fg = "darkgreen")
        title_lbl.place(x=0 , y=130 , width=1300 , height=45)

        #student button
        img4 = Image.open(r"C:\Users\Akriti\OneDrive\Desktop\Facial Recognition Project\pictures\student.jpg")
        img4=img4.resize((180,100),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(image=self.photoimg4,command=self.student_details , cursor="hand2")
        b1.place(x=150,y=200 , height=150)

        #b1_1=Button(text="Student Details",command=self.student_details , cursor="hand2" , font=("times new roman" , 15 , "bold"),bg="darkblue" , fg="white")
        #b1.place(x=150,y=350 ,width=150, height=50)

        #Detect face button
        img5 = Image.open(r"C:\Users\Akriti\OneDrive\Desktop\Facial Recognition Project\pictures\face_detector.jpg")
        img5=img5.resize((180,100),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(image=self.photoimg5 , cursor="hand2")
        b1.place(x=500,y=200 , height=150)

        #b1_1=Button(text="Face Detector" , cursor="hand2" , font=("times new roman" , 15 , "bold"),bg="darkblue" , fg="white")
        #b1.place(x=500,y=350 ,width=150, height=50)

        #Attendance button
        img6 = Image.open(r"C:\Users\Akriti\OneDrive\Desktop\Facial Recognition Project\pictures\attendance.jpg")
        img6=img6.resize((180,100),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(image=self.photoimg6 , cursor="hand2")
        b1.place(x=800,y=200 , height=150)

        #b1_1=Button(text="Attendance" , cursor="hand2" , font=("times new roman" , 15 , "bold"),bg="darkblue" , fg="white")
        #b1.place(x=800,y=350 ,width=150, height=50)

        #help desk button
        img7 = Image.open(r"C:\Users\Akriti\OneDrive\Desktop\Facial Recognition Project\pictures\help_desk.png")
        img7=img7.resize((180,100),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(image=self.photoimg7 , cursor="hand2")
        b1.place(x=1100,y=200 , height=150)

        #b1_1=Button(text="Help Desk" , cursor="hand2" , font=("times new roman" , 15 , "bold"),bg="darkblue" , fg="white")
        #b1.place(x=1100,y=350 ,width=150, height=50)

        #train button
        img8 = Image.open(r"C:\Users\Akriti\OneDrive\Desktop\Facial Recognition Project\pictures\train_model.jpg")
        img8=img8.resize((180,100),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(image=self.photoimg8 , cursor="hand2")
        b1.place(x=150,y=400 , height=150)

        #b1_1=Button(text="Training" , cursor="hand2" , font=("times new roman" , 15 , "bold"),bg="darkblue" , fg="white")
        #b1.place(x=150,y=550 ,width=150, height=50)

        #photos button
        img9 = Image.open(r"C:\Users\Akriti\OneDrive\Desktop\Facial Recognition Project\pictures\photos.jpg")
        img9=img9.resize((180,100),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(image=self.photoimg9 , cursor="hand2")
        b1.place(x=500,y=400 , height=150)

        #b1_1=Button(text="Photos Set" , cursor="hand2" , font=("times new roman" , 15 , "bold"),bg="darkblue" , fg="white")
        #b1.place(x=500,y=350 ,width=150, height=50)

        #Developer button
        img10 = Image.open(r"C:\Users\Akriti\OneDrive\Desktop\Facial Recognition Project\pictures\Developer.jpg")
        img10=img10.resize((180,100),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(image=self.photoimg10 , cursor="hand2")
        b1.place(x=800,y=400 , height=150)

        #b1_1=Button(text="Developer" , cursor="hand2" , font=("times new roman" , 15 , "bold"),bg="darkblue" , fg="white")
        #b1.place(x=800,y=350 ,width=150, height=50)

        #Exit button
        img11 = Image.open(r"C:\Users\Akriti\OneDrive\Desktop\Facial Recognition Project\pictures\exit.jpg")
        img11=img11.resize((180,100),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(image=self.photoimg11 , cursor="hand2")
        b1.place(x=1100,y=400 , height=150)

        #b1_1=Button(text="Exit" , cursor="hand2" , font=("times new roman" , 15 , "bold"),bg="darkblue" , fg="white")
        #b1.place(x=1100,y=350 ,width=150, height=50)


        def student_details(self):
            self.new_window=Toplevel(self.root)
            self.app=Student(self.new_window)

       

        

if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
