from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector


class RoomBooking:

    def __init__(self, root):
        self.root = root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1295x550+230+220")

        # ================= TITLE =================
        lbl_title = Label(
            self.root,
            text=" ROOM BOOKING DETAILS ",
            font=("Times New Roman", 40, "bold"),
            bg="black",
            fg="gold",
            bd=4,
            relief=RIDGE
        )
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # ================= LOGO =================
        # keep photo2.jpg in same folder as this .py file
        img2 = Image.open("photo2.jpg")
        img2 = img2.resize((100, 40), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        Label(self.root, image=self.photoimg2).place(x=5, y=2, width=100, height=40)

        # =========================================================
        # ================= LEFT FORM =============================
        # =========================================================
        left = LabelFrame(
            self.root,
            text="Roombooking Details",
            font=("Times New Roman", 12, "bold"),
            bd=2,
            relief=RIDGE
        )
        left.place(x=5, y=50, width=425, height=490)

        labels = [
            "Customer Contact",
            "Check_in Date",
            "Check_Out Date",
            "Room Type",
            "Available Room",
            "Meal",
            "No Of Days",
            "Paid Tax",
            "Sub Total",
            "Total Cost"
        ]

        self.vars = {}

        for i, txt in enumerate(labels):
            Label(left, text=txt, font=("arial", 11, "bold")).grid(
                row=i, column=0, padx=5, pady=6, sticky=W
            )

            if txt == "Room Type":
                box = ttk.Combobox(left, state="readonly", width=18)
                box["values"] = ("Single", "Double", "Luxury")
                box.current(0)
                box.grid(row=i, column=1)
                self.vars[txt] = box
            else:
                var = StringVar()
                self.vars[txt] = var
                ttk.Entry(left, textvariable=var, width=20).grid(row=i, column=1)

        Button(left, text="Fetch Data", command=self.fetch_data,
               bg="black", fg="gold").place(x=320, y=5)

        Button(left, text="Bill", bg="black", fg="gold").place(x=10, y=360)

        # ================= BUTTON FRAME =================
        btn_frame = Frame(left, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=410, height=55)

        Button(btn_frame, text="Add", command=self.add_data,
               bg="black", fg="gold").grid(row=0, column=0, sticky="ew")

        Button(btn_frame, text="Update", command=self.update_data,
               bg="black", fg="gold").grid(row=0, column=1, sticky="ew")

        Button(btn_frame, text="Delete", command=self.delete_data,
               bg="black", fg="gold").grid(row=0, column=2, sticky="ew")

        Button(btn_frame, text="Reset", command=self.reset_data,
               bg="black", fg="gold").grid(row=0, column=3, sticky="ew")

        btn_frame.columnconfigure((0, 1, 2, 3), weight=1)

        # =========================================================
        # ================= RIGHT SECTION ==========================
        # =========================================================
        right = LabelFrame(
            self.root,
            text="View Details And Search System",
            font=("Times New Roman", 12, "bold"),
            bd=2,
            relief=RIDGE
        )
        right.place(x=435, y=50, width=860, height=490)

        # Image
        img3 = Image.open("imag.jpg")
        img3 = img3.resize((840, 180), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        Label(right, image=self.photoimg3).place(x=5, y=0, width=840, height=180)

        # Search
        Label(right, text="Search By:", bg="red", fg="white").place(x=10, y=190)

        self.search_var = StringVar()
        combo = ttk.Combobox(right, textvariable=self.search_var,
                             state="readonly", width=15)
        combo["values"] = ("Mobile", "Ref")
        combo.current(0)
        combo.place(x=110, y=190)

        self.txt_search = StringVar()
        ttk.Entry(right, textvariable=self.txt_search, width=25).place(x=250, y=190)

        Button(right, text="Search", command=self.search,
               bg="black", fg="gold").place(x=450, y=187)

        Button(right, text="Show All", command=self.fetch_data,
               bg="black", fg="gold").place(x=560, y=187)

        # ================= TABLE =================
        table_frame = Frame(right, bd=2, relief=RIDGE)
        table_frame.place(x=5, y=230, width=840, height=230)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.table = ttk.Treeview(
            table_frame,
            columns=("contact", "checkin", "checkout",
                     "roomtype", "roomno", "meal", "days"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.table.xview)
        scroll_y.config(command=self.table.yview)

        self.table["show"] = "headings"

        for col in self.table["columns"]:
            self.table.heading(col, text=col.title())
            self.table.column(col, width=110)

        self.table.pack(fill=BOTH, expand=1)

        self.fetch_data()

    # =========================================================
    # DATABASE
    # =========================================================
    def db(self):
        return mysql.connector.connect(
            host="localhost",
            username="root",
            password="mohit@12345",
            database="project1"
        )

    # =========================================================
    # FUNCTIONS
    # =========================================================

    def fetch_data(self):
        conn = self.db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM room")
        rows = cur.fetchall()

        self.table.delete(*self.table.get_children())
        for row in rows:
            self.table.insert("", END, values=row)

        conn.close()

    def search(self):
        val = self.txt_search.get()

        if not val:
            messagebox.showerror("Error", "Enter search value")
            return

        conn = self.db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM room WHERE contact LIKE %s", ('%' + val + '%',))
        rows = cur.fetchall()

        self.table.delete(*self.table.get_children())
        for row in rows:
            self.table.insert("", END, values=row)

        conn.close()

    def add_data(self):
        messagebox.showinfo("Add", "Add button clicked")

    def update_data(self):
        messagebox.showinfo("Update", "Update button clicked")

    def delete_data(self):
        messagebox.showinfo("Delete", "Delete button clicked")

    def reset_data(self):
        for key in self.vars:
            if isinstance(self.vars[key], StringVar):
                self.vars[key].set("")


# =========================================================
if __name__ == "__main__":
    root = Tk()
    obj = RoomBooking(root)
    root.mainloop()
