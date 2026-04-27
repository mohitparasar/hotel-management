from tkinter import *
from PIL import Image, ImageTk
from customer import Cust_Win
from room import RoomBooking
from detailes import DetailsRoom

class HospitalManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1515x800+0+0")


#----------------------- 1st image ----------------------------------------------------------------

        img1 = Image.open(r"C:\Users\Mohit\Desktop\hotel management\photo1.jpg")
        img1 = img1.resize((1550, 140), Image.Resampling.LANCZOS)

        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg = Label(self.root, image=self.photoimage1, bd=1, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)

#---------------------------- logo ----------------------------------------------------------------

        img2 = Image.open(r"C:\Users\Mohit\Desktop\hotel management\photo2.jpg")
        img2 = img2.resize((230, 140), Image.Resampling.LANCZOS)

        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimage2, bd=1, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)  

#================================== title ============================

        lbl_title=Label(self.root, text = "HOTEL MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), bg = "black", fg ="gold", bd = 4, relief=RIDGE)              
        lbl_title.place(x=0, y = 140, width=1550, height=50)

#=================================== main frame ============================
        main_frame = Frame(self.root, bd = 4, relief=RIDGE)
        main_frame.place(x=0, y = 190, width=1550, height=620 )  

#==================================== menu =======================================

        lbl_menu=Label(main_frame, text = "MENU", font=("times new roman", 20, "bold"), bg = "black", fg ="gold", bd = 4, relief=RIDGE)              
        lbl_menu.place(x=0, y = 0, width=230) 

#====================================== bttn frame ============================
        btn_frame = Frame(main_frame, bd = 4, relief=RIDGE)
        btn_frame.place(x=0, y = 35, width=228, height=190 )

        cust_btn = Button(btn_frame, text="CUSTOMER",command=self.cust_details,font=("times new roman", 14, "bold"), bg = "black", fg ="gold", bd = 0, width=22, cursor="hand1")                
        cust_btn.grid(row=0, column=0, pady=1)

        room_btn = Button(btn_frame, text="ROOM",command=self.Roombooking,font=("times new roman", 14, "bold"), bg = "black", fg ="gold", bd = 0, width=22, cursor="hand1")                
        room_btn.grid(row=1, column=0,pady=1)

        detail_btn = Button(btn_frame, text="DETAILS",command=self.details_room,font=("times new roman", 14, "bold"), bg = "black", fg ="gold", bd = 0, width=22, cursor="hand1")                
        detail_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, text="REPORT",font=("times new roman", 14, "bold"), bg = "black", fg ="gold", bd = 0, width=22, cursor="hand1")                
        report_btn.grid(row=3, column=0, pady=1)         

        logout_btn = Button(btn_frame, text="LogOut",font=("times new roman", 14, "bold"), bg = "black", fg ="gold", bd = 0, width=22, cursor="hand1")                
        logout_btn.grid(row=4, column=0, pady=1)   


#================================================ right side image ===================================
                       
        img3 = Image.open(r"C:\Users\Mohit\Desktop\hotel management\img6.jpg")
        img3 = img3.resize((1310, 590), Image.Resampling.LANCZOS)

        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(main_frame, image=self.photoimage3, bd=1, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1310, height=590)

#========================================== down images ==========================================

#=========================== down images ============================

        img4 = Image.open(r"C:\Users\Mohit\Desktop\hotel management\img0.jpg")
        img4 = img4.resize((230, 210), Image.Resampling.LANCZOS)

        self.photoimage4 = ImageTk.PhotoImage(img4)
        lblimg4 = Label(main_frame, image=self.photoimage4, bd=1, relief=RIDGE)
        lblimg4.place(x=0, y=225, width=230, height=210)


        img5 = Image.open(r"C:\Users\Mohit\Desktop\hotel management\download.jpg")
        img5 = img5.resize((230, 190), Image.Resampling.LANCZOS)

        self.photoimage5 = ImageTk.PhotoImage(img5)
        lblimg5 = Label(main_frame, image=self.photoimage5, bd=1, relief=RIDGE)
        lblimg5.place(x=0, y=420, width=230, height=190)


    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)

    def Roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=RoomBooking(self.new_window) 

    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)        




if __name__ == "__main__":
    root = Tk()
    obj = HospitalManagementSystem(root)
    root.mainloop()
 