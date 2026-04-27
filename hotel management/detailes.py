from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
from time import strftime
import mysql.connector
from tkinter import messagebox



class DetailsRoom:

    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        # ==================== Title ====================
        lbl_title = Label(
            self.root,
            text="ADD CUSTOMER DETAILS",
            font=("Times New Roman", 40, "bold"),
            bg="black",
            fg="gold",
            bd=4,
            relief=RIDGE
        )
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # ==================== Logo ====================
        img2 = Image.open(r"C:\Users\Mohit\Desktop\hotel management\photo2.jpg")
        img2 = img2.resize((100, 40), Image.Resampling.LANCZOS)

        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2)
        lblimg2.place(x=5, y=2, width=100, height=40)

        # ==================== Room Details Frame ====================
        labelframeleft = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            text="New Room Add",
            font=("Times New Roman", 12, "bold"),
            padx=2
        )
        labelframeleft.place(x=5, y=50, width=540, height=350)

        # ==================== Floor ====================
        Label(labelframeleft, text="Floor",
              font=("Times New Roman", 12, "bold")).grid(row=0, column=0, sticky=W)
        self.var_floor=StringVar()
        ttk.Entry(labelframeleft,textvariable=self.var_floor,
                  font=("arial", 13, "bold"), width=20).grid(row=0, column=1, sticky=W)

        # ==================== Room No ====================
        Label(labelframeleft, text="Room No.",
              font=("Times New Roman", 12, "bold")).grid(row=1, column=0, sticky=W)
        self.var_roomNo = StringVar()
        ttk.Entry(labelframeleft,textvariable=self.var_roomNo,
                  font=("arial", 13, "bold"), width=20).grid(row=1, column=1, sticky=W)

        # ==================== Room Type ====================
        Label(labelframeleft, text="Room Type",
              font=("Times New Roman", 12, "bold")).grid(row=2, column=0, sticky=W)
        self.var_roomtype=StringVar()
        ttk.Entry(labelframeleft, textvariable=self.var_roomtype,
                  font=("arial", 13, "bold"), width=20).grid(row=2, column=1, sticky=W)

        # ================= BUTTON FRAME =================
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=410, height=55)

        Button(btn_frame, text="Add",command=self.add_data, bg="black", fg="gold").grid(row=0, column=0, sticky="ew")
        Button(btn_frame, text="Update", bg="black", fg="gold").grid(row=0, column=1, sticky="ew")
        Button(btn_frame, text="Delete", bg="black", fg="gold").grid(row=0, column=2, sticky="ew")
        Button(btn_frame, text="Reset", bg="black", fg="gold").grid(row=0, column=3, sticky="ew")

        btn_frame.columnconfigure((0, 1, 2, 3), weight=1)

        # ==================== Table Frame ====================
        Table_frame = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            text="Show Room Detail",
            font=("arial", 12, "bold"),
            padx=2
        )
        Table_frame.place(x=600, y=55, width=600, height=350)

        # ================= Scrollbars =================
        scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        # ================= Treeview =================
        self.table = ttk.Treeview(
            Table_frame,
            columns=("floor", "roomno", "roomtype"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.table.xview)
        scroll_y.config(command=self.table.yview)

        # headings
        self.table.heading("floor", text="Floor")
        self.table.heading("roomno", text="Room No")
        self.table.heading("roomtype", text="Room Type")

        # column size
        self.table.column("floor", width=100)
        self.table.column("roomno", width=100)
        self.table.column("roomtype", width=150)

        self.table["show"] = "headings"

        self.table.pack(fill=BOTH, expand=1)

    
    def add_data(self):
        if self.var_floor.get()==""or self.var_roomtype.get()=="":
         messagebox.showerror("ERROR","All fields are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="mohit@12345",database="mohitdb")
                my_cursor=conn.cursor()
                my_cursor.execute("INSERT INTO customer VALUES(%s,%s,%s)",(
                                                        self.var_floor.get(),
                                                        self.var_roomNo.get(),
                                                        self.var_roomtype.get(),
 
                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","new room added successfully ", parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning", f"some thing went wrong:{str(es)}", parent=self.root)


# ==================== MAIN ====================
if __name__ == "__main__":
    root = Tk()
    obj = DetailsRoom(root)
    root.mainloop()
