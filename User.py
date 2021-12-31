import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mBox
import pymysql
import Dbcon as Db


class UserApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ADD USER.")
        self.geometry("690x450+10+60")
        self.configure(bg="gray")
        self.resizable(0, 0)
        # ====================Variables========================#
        userid = tk.StringVar
        fname = tk.StringVar
        sname = tk.StringVar
        gender = tk.StringVar
        phoneno = tk.StringVar
        upass = tk.StringVar
        cupass = tk.StringVar

        bg_color = "green"
        fg_color = "white"




        # ============================================================Frames============================================

        self.MFrame = LabelFrame(self, width=600, height=450, font=('arial', 15, 'bold'), \
                                     bg=bg_color, bd=15, relief='ridge')
        self.MFrame.grid(row=0, column=0, padx=10, pady=20)

        self.CFrame = LabelFrame(self.MFrame, width=300, height=300, font=('arial', 12, 'bold'), \
                                  relief='ridge', bd=10, bg='lightblue', text='NEW USER')
        self.CFrame.grid(row=1, column=0, padx=10)

        self.DFrame = LabelFrame(self.MFrame, width=300, height=300, font=('arial', 12, 'bold'), \
                                  relief='ridge', bd=10, bg='lightblue', text='USER INFO')
        self.DFrame.grid(row=1, column=1, padx=10)

        self.EFrame = LabelFrame(self,width=500, height=100, font=('arial', 10, 'bold'), \
                                  bg='lightblue', relief='ridge', bd=13)
        self.EFrame.grid(row=2, column=0, pady=10)

        # ========================================================Labels of CFrame=====================================
        self.Luserid = Label(self.CFrame, text='USER ID:', font=('arial', 10, 'bold'), bg = bg_color,fg = fg_color)
        self.Luserid.grid(row=0, column=0, sticky=W, padx=20, pady=10)
        self.Lfname = Label(self.CFrame, text='F Name:', font=('arial', 10, 'bold'), bg = bg_color,fg = fg_color)
        self.Lfname.grid(row=1, column=0, sticky=W, padx=20)
        self.Lsname = Label(self.CFrame, text='Sur Name:', font=('arial', 10, 'bold'), bg = bg_color,fg = fg_color)
        self.Lsname.grid(row=2, column=0, sticky=W, padx=20)
        self.Lgender = Label(self.CFrame, text='Gender:', font=('arial', 10, 'bold'), bg = bg_color,fg = fg_color)
        self.Lgender.grid(row=3, column=0, sticky=W, padx=20)
        self.Lphoneno = Label(self.CFrame, text='Phone No:', font=('arial', 10, 'bold'), bg = bg_color,fg = fg_color)
        self.Lphoneno.grid(row=4, column=0, sticky=W, padx=20)
        self.Lupass = Label(self.CFrame, text='Password:', font=('arial', 10, 'bold'), bg = bg_color,fg = fg_color)
        self.Lupass.grid(row=5, column=0, sticky=W, padx=20)
        self.Lcupass = Label(self.CFrame, text='Confirm Password:', font=('arial', 10, 'bold'), bg = bg_color,fg = fg_color)
        self.Lcupass.grid(row=6, column=0, sticky=W, padx=20)

        # ========================================================Entries of CFrame====================================
        self.Txtuserid = Entry(self.CFrame, font=('arial', 10, 'bold'), textvariable=userid)
        self.Txtuserid.grid(row=0, column=1, padx=10, pady=5)
        self.Txtfname = Entry(self.CFrame, font=('arial', 10, 'bold'), textvariable=fname)
        self.Txtfname.grid(row=1, column=1, padx=10, pady=5)
        self.Txtsname = Entry(self.CFrame, font=('arial', 10, 'bold'), textvariable=sname)
        self.Txtsname.grid(row=2, column=1, padx=10, pady=5)
        self.genderChosen = ttk.Combobox(self.CFrame, font=('arial', 10, 'bold'), width=17, textvariable=gender, state='readonly')
        self.genderChosen['values'] = ("MALE", "FEMALE")
        self.genderChosen.grid(row=3, column=1, padx=10, pady=5)
        self.genderChosen.current(0)
        self.Txtphoneno = Entry(self.CFrame, font=('arial', 10, 'bold'), textvariable=phoneno)
        self.Txtphoneno.grid(row=4, column=1, padx=10, pady=5)
        self.Txtupass = Entry(self.CFrame, font=('arial', 10, 'bold'), show = "*", textvariable=upass)
        self.Txtupass.grid(row=5, column=1, padx=10, pady=5)
        self.Txtcupass = Entry(self.CFrame, font=('arial', 10, 'bold'), show = "*", textvariable=cupass)
        self.Txtcupass.grid(row=6, column=1, padx=10, pady=5)
        # ========================================================Buttons of EFrame===============================
        self.btnSave = Button(self.EFrame, text='SAVE', font=('arial', 10, 'bold'), width=8, bg = bg_color,fg = fg_color,command=self.savst)
        self.btnSave.grid(row=0, column=0, padx=10, pady=10)
        self.btnReset = Button(self.EFrame, text='RESET', font=('arial', 10, 'bold'), width=8, bg = bg_color,fg = fg_color,command=self.allclear)
        self.btnReset.grid(row=0, column=1, padx=10, pady=10)
        self.btnUpdate = Button(self.EFrame, text='UPDATE', font=('arial', 10, 'bold'), width=8, bg = bg_color,fg = fg_color,command=self.upbk)
        self.btnUpdate.grid(row=0, column=2, padx=10, pady=10)
        self.btnDelete = Button(self.EFrame, text='DELETE', font=('arial', 10, 'bold'), width=8, bg = bg_color,fg = fg_color,command=self.delst)
        self.btnDelete.grid(row=0, column=3, padx=10, pady=10)
        self.btnSearch = Button(self.EFrame, text='VIEW', font=('arial', 10, 'bold'), width=8, bg = bg_color,fg = fg_color,command=self.searchst)
        self.btnSearch.grid(row=0, column=4, padx=10, pady=10)
        self.btnExit = Button(self.EFrame, text='EXIT', font=('arial', 10, 'bold'), width=8, bg = bg_color,fg = fg_color,command=self.exitt)
        self.btnExit.grid(row=0, column=5, padx=10, pady=10)

        # ===============================================List Box and scrollbar====================================
        self.scrollbar = Scrollbar(self.DFrame)
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.listbox = Listbox(self.DFrame, width=30, height=10, font=('arial', 10, 'bold'))
        self.listbox.grid(row=0, column=0)

    # ==========Exit Function==========
    def exitt(self):
        result = mBox.askquestion(self, 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            self.destroy()

    # ==========Clear Function==========
    def allclear(self):
        self.Txtuserid.delete(0, END)
        self.Txtfname.delete(0, END)
        self.Txtsname.delete(0, END)
        self.Txtphoneno.delete(0, END)
        self.Txtupass.delete(0, END)
        self.Txtcupass.delete(0, END)
        self.listbox.delete(0, 7)

    # ==========Register student Function==========
    def savst(self):
        userid = self.Txtuserid.get()
        fname = self.Txtfname.get()
        sname = self.Txtsname.get()
        gender = self.genderChosen.get()
        phoneno = self.Txtphoneno.get()
        upass = self.Txtupass.get()
        cupass = self.Txtcupass.get()

        if userid == "" or fname == "" or sname == "" or gender == "" or phoneno == "" or upass == "" or cupass == "":
            mBox.showerror(self, 'Error No Blanks allowed')
        elif upass != cupass:
            mBox.showerror(self, 'Passwords do not match')
        else:
            try:
                conn = pymysql.connect(**Db.dbConfig)
                cursor = conn.cursor()
                cursor.execute("select * from userlogin where userid=%s", userid)
                rowcount = cursor.rowcount
                if cursor.rowcount == 1:
                    mBox.showinfo('Information', "user. already saved")

                else:
                    cursor.execute("Insert into userlogin( userid, fname, sname, gender, phoneno, upass, cupass)"
                                   "values(%s,%s,%s,%s,%s,%s,%s)", (userid, fname, sname, gender, phoneno, upass, cupass))
                    conn.commit()
                    if cursor:
                        mBox.showinfo("Done", "user Inserted Successfully")
                        ask = mBox.askyesno("Confirm", "Do you want to add another user?")
                        if ask:
                            self.allclear()
                        else:
                            self.allclear()
                    else:
                        mBox.showerror("Error", "Unable to save")
                    cursor.close()
                    conn.close()
            except Exception as es:
                  print('Error', f"due to :{str(es)}")

    # ==========Delete student Function==========
    def delst(self):
        userid = self.Txtuserid.get()
        if userid == "":
            mBox.showerror(self, 'Enter user id')
        else:
            try:
                conn = pymysql.connect(**Db.dbConfig)
                cursor = conn.cursor()
                cursor.execute("DELETE FROM userlogin where userid=%s", userid)
                conn.commit()
                rowcount = cursor.rowcount
                if cursor.rowcount == 1:
                    mBox.showinfo('Information', "deleted Successfully")
                    ask = mBox.askyesno("Confirm", "Do you want to delete another user?")
                    if ask:
                        self.allclear()
                    else:
                        self.allclear()
                else:
                    mBox.showinfo("Error", "wrong user id")
                    self.allclear()
                    cursor.close()
                    conn.close()
            except Exception as es:
                  print('Error', f"due to :{str(es)}")

    # ==========Update student Function==========
    def upbk(self):
        userid = self.Txtuserid.get()
        fname = self.Txtfname.get()
        sname = self.Txtsname.get()
        gender = self.genderChosen.get()
        phoneno = self.Txtphoneno.get()
        upass = self.Txtupass.get()
        cupass = self.Txtcupass.get()

        if userid == "" or fname == "" or sname == "" or gender == "" or phoneno == "" or upass == "" or cupass == "":
            mBox.showerror(self, 'Error,Enter user id, No Blanks allowed')
        else:
            try:
                conn = pymysql.connect(**Db.dbConfig)
                cursor = conn.cursor()
                cursor.execute("UPDATE userlogin SET fname=%s,sname=%s,gender=%s,phoneno=%s,upass=%s,"
                               "cupass=%s where userid=%s", (fname, sname, gender, phoneno,  upass,
                                                            cupass, userid))
                conn.commit()
                rowcount = cursor.rowcount
                if cursor.rowcount == 1:
                    mBox.showinfo("Done", "user Updated Successfully")
                    ask = mBox.askyesno("Confirm", "Do you want to Update another record?")
                    if ask:
                        self.allclear()
                else:
                    mBox.showerror("Error", "Unable to update wrong user id")
                    cursor.close()
                    conn.close()
            except Exception as es:
                  print('Error', f"due to :{str(es)}")

    # ==========Search student & Display in Listbox Function==========
    def searchst(self):
        userid = self.Txtuserid.get()
        if userid == "":
            mBox.showerror(self, 'Error Enter user id', )
        else:
            try:
                conn = pymysql.connect(**Db.dbConfig)
                cursor = conn.cursor()
                cursor.execute("select * from userlogin where userid=%s", userid)
                rowcount = cursor.fetchall()
                for row in rowcount:
                    self.listbox.insert(1, "User Number. :" + str(row[0]))
                    self.listbox.insert(2, "First Name :" + str(row[1]))
                    self.listbox.insert(3, "Sur Name :" + str(row[2]))
                    self.listbox.insert(4, "Gender :" + str(row[3]))
                    self.listbox.insert(5, "Phone Number. :" + str(row[4]))

                if cursor.rowcount == 1:
                    mBox.showinfo('Information', "record found")
                    ask = mBox.askyesno("Confirm", "Do you want to search another record?")
                    if ask:
                        self.allclear()
                else:
                    mBox.showinfo("Error", "Unable to Search")
                    self.allclear()
                    cursor.close()
                    conn.close()
            except Exception as es:
                  print('Error', f"due to :{str(es)}")


if __name__ == "__main__":
    usertapp = UserApp()
    usertapp.mainloop()