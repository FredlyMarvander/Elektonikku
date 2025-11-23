from User import User
from tkinter import *
from tkinter import ttk
from user_service import user_services




class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title = "Elektronikku"
        self.root.geometry("800x600")
        ttk.Label(self.root, text="Welcome to Elektronikku", font=("Helvetica", 16)).pack(pady=20)
        self.entry_username = ttk.Entry(self.root)
        self.entry_username.pack(pady=10)
        self.entry_password = ttk.Entry(self.root, show="*")
        self.entry_password.pack(pady=10)
        self.btn_login = ttk.Button(self.root, text="Login", command=self.proses_login)
        self.btn_login.pack(pady=20)

    
    
    def proses_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        print("Attempting login with:", username, password)
        if (user_services.login(username, password)):
            self.clear_window()
            self.home_screen()
            
    def home_screen(self):
        ttk.Label(self.root, text="Home Screen", font=("Helvetica", 16)).pack(pady=20)
        # Additional home screen widgets can be added here

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

root = Tk()
app = MainApp(root)
root.mainloop()