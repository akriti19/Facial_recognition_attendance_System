
from tkinter import *;

         # ==================================Buttons Frame========================================
         btnFrame = Frame(student_frame, relief=RIDGE, bg="cyan")
         btnFrame.place(x=0, y=180, width=640, height=40)

         save_btn = Button(btnFrame, text="Save", command=self.add_data, width=13, font=('arial', 13, 'bold'), bg="red", fg="white")
         save_btn.grid(row=0, column=0)

         update_btn = Button(btnFrame, text="Update", width=13, font=('arial', 13, 'bold'), bg="red", fg="white")
         update_btn.grid(row=0, column=1)

         delete_btn = Button(btnFrame, text="Delete", width=13, font=('arial', 13, 'bold'), bg="red", fg="white")
         delete_btn.grid(row=0, column=2)

         reset_btn = Button(btnFrame, text="Reset", width=14, font=('arial', 13, 'bold'), bg="red", fg="white")
         reset_btn.grid(row=0, column=3)

         # ==================================Buttons Frame1========================================
         btnFrame1 = Frame(student_frame, relief=RIDGE, bg="cyan")
         btnFrame1.place(x=0, y=220, width=640, height=40)

         capture_photo_btn = Button(btnFrame1, text="Capture Photo Sample", width=29, font=('arial', 13, 'bold'), bg="red", fg="white")
         capture_photo_btn.grid(row=1, column=0)

         update_photo_btn = Button(btnFrame1, text="Update Photo Sample", width=30, font=('arial', 13, 'bold'), bg="red", fg="white")
         update_photo_btn.grid(row=1, column=1)

         # right label frame
         Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=("Calibri", 12, "bold"))
         Right_frame.place(x=670, y=10, width=650, height=500)

         img_right = Image.open("Images/scholarImages/high-school-grad.jpg")
         img_right = img_right.resize((650, 80), Image.ANTIALIAS)
         self.photoimg_right = ImageTk.PhotoImage(img_right)

         f_lbl = Label(Right_frame, image=self.photoimg_right)
         f_lbl.place(x=5, y=0, width=640, height=60)

         # ==================================Search Systems========================================
         search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",
                                           font=("Calibri", 12, "bold"), fg="green")
         search_frame.place(x=5, y=60, width=640, height=60)

         search_label = Label(search_frame, text=" Search By: ", font=("Calibri", 10, "bold"), bg="blue",
                             fg="white")
         search_label.grid(row=0, column=0, padx=10, sticky=W)

         search_combo = ttk.Combobox(search_frame, font=("Calibri", 10, "bold"), state="readonly", width=12)
         search_combo["values"] = ("Select", "Roll_no", "Contact_no", "StdID")
         search_combo.current(0)
         search_combo.grid(row=0, column=1, padx=10, pady=5, sticky=W)

         search_entry = ttk.Entry(search_frame, width=20, font=("Calibri", 10, "bold"))
         search_entry.grid(row=0, column=2, padx=10, sticky=W)

         search_btn = Button(search_frame, text="Search", width=10, font=('arial', 10, 'bold'), bg="red", fg="white")
         search_btn.grid(row=0, column=3, padx=1)

         showAll_btn = Button(search_frame, text="Show All", width=10, font=('arial', 10, 'bold'), bg="red", fg="white")
         showAll_btn.grid(row=0, column=4, padx=1)

         # ==================================Table Frame==========================================
         table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
         table_frame.place(x=5, y=120, width=640, height=330)

         scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
         scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

         self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "section",
                                                                "roll", "gender", "phone", "address", "photo"),
                                           xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

         scroll_x.pack(side=BOTTOM, fill=X)
         scroll_y.pack(side=RIGHT, fill=Y)
         scroll_x.config(command=self.student_table.xview)
         scroll_y.config(command=self.student_table.yview)

         self.student_table.heading("dep", text="Department")
         self.student_table.heading("course", text="Course")
         self.student_table.heading("year", text="Year")
         self.student_table.heading("sem", text="Semester")
         self.student_table.heading("id", text="StudentID")
         self.student_table.heading("name", text="Name")
         self.student_table.heading("section", text="Section")
         self.student_table.heading("roll", text="RollNo")
         self.student_table.heading("gender", text="Gender")
         self.student_table.heading("phone", text="Phone")
         self.student_table.heading("address", text="Address")
         self.student_table.heading("photo", text="PhotoSampleStatus")
         self.student_table["show"] = "headings"

         self.student_table.column("dep", width=100)
         self.student_table.column("course", width=100)
         self.student_table.column("year", width=100)
         self.student_table.column("sem", width=100)
         self.student_table.column("id", width=100)
         self.student_table.column("name", width=100)
         self.student_table.column("section", width=100)
         self.student_table.column("roll", width=100)
         self.student_table.column("gender", width=100)
         self.student_table.column("phone", width=100)
         self.student_table.column("address", width=100)
         self.student_table.column("photo", width=200)

         self.student_table.pack(fill=BOTH, expand=1)

     # ==================================Functions Declaration========================================
     # validations
     def add_data(self):
         if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
             messagebox.showerror("Error", "All Fields are mandatory", parent=self.root)
             # here, parent=self.root shows the message explicitly in that window
         else:
             # pass
             # messagebox.showinfo("Success", "Data Saved Successfully")
             try:
                 conn = mysql.connector.connect(host="localhost",
                                                username="root",
                                                password="Test@123",
                                                database="face_recognizer")
                 my_cursor = conn.cursor()
                 my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                   (
                                       self.var_dep.get(),
                                       self.var_course.get(),
                                       self.var_year.get(),
                                       self.var_semester.get(),
                                       self.var_std_id.get(),
                                       self.var_std_name.get(),
                                       self.var_sec.get(),
                                       self.var_roll.get(),
                                       self.var_gender.get(),
                                       self.var_phone.get(),
                                       self.var_address.get(),
                                       self.var_radio1.get()
                                   ))
                 conn.commit()
                 conn.close()
                 messagebox.showinfo("Done", "Student details have been added successfully", parent=self.root)

             except Exception as es:
                 messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)


 if __name__ == "__main__":
     root = Tk()
     obj = Student(root)
     root.mainloop()