from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
import mysql.connector
from tkinter import messagebox

 

class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1295x550+230+220")

        #============================= variables ===============================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()


        # ==================== Title ====================
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS",
                          font=("Times New Roman", 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # ==================== Logo ====================
        img2 = Image.open(r"C:\Users\Mohit\Desktop\hotel management\photo2.jpg")
        img2 = img2.resize((100, 40), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2)
        lblimg2.place(x=5, y=2, width=100, height=40)

        # ==================== Customer Details Frame ====================
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details",
                                    font=("Times New Roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # ==================== Labels and Entry Fields ====================
        lbl_cust_ref = Label(labelframeleft, text="Customer Ref", font=("Times New Roman", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)
        enty_ref = ttk.Entry(labelframeleft, textvariable=self.var_ref,width=29, font=("Times New Roman", 13, "bold"),state="readonly")
        enty_ref.grid(row=0, column=1)

        cname = Label(labelframeleft, text="Customer Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)
        txtcname = ttk.Entry(labelframeleft, textvariable=self.var_cust_name,font=("arial", 13, "bold"), width=29)
        txtcname.grid(row=1, column=1)

        lblmname = Label(labelframeleft, text="Mother Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblmname.grid(row=2, column=0, sticky=W)
        txtmname = ttk.Entry(labelframeleft, textvariable=self.var_mother,font=("arial", 13, "bold"), width=29)
        txtmname.grid(row=2, column=1)

        label_gender = Label(labelframeleft, text="Gender:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_gender.grid(row=3, column=0, sticky=W)
        combo_gender = ttk.Combobox(labelframeleft,textvariable=self.var_gender, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_gender["value"] = ("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        lblPostCode = Label(labelframeleft, text="PostCode:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPostCode.grid(row=4, column=0, sticky=W)
        txtPostCode = ttk.Entry(labelframeleft, textvariable=self.var_post,font=("arial", 13, "bold"), width=29)
        txtPostCode.grid(row=4, column=1)

        lblMobile = Label(labelframeleft, text="Mobile:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMobile.grid(row=5, column=0, sticky=W)
        txtMobile = ttk.Entry(labelframeleft,textvariable=self.var_mobile, font=("arial", 13, "bold"), width=29)
        txtMobile.grid(row=5, column=1)

        lblEmail = Label(labelframeleft, text="Email:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblEmail.grid(row=6, column=0, sticky=W)
        txtEmail = ttk.Entry(labelframeleft,textvariable=self.var_email, font=("arial", 13, "bold"), width=29)
        txtEmail.grid(row=6, column=1)

        lblNationality = Label(labelframeleft, text="Nationality:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNationality.grid(row=7, column=0, sticky=W)
        combo_Nationality = ttk.Combobox(labelframeleft,textvariable=self.var_nationality, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_Nationality["value"] = ("Indian", "American", "British")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7, column=1)

        lblIDProof = Label(labelframeleft, text="ID Proof Type:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblIDProof.grid(row=8, column=0, sticky=W)
        combo_ID = ttk.Combobox(labelframeleft,textvariable=self.var_id_proof, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_ID["value"] = ("Aadhar Card", "Driving License", "Passport")
        combo_ID.current(0)
        combo_ID.grid(row=8, column=1)

        lblIDNumber = Label(labelframeleft, text="ID Number:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblIDNumber.grid(row=9, column=0, sticky=W)
        txtlblIDNumber = ttk.Entry(labelframeleft,textvariable=self.var_id_number, font=("arial", 13, "bold"), width=29)
        txtlblIDNumber.grid(row=9, column=1)

        lblAddress = Label(labelframeleft, text="Address:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblAddress.grid(row=10, column=0, sticky=W)
        txtlblAddress = ttk.Entry(labelframeleft,textvariable=self.var_address, font=("arial", 13, "bold"), width=29)
        txtlblAddress.grid(row=10, column=1)

        # ==================== Button Frame ====================
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add",command=self.add_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btnupdate = Button(btn_frame, text="Update",command=self.update, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnupdate.grid(row=0, column=1, padx=1)

        btndelete = Button(btn_frame, text="Delete",command=self.delete_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btndelete.grid(row=0, column=2, padx=1)

        btnreset = Button(btn_frame, text="Reset",command=self.reset, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnreset.grid(row=0, column=3, padx=1)

        # ==================== Table Frame ====================
        Table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System",
                                 font=("Times New Roman", 12, "bold"), padx=2)
        Table_frame.place(x=435, y=50, width=860, height=490)

        lblsearchby = Label(Table_frame, text="Search By:", font=("arial", 12, "bold"), bg="red", fg="white")
        lblsearchby.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var=StringVar()

        combo_search = ttk.Combobox(Table_frame,textvariable=self.search_var, font=("arial", 12, "bold"), width=24, state="readonly")
        combo_search["value"] = ("Mobile", "Ref")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_search=StringVar()

        txtsearch = ttk.Entry(Table_frame,textvariable=self.txt_search, font=("arial", 13, "bold"), width=24)
        txtsearch.grid(row=0, column=2, padx=2)

        btnsearch = Button(Table_frame, text="Search",command=self.search, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnsearch.grid(row=0, column=3, padx=1)

        btnshowall = Button(Table_frame, text="Show All",command=self.fetch_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnshowall.grid(row=0, column=4, padx=1)

        # ==================== Data Table ====================
        details_Table = Frame(Table_frame, bd=2, relief=RIDGE)
        details_Table.place(x=0, y=50, width=860, height=350)

        Scroll_x = ttk.Scrollbar(details_Table, orient=HORIZONTAL)
        Scroll_y = ttk.Scrollbar(details_Table, orient=VERTICAL)

        self.Cust_details_Table = ttk.Treeview(details_Table, columns=("ref", "name", "mother", "gender", "post",
                                                                       "email", "nationality", "idproof", "idnumber", "address"),
                                               xscrollcommand=Scroll_x.set,
                                               yscrollcommand=Scroll_y.set)

        Scroll_x.pack(side=BOTTOM, fill=X)
        Scroll_y.pack(side=RIGHT, fill=Y)

        Scroll_x.config(command=self.Cust_details_Table.xview)
        Scroll_y.config(command=self.Cust_details_Table.yview)

        self.Cust_details_Table.heading("ref", text="Ref")
        self.Cust_details_Table.heading("name", text="Name")
        self.Cust_details_Table.heading("mother", text="Mother Name")
        self.Cust_details_Table.heading("gender", text="Gender")
        self.Cust_details_Table.heading("post", text="PostCode")
        #self.Cust_details_Table.heading("number",text="number")
        self.Cust_details_Table.heading("email", text="Email")
        self.Cust_details_Table.heading("nationality", text="Nationality")
        self.Cust_details_Table.heading("idproof", text="ID Proof")
        self.Cust_details_Table.heading("idnumber", text="ID Number")
        self.Cust_details_Table.heading("address", text="Address")

        self.Cust_details_Table["show"] = "headings"

        for col in ("ref", "name", "mother", "gender", "post", "email", "nationality", "idproof", "idnumber", "address"):
            self.Cust_details_Table.column(col, width=100)

        self.Cust_details_Table.pack(fill=BOTH, expand=1)
        self.Cust_details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get()==""or self.var_mother.get()=="":
         messagebox.showerror("ERROR","All fields are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="mohit@12345",database="mohitdb")
                my_cursor=conn.cursor()
                my_cursor.execute("INSERT INTO customer VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                        self.var_ref.get(),
                                                        self.var_cust_name.get(),
                                                        self.var_mother.get(),
                                                        self.var_gender.get(),
                                                        self.var_post.get(),
                                                        self.var_mobile.get(),
                                                        self.var_email.get(),
                                                        self.var_nationality.get(),
                                                        self.var_id_proof.get(),
                                                        self.var_id_number.get(),
                                                        self.var_address.get()
                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success"," customer has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning", f"some thing went wrong:{str(es)}", parent=self.root)
    def fetch_data(self):
        conn = mysql.connector.connect(
        host="localhost",
        username="root",
        password="mohit@12345",
        database="mohitdb"
    )
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM customer")
        rows = my_cursor.fetchall()

       # clear old data safely
        self.Cust_details_Table.delete(*self.Cust_details_Table.get_children())

        for i in rows:
         self.Cust_details_Table.insert("", END, values=i)

        conn.close()

    def get_cursor(self, event=""):
      cursor_row = self.Cust_details_Table.focus()
      content = self.Cust_details_Table.item(cursor_row)
      row = content["values"]

      # ⭐ SAFETY CHECK
      if len(row) == 0:
        return

      self.var_ref.set(row[0])
      self.var_cust_name.set(row[1])
      self.var_mother.set(row[2])
      self.var_gender.set(row[3])
      self.var_post.set(row[4])
      self.var_mobile.set(row[5])
      self.var_email.set(row[6])
      self.var_nationality.set(row[7])
      self.var_id_proof.set(row[8])
      self.var_id_number.set(row[9])
      self.var_address.set(row[10])
  

    def update(self):
        if self.var_mobile.get()=="":
           messagebox.showerror("Error","please enter mobile number",parent=self.root)
        else:
           conn = mysql.connector.connect(
           host="localhost",
           username="root",
           password="mohit@12345",
           database="mohitdb"
        )
        my_cursor = conn.cursor()
        my_cursor.execute(" Update customer set name=%s, mother=%s, gender=%s, postcode=%s, mobile=%s, email=%s, nationality=%s,idproof=%s, idnumber=%s, address=%s where ref=%s",(
                                                        
                                                        self.var_cust_name.get(),
                                                        self.var_mother.get(),
                                                        self.var_gender.get(),
                                                        self.var_post.get(),
                                                        self.var_mobile.get(),
                                                        self.var_email.get(),
                                                        self.var_nationality.get(),
                                                        self.var_id_proof.get(),
                                                        self.var_id_number.get(),
                                                        self.var_address.get(),
                                                        self.var_ref.get()                                                                                                                                                                            
        ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update", "Customer details has been updated successfully",parent=self.root)

    def delete_data(self):
        if self.var_ref.get() == "":
         messagebox.showerror("Error", "Select customer to delete", parent=self.root)
         return

        confirm = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete this customer?",
        parent=self.root
    )

        if not confirm:
         return

        conn = mysql.connector.connect(
        host="localhost",
        username="root",
        password="mohit@12345",
        database="mohitdb"
       )
        my_cursor = conn.cursor()

        my_cursor.execute(
        "DELETE FROM customer WHERE ref=%s",
        (self.var_ref.get(),)
       )

        conn.commit()
        conn.close()

        self.fetch_data()
        messagebox.showinfo("Success", "Customer deleted successfully", parent=self.root)

 
    def reset(self):
       #self.var_ref.set(""),
       self.var_cust_name.set(""),
       self.var_mother.set(""),
       #self.var_gender.set(""),
       self.var_post.set(""),
       self.var_mobile.set(""),
       self.var_email.set(""),
       #self.var_nationality.set(""),
       #self.var_id_proof.set(""),
       self.var_id_number.set(""),
       self.var_address.set(r"")      
       x=random.randint(1000,9999)
       self.var_ref.set(str(x)) 

    def search(self):    
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="mohit@12345",
            database="mohitdb"
        )
        my_cursor = conn.cursor()
    
        query = "SELECT * FROM customer WHERE " + str(self.search_var.get()) + " LIKE %s"
        value = ("%" + self.txt_search.get() + "%",)
    
        my_cursor.execute(query, value)
        rows = my_cursor.fetchall()
    
        # ✅ correct delete
        self.Cust_details_Table.delete(*self.Cust_details_Table.get_children())
    
        for i in rows:
            self.Cust_details_Table.insert("", END, values=i)
    
        conn.close()

           
          




                        
if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()
