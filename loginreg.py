import tkinter as tk
import os
class loginreg:
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("Account login")
        self.root.geometry("400x350")
        tk.Label(text="Login to continue", width="300", height="2", font=("Calibri", 13)).pack()
        tk.Label(text="").pack()
        path=os.getcwd()
        self.npath=path+"/Users"
        tk.Button(text="Login", height="2", width="30", command =self.login).pack()
        tk.Label(text="").pack()
        tk.Label(text="New user?", width="300", height="1", font=("Calibri", 10)).pack()
        tk.Button(text="Register", height="2", width="30", command=self.register).pack()
        self.root.mainloop()
    def login(self):
        self.login_screen = tk.Toplevel(self.root)
        self.login_screen.title("Login")        
        self.login_screen.geometry("400x300")
        tk.Label(self.login_screen, text="Please enter details below to login").pack()
        tk.Label(self.login_screen, text="").pack()
        self.username_verify =tk.StringVar()
        self.password_verify =tk.StringVar()
        tk.Label(self.login_screen, text="Username * ").pack()
        self.username_login_entry =tk.Entry(self.login_screen, textvariable=self.username_verify)
        self.username_login_entry.pack()
        tk.Label(self.login_screen, text="").pack()
        tk.Label(self.login_screen, text="Password * ").pack()
        self.password_login_entry = tk.Entry(self.login_screen, textvariable=self.password_verify, show= '*')
        self.password_login_entry.pack()
        tk.Label(self.login_screen, text="").pack()
        tk.Button(self.login_screen, text="Login", width=10, height=1, command = self.login_verify).pack()
    def login_verify(self):
        self.username1 = self.username_verify.get()
        password1 = self.password_verify.get()
        l1=len(self.username1)
        l2=len(password1)
        self.username_login_entry.delete(0, l1)
        self.password_login_entry.delete(0, l2)        
        list_of_files = os.listdir(self.npath)
        print(list_of_files)
        if self.username1 in list_of_files:
            file1 = open(self.npath+"/"+self.username1, "r")
            verify = file1.read().splitlines()
            print(type(verify))
            if password1== verify[1]:
                self.login_sucess()

            else:
                self.username1=""
                self.password_not_recognised()

        else:
            self.username1=""
            self.user_not_found()
    def login_sucess(self):     
        self.login_success_screen = tk.Toplevel(self.login_screen)
        self.login_success_screen.title("Success")
        self.login_success_screen.geometry("150x100")
        self.ll=tk.Label(self.login_success_screen, text="Login Success",fg="green")
        self.ll.pack()
        self.lb=tk.Button(self.login_success_screen, text="OK", command=self.delete_login_success)
        self.lb.pack()
        
    # Designing popup for login invalid password

    def password_not_recognised(self):
        self.password_not_recog_screen = tk.Toplevel(self.login_screen)
        self.password_not_recog_screen.title("Success")
        self.password_not_recog_screen.geometry("150x100")
        tk.Label(self.password_not_recog_screen, text="Invalid Password ",fg="red").pack()
        tk.Button(self.password_not_recog_screen, text="OK", command=self.delete_password_not_recognised).pack()

    # Designing popup for user not found
     
    def user_not_found(self):
        
        self.user_not_found_screen =tk.Toplevel(self.login_screen)
        self.user_not_found_screen.title("Success")
        self.user_not_found_screen.geometry("150x100")
        tk.Label(self.user_not_found_screen, text="User Not Found",fg="red").pack()
        tk.Button(self.user_not_found_screen, text="OK", command=self.delete_user_not_found_screen).pack()

    def delete_login_success(self):
        self.root.destroy()



    def delete_password_not_recognised(self):
        self.password_not_recog_screen.destroy()


    def delete_user_not_found_screen(self):
        self.user_not_found_screen.destroy()

    def register(self):
        print('registering')
        self.register_screen =tk.Toplevel(self.root) 
        self.register_screen.title("Register")
        self.register_screen.geometry("300x250")
        self.username =tk.StringVar()
        self.password =tk.StringVar()
        tk.Label(self.register_screen, text="Please enter details below").pack()
        username_lable =tk.Label(self.register_screen, text="Username * ")
        username_lable.pack()
        self.username_entry =tk.Entry(self.register_screen, textvariable=self.username)
        self.username_entry.pack()
        password_lable =tk.Label(self.register_screen, text="Password * ")
        password_lable.pack()
        self.password_entry =tk.Entry(self.register_screen, textvariable=self.password, show='*')
        self.password_entry.pack()
        tk.Button(self.register_screen, text="Register", width=10, height=1,command=self.register_user).pack()
    def register_user(self):
        username_info = self.username.get()
        password_info = self.password.get()
        l1=len(username_info)
        l2=len(password_info)
        if l2!=0 and l1!=0:
            file = open(self.npath+"/"+username_info, "w")
            file.write(username_info + "\n")
            file.write(password_info)
            file.close()

        self.username_entry.delete(0,l1)
        self.password_entry.delete(0,l2)
        if l2!=0:
            tk.Label(self.register_screen, text="Registration Success\nProceed to login", fg="green", font=("calibri", 11)).pack() 

          