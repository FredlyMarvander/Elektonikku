from User import User
from tkinter import *
from tkinter import ttk
from user_service import user_services
from tkinter import messagebox
from product_service import product_services
from Product import Product
from PIL import Image, ImageTk, ImageOps
import requests
from io import BytesIO
import threading
from cart_service import cart_services 
from CartDetail import CartDetail
from cart_detail_service import cart_detail_service
from datetime import date
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt



class MainApp():
    def __init__(self, root):
        self.root = root
        self.root.title("🛒 Elektronikku")
        self.root.state("zoomed")
        self.root.configure(bg="#f0f0f0")
        
        # Color scheme
        self.PRIMARY_COLOR = "#4A90E2"
        self.SUCCESS_COLOR = "#52C41A"
        self.DANGER_COLOR = "#F5222D"
        self.WARNING_COLOR = "#FA8C16"
        self.INFO_COLOR = "#1890FF"
        self.DARK_COLOR = "#262626"
        self.LIGHT_BG = "#FFFFFF"
        self.GRAY_BG = "#F5F5F5"
        self.TEXT_COLOR = "#333333"
        self.SECONDARY_TEXT = "#8C8C8C"
        
        self.home_screen()

    def home_screen(self):
        self.clear_window()
        main_frame = Frame(self.root, bg=self.GRAY_BG)
        main_frame.pack(fill=BOTH, expand=YES)
        
        # Header Section
        header_frame = Frame(main_frame, bg="#4A70A9", height=120)
        header_frame.pack(fill=X)
        header_frame.pack_propagate(False)
        
        Label(
            header_frame,
            text="🛒 ELEKTRONIKKU",
            font=("Arial", 36, "bold"),
            bg="#4A70A9",
            fg="white"
        ).pack(pady=10)
        
        Label(
            header_frame,
            text="Your Trusted Electronics Marketplace",
            font=("Arial", 14),
            bg="#4A70A9",
            fg="white"
        ).pack()
        
        # Content Section
        content_frame = Frame(main_frame, bg=self.GRAY_BG)
        content_frame.pack(expand=YES, fill=BOTH, pady=80)
        
        # Welcome Text
        Label(
            content_frame,
            text="Welcome! Please select your role",
            font=("Arial", 18),
            bg="#F9F8F6",
            fg=self.TEXT_COLOR
        ).pack(pady=(0, 40))
        
        # Button Container
        button_frame = Frame(content_frame, bg=self.GRAY_BG)
        button_frame.pack()
        
        # Admin Button
        self.buttonAdmin = Button(
            button_frame,
            text="Admin Login",
            font=("Arial", 16, "bold"),
            bg="#4A70A9",
            fg="white",
            activebackground="#4A70A9",
            activeforeground="white",
        
            bd=0,
            padx=40,
            pady=20,
            cursor="hand2",
            command=self.admin
        )
        self.buttonAdmin.pack(pady=15)

        
        # Customer Button
        self.buttonCustomer = Button(
            button_frame,
            text="Customer Login",
            font=("Arial", 16, "bold"),
            bg="#4A70A9",
            fg="white",
            activebackground="#4A70A9",
            activeforeground="white",
          
            bd=0,
            padx=40,
            pady=20,
            cursor="hand2",
            command=self.customer
        )
        self.buttonCustomer.pack(pady=15)


    def admin(self):
        self.clear_window()
        
        main_frame = Frame(self.root, bg=self.GRAY_BG)
        main_frame.pack(fill=BOTH, expand=YES)
        
        # Header
        header_frame = Frame(main_frame, bg="#4A70A9", height=100)
        header_frame.pack(fill=X)
        header_frame.pack_propagate(False)
        
        Label(
            header_frame,
            text="Admin Login",
            font=("Arial", 28, "bold"),
            bg="#4A70A9",
            fg="white"
        ).pack(pady=30)
        
        # Content
        content_frame = Frame(main_frame, bg=self.LIGHT_BG, bd=0)
        content_frame.pack(pady=60, padx=200)
        
        inner_frame = Frame(content_frame, bg=self.LIGHT_BG)
        inner_frame.pack(padx=60, pady=40)
        
        # Email
        Label(
            inner_frame,
            text="Email Address",
            font=("Arial", 12, "bold"),
            bg=self.LIGHT_BG,
            fg=self.TEXT_COLOR,
            anchor=W
        ).pack(fill=X, pady=(0, 5))
        
        self.entry_email = Entry(
            inner_frame,
            font=("Arial", 13),
            bd=1,
            relief=SOLID,
            highlightthickness=2,
            highlightbackground="#D9D9D9",
            highlightcolor=self.INFO_COLOR
        )
        self.entry_email.pack(fill=X, ipady=10, pady=(0, 20))
        
        # Password
        Label(
            inner_frame,
            text="Password",
            font=("Arial", 12, "bold"),
            bg=self.LIGHT_BG,
            fg=self.TEXT_COLOR,
            anchor=W
        ).pack(fill=X, pady=(0, 5))
        
        self.entry_password = Entry(
            inner_frame,
            font=("Arial", 13),
            show="●",
            bd=1,
            relief=SOLID,
            highlightthickness=2,
            highlightbackground="#D9D9D9",
            highlightcolor=self.INFO_COLOR
        )
        self.entry_password.pack(fill=X, ipady=10, pady=(0, 30))
        
        # Login Button
        self.btn_login = Button(
            inner_frame,
            text="Login",
            font=("Arial", 14, "bold"),
            bg="#4A70A9",
            fg="white",
            activebackground="#4A70A9",
            activeforeground="white",
            relief=FLAT,
            bd=0,
            cursor="hand2",
            command=self.proses_login_admin
        )
        self.btn_login.pack(fill=X, ipady=12, pady=(0, 10))
        self.btn_login.bind("<Enter>", lambda e: e.widget.config(bg="#096DD9"))
        self.btn_login.bind("<Leave>", lambda e: e.widget.config(bg=self.INFO_COLOR))
        
        # Back Button
        btn_back = Button(
            inner_frame,
            text="← Back",
            font=("Arial", 12),
            bg=self.LIGHT_BG,
            fg=self.SECONDARY_TEXT,
            activebackground=self.GRAY_BG,
            relief=FLAT,
            bd=1,
            cursor="hand2",
            command=self.home_screen
        )
        btn_back.pack(fill=X, ipady=8)
        btn_back.bind("<Enter>", lambda e: e.widget.config(bg=self.GRAY_BG))
        btn_back.bind("<Leave>", lambda e: e.widget.config(bg=self.LIGHT_BG))

    def customer(self):
        self.clear_window()
        
        main_frame = Frame(self.root, bg=self.GRAY_BG)
        main_frame.pack(fill=BOTH, expand=YES)
        
        # Header
        header_frame = Frame(main_frame, bg="#4A70A9", height=100)
        header_frame.pack(fill=X)
        header_frame.pack_propagate(False)
        
        Label(
            header_frame,
            text="Customer Login",
            font=("Arial", 28, "bold"),
            bg="#4A70A9",
            fg="white"
        ).pack(pady=30)
        
        # Content
        content_frame = Frame(main_frame, bg=self.LIGHT_BG, bd=0)
        content_frame.pack(pady=60, padx=200)
        
        inner_frame = Frame(content_frame, bg=self.LIGHT_BG)
        inner_frame.pack(padx=60, pady=40)
        
        # Email
        Label(
            inner_frame,
            text="Email Address",
            font=("Arial", 12, "bold"),
            bg=self.LIGHT_BG,
            fg=self.TEXT_COLOR,
            anchor=W
        ).pack(fill=X, pady=(0, 5))
        
        self.entry_email = Entry(
            inner_frame,
            font=("Arial", 13),
            bd=1,
            relief=SOLID,
            highlightthickness=2,
            highlightbackground="#D9D9D9",
            highlightcolor="#4A70A9"
        )
        self.entry_email.pack(fill=X, ipady=10, pady=(0, 20))
        
        # Password
        Label(
            inner_frame,
            text="Password",
            font=("Arial", 12, "bold"),
            bg=self.LIGHT_BG,
            fg=self.TEXT_COLOR,
            anchor=W
        ).pack(fill=X, pady=(0, 5))
        
        self.entry_password = Entry(
            inner_frame,
            font=("Arial", 13),
            show="●",
            bd=1,
            relief=SOLID,
            highlightthickness=2,
            highlightbackground="#D9D9D9",
            highlightcolor="#4A70A9"
        )
        self.entry_password.pack(fill=X, ipady=10, pady=(0, 30))
        
        # Login Button
        self.btn_login = Button(
            inner_frame,
            text="Login",
            font=("Arial", 14, "bold"),
            bg="#4A70A9",
            fg="white",
            activebackground="#4A70A9",
            activeforeground="white",
            relief=FLAT,
            bd=0,
            cursor="hand2",
            command=self.proses_login_customer
        )
        self.btn_login.pack(fill=X, ipady=12, pady=(0, 10))

        
        # Register Button
        self.btn_register = Button(
            inner_frame,
            text="Register",
            font=("Arial", 12),
            bg=self.LIGHT_BG,
            fg=self.PRIMARY_COLOR,
            activebackground=self.GRAY_BG,
            relief=SOLID,
            bd=1,
            cursor="hand2",
            command=self.register_user
        )
        self.btn_register.pack(fill=X, ipady=10, pady=(0, 10))
        self.btn_register.bind("<Enter>", lambda e: e.widget.config(bg=self.GRAY_BG))
        self.btn_register.bind("<Leave>", lambda e: e.widget.config(bg=self.LIGHT_BG))
        
        # Back Button
        btn_back = Button(
            inner_frame,
            text="← Back",
            font=("Arial", 12),
            bg=self.LIGHT_BG,
            fg=self.SECONDARY_TEXT,
            activebackground=self.GRAY_BG,
            relief=FLAT,
            bd=1,
            cursor="hand2",
            command=self.home_screen
        )
        btn_back.pack(fill=X, ipady=8)
        btn_back.bind("<Enter>", lambda e: e.widget.config(bg=self.GRAY_BG))
        btn_back.bind("<Leave>", lambda e: e.widget.config(bg=self.LIGHT_BG))

    def register_user(self):
        self.clear_window()
        
        main_frame = Frame(self.root, bg=self.GRAY_BG)
        main_frame.pack(fill=BOTH, expand=YES)
        
        # Header
        header_frame = Frame(main_frame, bg="#4A70A9", height=100)
        header_frame.pack(fill=X)
        header_frame.pack_propagate(False)
        
        Label(
            header_frame,
            text="Create New Account",
            font=("Arial", 28, "bold"),
            bg="#4A70A9",
            fg="white"
        ).pack(pady=30)
        
        # Content with scrollbar
        content_frame = Frame(main_frame, bg=self.LIGHT_BG, width=400, height=800)
        content_frame.pack(pady=10, padx=200)
        content_frame.pack_propagate(False)
        
        inner_frame = Frame(content_frame, bg=self.LIGHT_BG, width=300, height=700)
        inner_frame.pack(padx=30, pady=20)
        inner_frame.pack_propagate(False)
        
        # Username
        Label(
            inner_frame,
            text="Username",
            font=("Arial", 12, "bold"),
            bg=self.LIGHT_BG,
            fg=self.TEXT_COLOR,
            anchor=W
        ).pack(fill=X, pady=(0, 5))
        
        self.entry_username = Entry(
            inner_frame,
            font=("Arial", 13),
            bd=1,
            relief=SOLID,
            highlightthickness=2,
            highlightbackground="#D9D9D9",
            highlightcolor=self.PRIMARY_COLOR
        )
        self.entry_username.pack(fill=X, ipady=10, pady=(0, 15))
        
        # Email
        Label(
            inner_frame,
            text="Email Address",
            font=("Arial", 12, "bold"),
            bg=self.LIGHT_BG,
            fg=self.TEXT_COLOR,
            anchor=W
        ).pack(fill=X, pady=(0, 5))
        
        self.entry_email = Entry(
            inner_frame,
            font=("Arial", 13),
            bd=1,
            relief=SOLID,
            highlightthickness=2,
            highlightbackground="#D9D9D9",
            highlightcolor=self.PRIMARY_COLOR
        )
        self.entry_email.pack(fill=X, ipady=10, pady=(0, 15))
        
        # Password
        Label(
            inner_frame,
            text="Password",
            font=("Arial", 12, "bold"),
            bg=self.LIGHT_BG,
            fg=self.TEXT_COLOR,
            anchor=W
        ).pack(fill=X, pady=(0, 5))
        
        self.entry_password = Entry(
            inner_frame,
            font=("Arial", 13),
            show="●",
            bd=1,
            relief=SOLID,
            highlightthickness=2,
            highlightbackground="#D9D9D9",
            highlightcolor=self.PRIMARY_COLOR
        )
        self.entry_password.pack(fill=X, ipady=10, pady=(0, 15))
        
        # Balance
        Label(
            inner_frame,
            text="Initial Balance (Rp)",
            font=("Arial", 12, "bold"),
            bg=self.LIGHT_BG,
            fg=self.TEXT_COLOR,
            anchor=W
        ).pack(fill=X, pady=(0, 5))
        
        self.entry_balance = Entry(
            inner_frame,
            font=("Arial", 13),
            bd=1,
            relief=SOLID,
            highlightthickness=2,
            highlightbackground="#D9D9D9",
            highlightcolor=self.PRIMARY_COLOR
        )
        self.entry_balance.pack(fill=X, ipady=10, pady=(0, 25))
        
        # Register Button
        self.btn_register = Button(
            inner_frame,
            text="Register",
            font=("Arial", 14, "bold"),
            bg="#4A70A9",
            fg="white",
            activebackground="#4A70A9",
            activeforeground="white",
            relief=FLAT,
            bd=0,
            cursor="hand2",
            command=self.process_register
        )
        self.btn_register.pack(fill=X, ipady=12, pady=(0, 10))
        self.btn_register.bind("<Enter>", lambda e: e.widget.config(bg="#389E0D"))
        self.btn_register.bind("<Leave>", lambda e: e.widget.config(bg=self.SUCCESS_COLOR))
        
        # Back Button
        btn_back = Button(
            inner_frame,
            text="← Back to Login",
            font=("Arial", 12),
            bg=self.LIGHT_BG,
            fg=self.SECONDARY_TEXT,
            activebackground=self.GRAY_BG,
            relief=FLAT,
            bd=1,
            cursor="hand2",
            command=self.customer
        )
        btn_back.pack(fill=X, ipady=8)
        btn_back.bind("<Enter>", lambda e: e.widget.config(bg=self.GRAY_BG))
        btn_back.bind("<Leave>", lambda e: e.widget.config(bg=self.LIGHT_BG))

    def process_register(self):
        if not self.entry_username.get() or not self.entry_email.get() or not self.entry_password.get() or not self.entry_balance.get():
            messagebox.showerror("Error", "All fields are required!")
            return
        
        try:
            balance = int(self.entry_balance.get())
        except ValueError:
            messagebox.showerror("Error", "Balance must be a number")
            return
        
        if int(self.entry_balance.get()) < 1:
            messagebox.showerror("Error", "Balance Must Greater than 0")
            return

        username = self.entry_username.get()
        email = self.entry_email.get()
        password = self.entry_password.get()
        role = "customer"  
        balance = self.entry_balance.get()    

       
        existed_email = user_services.getUserByEmail(email)
        if existed_email:
            messagebox.showerror("Error", "Email already exists!")
            return

       
        new_user = User(username, email, password, role, balance)
        new_user.register()
        messagebox.showinfo("Success", "Registration successful! Please log in.")
        self.customer()

    def proses_login_customer(self):
        if not self.entry_email.get() or not self.entry_password.get():
            messagebox.showerror("Error", "All fields are required!")
            return

        email = self.entry_email.get()
        password = self.entry_password.get()
       
        if (user_services.login_customer(email, password)):
            messagebox.showinfo("Info", "Login Successfully!")
            self.current_customer_id = user_services.getUserByEmail(email)[0]
            self.clear_window()
            self.home_screen_customer()
        else:
            messagebox.showerror("Error", "Email or Password is Wrong")

    def proses_login_admin(self):
        if not self.entry_email.get() or not self.entry_password.get():
            messagebox.showerror("Error", "All fields are required!")
            return

        email = self.entry_email.get()
        password = self.entry_password.get()
        self.login = user_services.login_admin(email, password)

        
        
        if (self.login):
            messagebox.showinfo("Info", "Login Successfully!")
            self.userId = user_services.getUserByEmail(email)[0]
            self.clear_window()
            self.home_screen_admin()
        else:
            messagebox.showerror("Error", "Email or Password is Wrong")

        self.current_admin_id = self.login[0]
            
    def home_screen_admin(self):
        self.clear_window()
        
        main_frame = Frame(self.root, bg=self.GRAY_BG)
        main_frame.pack(fill=BOTH, expand=YES)
        
        # Header
        header_frame = Frame(main_frame, bg="#4A70A9", height=120)
        header_frame.pack(fill=X)
        header_frame.pack_propagate(False)
        
        Label(
            header_frame,
            text="Admin Dashboard",
            font=("Arial", 32, "bold"),
            bg="#4A70A9",
            fg="white"
        ).pack(pady=35)
        
        # Content
        content_frame = Frame(main_frame, bg=self.GRAY_BG)
        content_frame.pack(pady=25)
        
        # View Products Button
        self.btn_view_products = Button(
            content_frame,
            text="View Products",
            font=("Arial", 16, "bold"),
            bg=self.PRIMARY_COLOR,
            fg="white",
            activebackground="#096DD9",
            activeforeground="white",
            relief=FLAT,
            bd=0,
            width=25,
            pady=15,
            cursor="hand2",
            command=self.view_products
        )
        self.btn_view_products.pack(pady=12)
        self.btn_view_products.bind("<Enter>", lambda e: e.widget.config(bg="#096DD9"))
        self.btn_view_products.bind("<Leave>", lambda e: e.widget.config(bg=self.PRIMARY_COLOR))
        
  
        self.btn_view_customers = Button(
            content_frame,
            text="View Customers",
            font=("Arial", 16, "bold"),
            bg="#4A70A9",
            fg="white",
            activebackground="#4A70A9",
            activeforeground="white",
            relief=FLAT,
            bd=0,
            width=25,
            pady=15,
            cursor="hand2",
            command=self.view_customers
        )
        self.btn_view_customers.pack(pady=12)
        self.btn_view_customers.bind("<Enter>", lambda e: e.widget.config(bg="#389E0D"))
        self.btn_view_customers.bind("<Leave>", lambda e: e.widget.config(bg=self.SUCCESS_COLOR))
        
        # Add Admin Button
        self.btn_add_admin = Button(
            content_frame,
            text="Add Admin",
            font=("Arial", 16, "bold"),
            bg=self.WARNING_COLOR,
            fg="white",
            activebackground="#D46B08",
            activeforeground="white",
            relief=FLAT,
            bd=0,
            width=25,
            pady=15,
            cursor="hand2",
            command=self.add_admin
        )
        self.btn_add_admin.pack(pady=12)
        self.btn_add_admin.bind("<Enter>", lambda e: e.widget.config(bg="#D46B08"))
        self.btn_add_admin.bind("<Leave>", lambda e: e.widget.config(bg=self.WARNING_COLOR))

        self.btn_add_admin = Button(
            content_frame,
            text="View Sales Reports",
            font=("Arial", 16, "bold"),
            bg=self.WARNING_COLOR,
            fg="white",
            activebackground="#D46B08",
            activeforeground="white",
            relief=FLAT,
            bd=0,
            width=25,
            pady=15,
            cursor="hand2",
            command=self.sales_reports
        )
        self.btn_add_admin.pack(pady=12)
        self.btn_add_admin.bind("<Enter>", lambda e: e.widget.config(bg="#D46B08"))
        self.btn_add_admin.bind("<Leave>", lambda e: e.widget.config(bg=self.WARNING_COLOR))
        
        # Logout Button
        self.btn_logout = Button(
            content_frame,
            text="Logout",
            font=("Arial", 16, "bold"),
            bg=self.DANGER_COLOR,
            fg="white",
            activebackground="#CF1322",
            activeforeground="white",
            relief=FLAT,
            bd=0,
            width=25,
            pady=15,
            cursor="hand2",
            command=self.logout
        )
        self.btn_logout.pack(pady=12)
        self.btn_logout.bind("<Enter>", lambda e: e.widget.config(bg="#CF1322"))
        self.btn_logout.bind("<Leave>", lambda e: e.widget.config(bg=self.DANGER_COLOR))

    def sales_reports(self):
        self.clear_window()
        
        main_frame = Frame(self.root, bg=self.GRAY_BG)
        main_frame.pack(fill=BOTH, expand=YES)
        
        # Header
        header_frame = Frame(main_frame, bg="#4A70A9", height=100)
        header_frame.pack(fill=X)
        header_frame.pack_propagate(False)
        
        Label(
            header_frame,
            text="Sales Reports",
            font=("Arial", 28, "bold"),
            bg="#4A70A9",
            fg="white"
        ).pack(pady=30)
        
  
        content_frame = Frame(main_frame, bg=self.LIGHT_BG, width=700, height=700)
        content_frame.pack(pady=10, padx=200)
        content_frame.pack_propagate(False)
        
        inner_frame = Frame(content_frame, bg=self.LIGHT_BG, width=600, height=700)
        inner_frame.pack(padx=30, pady=10)
        inner_frame.pack_propagate(False)
        
        cart = cart_services.getCartAndCartDetails(self.current_admin_id)
        
        
        dates = []
        totalPrices = []

        for data in cart:
            date = data[0]
            totalPrice = data[1]

            dates.append(date.strftime("%Y-%m-%d"))
            totalPrices.append(totalPrice)



        # Buat chart
        fig, ax = plt.subplots()
        ax.bar(dates, totalPrices)
        ax.set_title("Total Penjualan per Tanggal")
        ax.set_xlabel("Tanggal")
        ax.set_ylabel("Total Penjualan")

        # Embed ke Tkinter
        chart = FigureCanvasTkAgg(fig, inner_frame)
        chart.get_tk_widget().pack(fill="both", expand=True)

     
            
        
        # Back Button
        btn_back = Button(
            inner_frame,
            text="← Back to Dashboard",
            font=("Arial", 12),
            bg=self.LIGHT_BG,
            fg=self.SECONDARY_TEXT,
            activebackground=self.GRAY_BG,
            relief=FLAT,
            bd=1,
            cursor="hand2",
            command=self.home_screen_admin
        )
        btn_back.pack(fill=X, ipady=8)
        btn_back.bind("<Enter>", lambda e: e.widget.config(bg=self.GRAY_BG))
        btn_back.bind("<Leave>", lambda e: e.widget.config(bg=self.LIGHT_BG))

    def add_admin(self):
        self.clear_window()
        
        main_frame = Frame(self.root, bg=self.GRAY_BG)
        main_frame.pack(fill=BOTH, expand=YES)

        
        # Header
        header_frame = Frame(main_frame, bg="#4A70A9", height=100)
        header_frame.pack(fill=X)
        header_frame.pack_propagate(False)
        
        Label(
            header_frame,
            text="Add New Admin",
            font=("Arial", 28, "bold"),
            bg="#4A70A9",
            fg="white"
        ).pack(pady=30)
        
        # Content
        content_frame = Frame(main_frame, bg=self.LIGHT_BG, width=400, height=700)
        content_frame.pack(pady=20, padx=200)
        content_frame.pack_propagate(False)
        
        inner_frame = Frame(content_frame, bg=self.LIGHT_BG, width=300, height=600)
        inner_frame.pack(padx=30, pady=40)
        inner_frame.pack_propagate(False)
        # Username
        Label(
            inner_frame,
            text="Username",
            font=("Arial", 12, "bold"),
            bg=self.LIGHT_BG,
            fg=self.TEXT_COLOR,
            anchor=W
        ).pack(fill=X, pady=(0, 5))
        
        self.entry_username = Entry(
            inner_frame,
            font=("Arial", 13),
            bd=1,
            relief=SOLID,
            highlightthickness=2,
            highlightbackground="#D9D9D9",
            highlightcolor=self.WARNING_COLOR
        )
        self.entry_username.pack(fill=X, ipady=10, pady=(0, 15))
        
        # Email
        Label(
            inner_frame,
            text="Email Address",
            font=("Arial", 12, "bold"),
            bg=self.LIGHT_BG,
            fg=self.TEXT_COLOR,
            anchor=W
        ).pack(fill=X, pady=(0, 5))
        
        self.entry_email = Entry(
            inner_frame,
            font=("Arial", 13),
            bd=1,
            relief=SOLID,
            highlightthickness=2,
            highlightbackground="#D9D9D9",
            highlightcolor=self.WARNING_COLOR
        )
        self.entry_email.pack(fill=X, ipady=10, pady=(0, 15))
        
        # Password
        Label(
            inner_frame,
            text="Password",
            font=("Arial", 12, "bold"),
            bg=self.LIGHT_BG,
            fg=self.TEXT_COLOR,
            anchor=W
        ).pack(fill=X, pady=(0, 5))
        
        self.entry_password = Entry(
            inner_frame,
            font=("Arial", 13),
            show="●",
            bd=1,
            relief=SOLID,
            highlightthickness=2,
            highlightbackground="#D9D9D9",
            highlightcolor=self.WARNING_COLOR
        )
        self.entry_password.pack(fill=X, ipady=10, pady=(0, 25))
        
        # Add Admin Button
        self.btn_add_admin = Button(
            inner_frame,
            text="Add Admin",
            font=("Arial", 14, "bold"),
            bg=self.SUCCESS_COLOR,
            fg="white",
            activebackground="#389E0D",
            activeforeground="white",
            relief=FLAT,
            bd=0,
            cursor="hand2",
            command=self.proses_add_admin
        )
        self.btn_add_admin.pack(fill=X, ipady=12, pady=(0, 10))
        self.btn_add_admin.bind("<Enter>", lambda e: e.widget.config(bg="#389E0D"))
        self.btn_add_admin.bind("<Leave>", lambda e: e.widget.config(bg=self.SUCCESS_COLOR))
        
        # Back Button
        btn_back = Button(
            inner_frame,
            text="← Back to Dashboard",
            font=("Arial", 12),
            bg=self.LIGHT_BG,
            fg=self.SECONDARY_TEXT,
            activebackground=self.GRAY_BG,
            relief=FLAT,
            bd=1,
            cursor="hand2",
            command=self.home_screen_admin
        )
        btn_back.pack(fill=X, ipady=8)
        btn_back.bind("<Enter>", lambda e: e.widget.config(bg=self.GRAY_BG))
        btn_back.bind("<Leave>", lambda e: e.widget.config(bg=self.LIGHT_BG))

    def proses_add_admin(self):


        username = self.entry_username.get()
        email = self.entry_email.get()
        password = self.entry_password.get()
        role = "admin"
        balance = 0

        if not username or not email or not password:
            messagebox.showerror("Error", "All Fields is Required!")
            return


        existed_email = user_services.getUserByEmail(email)
        if existed_email:
            messagebox.showerror("Error", "Email already exists!")
            return

        new_admin = User(username, email, password, role, balance)
        new_admin.register()
        messagebox.showinfo("Success", "New admin added successfully!")
        self.home_screen_admin()

    def view_customers(self):
        self.clear_window()
        
        # Main frame
        main_frame = Frame(self.root, bg=self.GRAY_BG)
        main_frame.pack(fill=BOTH, expand=YES)
        
        # Header dengan warna #4A70A9
        header_frame = Frame(main_frame, bg="#4A70A9", height=100)
        header_frame.pack(fill=X)
        header_frame.pack_propagate(False)
        
        Label(
            header_frame,
            text="Customer Management",
            font=("Arial", 28, "bold"),
            bg="#4A70A9",
            fg="white"
        ).pack(pady=30)
        
        # Content frame
        content_frame = Frame(main_frame, bg=self.LIGHT_BG)
        content_frame.pack(fill=BOTH, expand=True, padx=40, pady=30)
        
        # Back button
        btn_back_frame = Frame(content_frame, bg=self.LIGHT_BG)
        btn_back_frame.pack(fill=X, pady=(0, 15))
        
        btn_back = Button(
            btn_back_frame,
            text="← Back to Dashboard",
            font=("Arial", 12, "bold"),
            bg="#4A70A9",
            fg="white",
            activebackground="#096DD9",
            activeforeground="white",
            relief=FLAT,
            bd=0,
            padx=20,
            pady=10,
            cursor="hand2",
            command=self.home_screen_admin
        )
        btn_back.pack(side=LEFT)
        btn_back.bind("<Enter>", lambda e: e.widget.config(bg="#096DD9"))
        btn_back.bind("<Leave>", lambda e: e.widget.config(bg="#4A70A9"))
        
        # Table container dengan styling
        table_container = Frame(content_frame, bg=self.LIGHT_BG, bd=2, relief=SOLID)
        table_container.pack(fill=BOTH, expand=True)
        
        # Style untuk Treeview
        style = ttk.Style()
        style.configure(
            "Customers.Treeview",
            background="white",
            foreground=self.TEXT_COLOR,
            rowheight=40,
            fieldbackground="white",
            borderwidth=0
        )
        style.configure(
            "Customers.Treeview.Heading",
            background="#4A70A9",
            foreground="white",
            font=("Arial", 11, "bold"),
            borderwidth=0,
            padding=(8, 6)
        )
        style.map(
            "Customers.Treeview",
            background=[("selected", "#4A70A9")],
            foreground=[("selected", "white")]
        )
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(table_container, orient=VERTICAL)
        
        # Treeview
        self.tableCustomers = ttk.Treeview(
            table_container,
            columns=("No", "Username", "Email", "Balance"),
            show="headings",
            style="Customers.Treeview",
            yscrollcommand=scrollbar.set
        )
        
        scrollbar.config(command=self.tableCustomers.yview)
        
        # Column headings
        self.tableCustomers.heading("No", text="ID")
        self.tableCustomers.heading("Username", text="Username")
        self.tableCustomers.heading("Email", text="Email")
        self.tableCustomers.heading("Balance", text="Balance")
        
        # Column widths
        self.tableCustomers.column("No", width=80, anchor="center")
        self.tableCustomers.column("Username", width=200, anchor="center")
        self.tableCustomers.column("Email", width=350, anchor="center")
        self.tableCustomers.column("Balance", width=150, anchor="center")
        
        # Pack table dan scrollbar
        self.tableCustomers.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        self.load_data_customers()

    def load_data_customers(self):
        self.dataCustomers = user_services.getCustomers()
        i = 1

       
        for customer in self.dataCustomers:
            balance = f"Rp{customer[5]:,}".replace(",", ".")
            self.tableCustomers.insert("", "end", values=(i, customer[1], customer[2], balance))
    
    def view_products(self):
        self.clear_window()
        
        # Main frame
        main_frame = Frame(self.root, bg=self.GRAY_BG)
        main_frame.pack(fill=BOTH, expand=YES)
        
        # Header dengan warna #4A70A9
        header_frame = Frame(main_frame, bg="#4A70A9", height=100)
        header_frame.pack(fill=X)
        header_frame.pack_propagate(False)
        
        Label(
            header_frame,
            text="Product Management",
            font=("Arial", 28, "bold"),
            bg="#4A70A9",
            fg="white"
        ).pack(pady=30)
        
        # Content frame
        content_frame = Frame(main_frame, bg=self.LIGHT_BG)
        content_frame.pack(fill=BOTH, expand=True, padx=40, pady=30)
        
        # Button frame at top
        button_top_frame = Frame(content_frame, bg=self.LIGHT_BG)
        button_top_frame.pack(fill=X, pady=(0, 15))
        
        # Back button
        btn_back = Button(
            button_top_frame,
            text="← Back to Dashboard",
            font=("Arial", 12, "bold"),
            bg="#4A70A9",
            fg="white",
            activebackground="#096DD9",
            activeforeground="white",
          
            bd=0,
            padx=20,
            pady=10,
            cursor="hand2",
            command=self.home_screen_admin
        )
        btn_back.pack(side=LEFT)
        btn_back.bind("<Enter>", lambda e: e.widget.config(bg="#096DD9"))
        btn_back.bind("<Leave>", lambda e: e.widget.config(bg="#4A70A9"))
        
        # Action buttons on the right
        action_frame = Frame(button_top_frame, bg=self.LIGHT_BG)
        action_frame.pack(side=RIGHT)
        
        self.btn_add_product = Button(
            action_frame,
            text="Add Product",
            font=("Arial", 11, "bold"),
            bg=self.SUCCESS_COLOR,
            fg="white",
            activebackground="#389E0D",
            activeforeground="white",
            relief=FLAT,
            bd=0,
            padx=15,
            pady=8,
            cursor="hand2",
            command=self.add_product
        )
        self.btn_add_product.pack(side=LEFT, padx=5)
        self.btn_add_product.bind("<Enter>", lambda e: e.widget.config(bg="#389E0D"))
        self.btn_add_product.bind("<Leave>", lambda e: e.widget.config(bg=self.SUCCESS_COLOR))
        
        self.btn_edit = Button(
            action_frame,
            text="Edit Selected",
            font=("Arial", 11, "bold"),
            bg=self.WARNING_COLOR,
            fg="white",
            activebackground="#D46B08",
            activeforeground="white",
            relief=FLAT,
            bd=0,
            padx=15,
            pady=8,
            cursor="hand2",
            command=self.edit_selected_product
        )
        self.btn_edit.pack(side=LEFT, padx=5)
        self.btn_edit.bind("<Enter>", lambda e: e.widget.config(bg="#D46B08"))
        self.btn_edit.bind("<Leave>", lambda e: e.widget.config(bg=self.WARNING_COLOR))
        
        self.btn_delete = Button(
            action_frame,
            text="Delete Selected",
            font=("Arial", 11, "bold"),
            bg=self.DANGER_COLOR,
            fg="white",
            activebackground="#CF1322",
            activeforeground="white",
            relief=FLAT,
            bd=0,
            padx=15,
            pady=8,
            cursor="hand2",
            command=self.delete_selected_product
        )
        self.btn_delete.pack(side=LEFT, padx=5)
        self.btn_delete.bind("<Enter>", lambda e: e.widget.config(bg="#CF1322"))
        self.btn_delete.bind("<Leave>", lambda e: e.widget.config(bg=self.DANGER_COLOR))
        
        # Table container dengan styling
        table_container = Frame(content_frame, bg=self.LIGHT_BG, bd=2, relief=SOLID)
        table_container.pack(fill=BOTH, expand=True)
        
        # Style untuk Treeview
        style = ttk.Style()
        style.configure(
            "Products.Treeview",
            background="white",
            foreground=self.TEXT_COLOR,
            rowheight=70,
            fieldbackground="white",
            borderwidth=0
        )
        style.configure(
            "Products.Treeview.Heading",
            background="#4A70A9",
            foreground="white",
            font=("Arial", 11, "bold"),
            borderwidth=0,
            padding=(8, 6)
        )
        style.map(
            "Products.Treeview",
            background=[("selected", "#4A70A9")],
            foreground=[("selected", "white")]
        )
        
        # Scrollbar
        scrollbar_y = ttk.Scrollbar(table_container, orient=VERTICAL)
        
        # Treeview
        self.table = ttk.Treeview(
            table_container,
            columns=("id", "View", "Name", "Description", "Price", "Stock"),
            show="headings",
            style="Products.Treeview",
            yscrollcommand=scrollbar_y.set
        )
        
        scrollbar_y.config(command=self.table.yview)
        
        # Column headings
        self.table.heading("id", text="ID")
        self.table.heading("View", text="Image")
        self.table.heading("Name", text="Product Name")
        self.table.heading("Description", text="Description")
        self.table.heading("Price", text="Price")
        self.table.heading("Stock", text="Stock")
        
        # Column widths
        self.table.column("id", width=50, anchor="center")
        self.table.column("View", width=70, anchor="center")
        self.table.column("Name", width=150, anchor="center")
        self.table.column("Description", width=300, anchor="center")
        self.table.column("Price", width=100, anchor="center")
        self.table.column("Stock", width=100, anchor="center")
        
        self.table.bind("<ButtonRelease-1>", self.on_table_click)
        
        # Pack table dan scrollbar
        self.table.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar_y.pack(side=RIGHT, fill=Y)
        
        self.image_refs = []
        self.load_table_data()

    def load_table_data(self):
        self.products = product_services.fetchProductById(self.userId)
        # self.btn_delete = ttk.Button(self.root, text="Delete Selected Product", command=lambda: self.delete_selected_product(id))
   
        self.image_urls = {}
        for product in self.products:
            
            price = f"Rp {product[4]:,}".replace(",", ".")
           
            self.table.insert("", "end",  values=(product[0], "View", product[1], product[2], price, product[5]))

            self.image_urls[product[0]] = product[3]

      

    def on_table_click(self, event):
        region = self.table.identify("region", event.x, event.y)

        if region == "cell":
            column = self.table.identify_column(event.x)
            row_id = self.table.identify_row(event.y)

            # Kolom ke-2 (View)
            if column == "#2":
                item = self.table.item(row_id)
                values = item["values"]

                product_id = values[0]
                image_url = self.image_urls.get(product_id)

                if image_url:
                    self.pop_up_image(image_url)


    def pop_up_image(self, image_url):
        top = Toplevel(self.root)
        top.title("Product Image")
        top.geometry("400x400")

        response = requests.get(image_url)
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        img = img.resize((400, 400))
        photo = ImageTk.PhotoImage(img)
        self.image_refs.append(photo)

        label = Label(top, image=photo)
        label.image = photo  # Simpan referensi gambar untuk mencegah garbage collection
        label.pack()
    
    def add_product(self):
        self.clear_window()
        
        # Main frame
        main_frame = Frame(self.root, bg=self.GRAY_BG)
        main_frame.pack(fill=BOTH, expand=YES)
        
        # Header dengan warna #4A70A9
        header_frame = Frame(main_frame, bg="#4A70A9", height=100)
        header_frame.pack(fill=X)
        header_frame.pack_propagate(False)
        
        Label(
            header_frame,
            text="Add New Product",
            font=("Arial", 28, "bold"),
            bg="#4A70A9",
            fg="white"
        ).pack(pady=10)
        
        # Content frame
        content_frame = Frame(main_frame, bg=self.LIGHT_BG, width=400, height=800)
        content_frame.pack(pady=10, padx=200)
        content_frame.pack_propagate(False)
        
        inner_frame = Frame(content_frame, bg=self.LIGHT_BG, width=300, height=700)
        inner_frame.pack(padx=30, pady=20)
        inner_frame.pack_propagate(False)
        
        # Product Name
        Label(
            inner_frame,
            text="Product Name",
            font=("Arial", 12, "bold"),
            bg=self.LIGHT_BG,
            fg=self.TEXT_COLOR,
            anchor=W
        ).pack(fill=X, pady=(0, 5))
        
        self.entry_name = Entry(
            inner_frame,
            font=("Arial", 13),
            bd=1,
            relief=SOLID,
            highlightthickness=2,
            highlightbackground="#D9D9D9",
            highlightcolor="#4A70A9"
        )
        self.entry_name.pack(fill=X, ipady=7, pady=(0, 5))
        
        # Description
        Label(
            inner_frame,
            text="Description",
            font=("Arial", 12, "bold"),
            bg=self.LIGHT_BG,
            fg=self.TEXT_COLOR,
            anchor=W
        ).pack(fill=X, pady=(0, 5))
        
        self.entry_description = Entry(
            inner_frame,
            font=("Arial", 13),
            bd=1,
            relief=SOLID,
            highlightthickness=2,
            highlightbackground="#D9D9D9",
            highlightcolor="#4A70A9"
        )
        self.entry_description.pack(fill=X, ipady=7, pady=(0, 5))
        
        # Image URL
        Label(
            inner_frame,
            text="Image URL",
            font=("Arial", 12, "bold"),
            bg=self.LIGHT_BG,
            fg=self.TEXT_COLOR,
            anchor=W
        ).pack(fill=X, pady=(0, 5))
        
        self.entry_image_url = Entry(
            inner_frame,
            font=("Arial", 13),
            bd=1,
            relief=SOLID,
            highlightthickness=2,
            highlightbackground="#D9D9D9",
            highlightcolor="#4A70A9"
        )
        self.entry_image_url.pack(fill=X, ipady=7, pady=(0, 5))
        
        # Price
        Label(
            inner_frame,
            text="Price (Rp)",
            font=("Arial", 12, "bold"),
            bg=self.LIGHT_BG,
            fg=self.TEXT_COLOR,
            anchor=W
        ).pack(fill=X, pady=(0, 5))
        
        self.entry_price = Entry(
            inner_frame,
            font=("Arial", 13),
            bd=1,
            relief=SOLID,
            highlightthickness=2,
            highlightbackground="#D9D9D9",
            highlightcolor="#4A70A9"
        )
        self.entry_price.pack(fill=X, ipady=7, pady=(0, 5))
        
        # Stock
        Label(
            inner_frame,
            text="Stock Quantity",
            font=("Arial", 12, "bold"),
            bg=self.LIGHT_BG,
            fg=self.TEXT_COLOR,
            anchor=W
        ).pack(fill=X, pady=(0, 5))
        
        self.entry_stock = Entry(
            inner_frame,
            font=("Arial", 13),
            bd=1,
            relief=SOLID,
            highlightthickness=2,
            highlightbackground="#D9D9D9",
            highlightcolor="#4A70A9"
        )
        self.entry_stock.pack(fill=X, ipady=7, pady=(5, 5))
        
        # Add Product Button
        self.btn_add_product = Button(
            inner_frame,
            text="Add Product",
            font=("Arial", 14, "bold"),
            bg=self.SUCCESS_COLOR,
            fg="white",
            activebackground="#389E0D",
            activeforeground="white",
            relief=FLAT,
            bd=0,
            cursor="hand2",
            command=self.proses_add_product
        )
        self.btn_add_product.pack(fill=X, ipady=7, pady=(0, 10))
        self.btn_add_product.bind("<Enter>", lambda e: e.widget.config(bg="#389E0D"))
        self.btn_add_product.bind("<Leave>", lambda e: e.widget.config(bg=self.SUCCESS_COLOR))
        
        # Back Button
        btn_back = Button(
            inner_frame,
            text="← Back to Products",
            font=("Arial", 12),
            bg=self.LIGHT_BG,
            fg=self.SECONDARY_TEXT,
            activebackground=self.GRAY_BG,
            relief=FLAT,
            bd=1,
            cursor="hand2",
            command=self.view_products
        )
        btn_back.pack(fill=X, ipady=8)
        btn_back.bind("<Enter>", lambda e: e.widget.config(bg=self.GRAY_BG))
        btn_back.bind("<Leave>", lambda e: e.widget.config(bg=self.LIGHT_BG))

    def proses_add_product(self):
        if not self.entry_name.get() or not self.entry_description.get() or not self.entry_image_url.get() or self.entry_price.get() == "" or self.entry_stock.get() == "":
            messagebox.showerror("Error", "All Field is Required!")
            return
        
        
        try:
            price = int(self.entry_price.get())
        except ValueError:
            messagebox.showerror("Error", "Price must be a number")
            return


        try:
            stock = int(self.entry_stock.get())
        except ValueError:
            messagebox.showerror("Error", "Stock must be a number")
            return
        
        if int(self.entry_price.get()) < 1:
            messagebox.showerror("Error", "Price Must Greater than 0")
            return
        
        if int(self.entry_stock.get()) < 1:
            messagebox.showerror("Error", "Stock Must Greater than 0")
            return
        
        

        name = self.entry_name.get()
        description = self.entry_description.get()
        image = self.entry_image_url.get()
        price = int(self.entry_price.get())
        stock = int(self.entry_stock.get())

        

        Product(name, description, image, price, stock, self.userId).insertProduct()
        messagebox.showinfo("Success", "Product added successfully!")

        self.view_products()
       
   


   

    def get_selected_product(self):
        selected_item = self.table.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No product selected!")
            return None
       
        product_values = self.table.item(selected_item)["values"]

        image = self.image_urls[product_values[0]]
        
        return product_values, image
    

    
    def delete_selected_product(self):
        product_values, image = self.get_selected_product()
  
        if product_values:
            product_id = product_values[0]
            confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{product_values[1]}'?")
            if confirm:
                product = Product("", "","", 0, 0, 0)
                product.deleteProduct(product_id)
                messagebox.showinfo("Success", "Product deleted successfully!")
                self.view_products()

    def edit_selected_product(self):
        product_values, image = self.get_selected_product()

        
        if product_values:
            self.clear_window()
            
            # Main frame
            main_frame = Frame(self.root, bg=self.GRAY_BG)
            main_frame.pack(fill=BOTH, expand=YES)
            
            # Header dengan warna #4A70A9
            header_frame = Frame(main_frame, bg="#4A70A9", height=100)
            header_frame.pack(fill=X)
            header_frame.pack_propagate(False)
            
            Label(
                header_frame,
                text="Edit Product",
                font=("Arial", 28, "bold"),
                bg="#4A70A9",
                fg="white"
            ).pack(pady=30)
            
            # Content frame
            content_frame = Frame(main_frame, bg=self.LIGHT_BG, width=400, height=800)
            content_frame.pack(pady=10, padx=200)
            content_frame.pack_propagate(False)
            
            inner_frame = Frame(content_frame, bg=self.LIGHT_BG, width=300, height=700)
            inner_frame.pack(padx=30, pady=20)
            inner_frame.pack_propagate(False)
                
            # Product Name
            Label(
                inner_frame,
                text="Product Name",
                font=("Arial", 12, "bold"),
                bg=self.LIGHT_BG,
                fg=self.TEXT_COLOR,
                anchor=W
            ).pack(fill=X, pady=(0, 5))
            
            self.entry_name = Entry(
                inner_frame,
                font=("Arial", 13),
                bd=1,
                relief=SOLID,
                highlightthickness=2,
                highlightbackground="#D9D9D9",
                highlightcolor="#4A70A9"
            )
            self.entry_name.insert(0, product_values[2])
            self.entry_name.pack(fill=X, ipady=7, pady=(0, 7))
            
            # Description
            Label(
                inner_frame,
                text="Description",
                font=("Arial", 12, "bold"),
                bg=self.LIGHT_BG,
                fg=self.TEXT_COLOR,
                anchor=W
            ).pack(fill=X, pady=(0, 5))
            
            self.entry_description = Entry(
                inner_frame,
                font=("Arial", 13),
                bd=1,
                relief=SOLID,
                highlightthickness=2,
                highlightbackground="#D9D9D9",
                highlightcolor="#4A70A9"
            )
            self.entry_description.insert(0, product_values[3])
            self.entry_description.pack(fill=X, ipady=7, pady=(0, 7))
            
            # Image URL
            Label(
                inner_frame,
                text="Image URL",
                font=("Arial", 12, "bold"),
                bg=self.LIGHT_BG,
                fg=self.TEXT_COLOR,
                anchor=W
            ).pack(fill=X, pady=(0, 5))
            
            self.entry_image_url = Entry(
                inner_frame,
                font=("Arial", 13),
                bd=1,
                relief=SOLID,
                highlightthickness=2,
                highlightbackground="#D9D9D9",
                highlightcolor="#4A70A9"
            )
            self.entry_image_url.insert(0, image)
            self.entry_image_url.pack(fill=X, ipady=7, pady=(0, 7))
            
            # Price
            Label(
                inner_frame,
                text="Price (Rp)",
                font=("Arial", 12, "bold"),
                bg=self.LIGHT_BG,
                fg=self.TEXT_COLOR,
                anchor=W
            ).pack(fill=X, pady=(0, 5))
            
            self.entry_price = Entry(
                inner_frame,
                font=("Arial", 13),
                bd=1,
                relief=SOLID,
                highlightthickness=2,
                highlightbackground="#D9D9D9",
                highlightcolor="#4A70A9"
            )
            self.entry_price.insert(0, product_values[4].replace("Rp", "").replace(".", ""))
            self.entry_price.pack(fill=X, ipady=7, pady=(0, 7))
            
            # Stock
            Label(
                inner_frame,
                text="Stock Quantity",
                font=("Arial", 12, "bold"),
                bg=self.LIGHT_BG,
                fg=self.TEXT_COLOR,
                anchor=W
            ).pack(fill=X, pady=(0, 5))
            
            self.entry_stock = Entry(
                inner_frame,
                font=("Arial", 13),
                bd=1,
                relief=SOLID,
                highlightthickness=2,
                highlightbackground="#D9D9D9",
                highlightcolor="#4A70A9"
            )
            self.entry_stock.insert(0, product_values[5])
            self.entry_stock.pack(fill=X, ipady=7, pady=(0, 25))
            
            # Update Product Button
            self.btn_update_product = Button(
                inner_frame,
                text="Update Product",
                font=("Arial", 14, "bold"),
                bg=self.WARNING_COLOR,
                fg="white",
                activebackground="#D46B08",
                activeforeground="white",
                relief=FLAT,
                bd=0,
                cursor="hand2",
                command=lambda: self.proses_update_product(int(product_values[0]))
            )
            self.btn_update_product.pack(fill=X, ipady=7, pady=(0, 5))
            self.btn_update_product.bind("<Enter>", lambda e: e.widget.config(bg="#D46B08"))
            self.btn_update_product.bind("<Leave>", lambda e: e.widget.config(bg=self.WARNING_COLOR))
            
            # Back Button
            btn_back = Button(
                inner_frame,
                text="← Back to Products",
                font=("Arial", 12),
                bg=self.LIGHT_BG,
                fg=self.SECONDARY_TEXT,
                activebackground=self.GRAY_BG,
                relief=FLAT,
                bd=1,
                cursor="hand2",
                command=self.view_products
            )
            btn_back.pack(fill=X, ipady=8, pady=5)
            btn_back.bind("<Enter>", lambda e: e.widget.config(bg=self.GRAY_BG))
            btn_back.bind("<Leave>", lambda e: e.widget.config(bg=self.LIGHT_BG))

    def proses_update_product(self, id):
        if not self.entry_name.get() or not self.entry_description.get() or not self.entry_image_url.get() or self.entry_price.get() == "" or self.entry_stock.get() == "":
            messagebox.showerror("Error", "All Field is Required!")
            return
        
        
        try:
            price = int(self.entry_price.get())
        except ValueError:
            messagebox.showerror("Error", "Price must be a number")
            return


        try:
            stock = int(self.entry_stock.get())
        except ValueError:
            messagebox.showerror("Error", "Stock must be a number")
            return
        
        if int(self.entry_price.get()) < 1:
            messagebox.showerror("Error", "Price Must Greater than 0")
            return
        
        if int(self.entry_stock.get()) < 1:
            messagebox.showerror("Error", "Stock Must Greater than 0")
            return

        name = self.entry_name.get()
        description = self.entry_description.get()
        image_url = self.entry_image_url.get()
        price = int(self.entry_price.get())
        stock = int(self.entry_stock.get())

        product = Product(name, description, image_url, price, stock, self.userId)
        product.updateProduct(id)
        messagebox.showinfo("Success", "Product updated successfully!")

        self.view_products()

    

    def home_screen_customer(self):
        self.clear_window()
        header = Frame(self.root, bg="#4A70A9", height=60)
        header.pack(fill=X)

        # ===== Frame Header =====
        header_left = Frame(header, bg="#4A70A9")
        header_left.pack(side=LEFT, fill=Y)

        header_center = Frame(header, bg="#4A70A9")
        header_center.pack(side=LEFT, expand=True)

        header_right = Frame(header, bg="#4A70A9")
        header_right.pack(side=RIGHT, fill=Y)

        # ===== ISI KIRI =====
        Label(
            header_left,
            text="Elektronikku",
            font=("Arial", 22, "bold"),
            bg="#4A70A9",
            fg="white"
        ).pack(padx=10, pady=10)

        # ===== ISI TENGAH =====
        Label(
            header_center,
            text="Smart Choice for Smart Life",
            font=("Arial", 16, "italic"),
            bg="#4A70A9",
            fg="white"
        ).pack(expand=True)

        # ===== ISI KANAN =====

        self.balance = user_services.getUserById(self.current_customer_id)[5]

        Label(
            header_right,
            text=f"Balance: Rp{self.balance:,}",
            font=("Arial", 14, "bold"),
            bg="#4A70A9",
            fg="white"
        ).pack(side=LEFT, padx=10, pady=10)

        ttk.Button(
            header_right,
            text="Cart",
            command=self.view_cart
        ).pack(side=RIGHT, padx=10, pady=10)

        body = Frame(root)
        body.pack(fill="both", expand=True)

        sidebar = Frame(body, width=250, bg="#4A70A9")
        sidebar.pack(side="left", fill="y")

        product_area = Frame(body, bg="white")
        product_area.pack(side="right", fill="both", expand=True)

        Button(sidebar,
           text="Profile",
           font=("Arial", 14, "bold"),
           bg="#69a7a7",
           fg="black",
           height=2, command=self.show_profile).pack(fill="x", padx=10, pady=20)
        
        Button(sidebar,
           text="Add Balance",
           font=("Arial", 14, "bold"),
           bg="#69a7a7",
           fg="black",
           height=2,
           command=self.add_balance).pack(fill="x", padx=10, pady=20)
        
        Button(sidebar,
           text="History",
           font=("Arial", 14, "bold"),
           bg="#69a7a7",
           fg="black",
           height=2,
           command=self.view_history
           ).pack(fill="x", padx=10, pady=20)
        
        Button(
            sidebar,
            text="Logout",
            font=("Arial", 14, "bold"),
            bg="#69a7a7",
            fg="black",
            command=self.logout
        ).pack(side=BOTTOM, fill="x", padx=10, pady=20)

        canvas = Canvas(product_area)
        scrollbar = Scrollbar(product_area, orient="vertical", command=canvas.yview)

        scrollable_frame = Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.products = product_services.fetchProducts()

        row, col = 0, 0
        for product in self.products:
            
            
            seller = user_services.getUserById(product[6])
            

            card = self.create_product_card(scrollable_frame,
                                        product[3],
                                        product[1],
                                        product[4],
                                        product[5],
                                        seller
                                        )
            card.grid(row=row, column=col, padx=20, pady=20)


            col += 1
            if col == 4:
                col = 0
                row += 1

    def view_history(self):
        self.clear_window()
        
        # Main frame
        main_frame = Frame(self.root, bg=self.GRAY_BG)
        main_frame.pack(fill=BOTH, expand=YES)
        
        # Header dengan warna #4A70A9
        header_frame = Frame(main_frame, bg="#4A70A9", height=100)
        header_frame.pack(fill=X)
        header_frame.pack_propagate(False)
        
        Label(
            header_frame,
            text="Purchase History",
            font=("Arial", 28, "bold"),
            bg="#4A70A9",
            fg="white"
        ).pack(pady=30)
        
        # Content frame
        content_frame = Frame(main_frame, bg=self.LIGHT_BG)
        content_frame.pack(fill=BOTH, expand=True, padx=10, pady=30)
        
        # Back button
        btn_back_frame = Frame(content_frame, bg=self.LIGHT_BG)
        btn_back_frame.pack(fill=X, pady=(0, 10))
        
        btn_back = Button(
            btn_back_frame,
            text="← Back to Home",
            font=("Arial", 12, "bold"),
            bg="#4A70A9",
            fg="white",
            activebackground="#096DD9",
            activeforeground="white",
            relief=FLAT,
            bd=0,
            padx=20,
            pady=10,
            cursor="hand2",
            command=self.home_screen_customer
        )
        btn_back.pack(side=LEFT)
        btn_back.bind("<Enter>", lambda e: e.widget.config(bg="#096DD9"))
        btn_back.bind("<Leave>", lambda e: e.widget.config(bg="#4A70A9"))
        
        # Table frame dengan styling
        table_container = Frame(content_frame, bg=self.LIGHT_BG, bd=2, relief=SOLID)
        table_container.pack(fill=BOTH, expand=True)
        
        # Style untuk Treeview
        style = ttk.Style()
        style.configure(
            "History.Treeview",
            background="white",
            foreground=self.TEXT_COLOR,
            rowheight=35,
            fieldbackground="white",
            borderwidth=0
        )
        style.configure(
            "History.Treeview.Heading",
            background="#4A70A9",
            foreground="black",
            font=("Arial", 11, "bold"),
            borderwidth=0
        )
        style.map(
            "History.Treeview",
            background=[("selected", "#4A70A9")],
            foreground=[("selected", "white")]
        )
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(table_container, orient=VERTICAL)
        
        # Treeview
        self.tableHistory = ttk.Treeview(
            table_container,
            columns=("CartID", "Datetime", "Total Price", "View Details"),
            show="headings",
            style="History.Treeview",
            yscrollcommand=scrollbar.set
        )
        
        scrollbar.config(command=self.tableHistory.yview)
        
        # Column headings
        self.tableHistory.heading("CartID", text="Cart ID")
        self.tableHistory.heading("Datetime", text="Datetime")
        self.tableHistory.heading("Total Price", text="Total Price")
        self.tableHistory.heading("View Details", text="View Details")
        
        # Column widths
        self.tableHistory.column("CartID", width=80, anchor="center")
        self.tableHistory.column("Datetime", width=200, anchor="center")
        self.tableHistory.column("Total Price", width=200, anchor="center")
        self.tableHistory.column("View Details", width=150, anchor="center")
        
        # Pack table dan scrollbar
        self.tableHistory.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.tableHistory.bind("<ButtonRelease-1>", self.on_table_click_history)
        
        self.load_data_history()

    def load_data_history(self):
        self.dataHistory = cart_services.getCartAndCartDetailsCustomer(self.current_customer_id)

        for history in self.dataHistory:
            self.tableHistory.insert("", "end", values=(history[0], history[1], f"Rp{history[2]:,}", "View Details"))
            
    def on_table_click_history(self, event):
        region = self.tableHistory.identify("region", event.x, event.y)

        if region == "cell":
            column = self.tableHistory.identify_column(event.x)
            row_id = self.tableHistory.identify_row(event.y)

            # Kolom ke-4 (View Details)
            if column == "#4":
                item = self.tableHistory.item(row_id)
                values = item["values"]

                cart_id = values[0]

                self.view_history_details(cart_id)

    def view_history_details(self, cart_id):
        details = cart_detail_service.fetchCartDetailsByCartId(cart_id)
        
        detail_window = Toplevel(self.root)
        detail_window.title(f"Cart Details - ID: {cart_id}")
        detail_window.geometry("800x600")
        detail_window.configure(bg=self.GRAY_BG)
        
        # Header frame
        header_frame = Frame(detail_window, bg="#4A70A9", height=80)
        header_frame.pack(fill=X)
        header_frame.pack_propagate(False)
        
        Label(
            header_frame,
            text=f"Cart Details - ID: {cart_id}",
            font=("Arial", 24, "bold"),
            bg="#4A70A9",
            fg="white"
        ).pack(pady=25)
        
  
        content_frame = Frame(detail_window, bg=self.LIGHT_BG)
        content_frame.pack(fill=BOTH, expand=True, padx=30, pady=20)
        
 
        table_container = Frame(content_frame, bg=self.LIGHT_BG, bd=2, relief=SOLID)
        table_container.pack(fill=BOTH, expand=True)
        
  
        style = ttk.Style()
        style.configure(
            "Details.Treeview",
            background="white",
            foreground=self.TEXT_COLOR,
            rowheight=110,
            fieldbackground="white",
            borderwidth=0
        )
        style.configure(
            "Details.Treeview.Heading",
            background="#4A70A9",
            foreground="black",
            font=("Arial", 11, "bold"),
            borderwidth=0,
            padding=(8, 6)
        )
        style.map(
            "Details.Treeview",
            background=[("selected", "#4A70A9")],
            foreground=[("selected", "white")]
        )
        
    
        scrollbar = ttk.Scrollbar(table_container, orient=VERTICAL)
        

        tree = ttk.Treeview(
            table_container,
            columns=("Name", "Quantity", "Price"),
            show="tree headings",
            style="Details.Treeview",
            yscrollcommand=scrollbar.set
        )
        
        scrollbar.config(command=tree.yview)
        
        tree.heading("#0", text="Image")
        
        tree.heading("Name", text="Product Name")
        tree.heading("Quantity", text="Quantity")
        tree.heading("Price", text="Price")
        
        tree.column("#0", width=120, anchor="center")
        
        tree.column("Name", width=250, anchor="center")
        tree.column("Quantity", width=120, anchor="center")
        tree.column("Price", width=150, anchor="center")
        
        self.history_images = []
       
        for detail in details:
            
            img_url = detail[5]
            response = requests.get(img_url)
            img_data = Image.open(BytesIO(response.content))

     
            img_data = img_data.resize((100, 100))

            img = ImageTk.PhotoImage(img_data)

            self.history_images.append(img)
        
            tree.insert("", "end", image=img, values=(detail[1], detail[3], f"Rp{detail[2]:,}"))
            

      
        tree.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)
        

        btn_frame = Frame(detail_window, bg=self.LIGHT_BG)
        btn_frame.pack(fill=X, padx=30, pady=(0, 20))
        
        btn_close = Button(
            btn_frame,
            text="✕ Close",
            font=("Arial", 12, "bold"),
            bg=self.DANGER_COLOR,
            fg="white",
            activebackground="#CF1322",
            activeforeground="white",
            relief=FLAT,
            bd=0,
            padx=30,
            pady=10,
            cursor="hand2",
            command=detail_window.destroy
        )
        btn_close.pack()
        btn_close.bind("<Enter>", lambda e: e.widget.config(bg="#CF1322"))
        btn_close.bind("<Leave>", lambda e: e.widget.config(bg=self.DANGER_COLOR))
        

    def add_to_cart_process(self, sellerId, name, price, image_url):
        checkCart = cart_services.checkCartActive(self.current_customer_id, sellerId)

        if not checkCart:
            cart_services.createCart(self.current_customer_id, sellerId)
            

        self.cartId = cart_services.getCartByUserAndSeller(self.current_customer_id, sellerId)
   

       
        product_in_cart = cart_detail_service.checkProductInCart(self.cartId[0], name)
        

        if product_in_cart:
            cart_detail_service.increaseQuantity(self.cartId[0], name)
        else:
            
            cartDetail = CartDetail(
                quantity=1,
                name=name,
                price=price,
                cartId=self.cartId[0],
                image_url=image_url
            )
            cartDetail.insertCartDetail()
        
        
        messagebox.showinfo("Success", "Successfully Add to Cart!")

             

    def view_cart(self):
        self.clear_window()
        
        # Header Cart dengan styling menarik
        header_cart = Frame(self.root, bg="#4A70A9", height=80)
        header_cart.pack(fill=X)
        header_cart.pack_propagate(False)

        
        Label(
            header_cart,
            text="My Shopping Cart",
            font=("Arial", 24, "bold"),
            bg="#4A70A9",
            fg="white"
        ).pack(pady=20)

       
       
        # Button Back dengan styling
        btn_back_frame = Frame(self.root, bg="#f5f5f5")
        btn_back_frame.pack(fill=X, pady=10)
        
        self.btn_back = ttk.Button(
            btn_back_frame, 
            text="← Back to Home", 
            command=self.home_screen_customer
        )
        self.btn_back.pack(pady=5)
        
        self.fetch_cart_id = cart_services.getCartByUserId(self.current_customer_id)
 
        
        self.fetch_cart = cart_detail_service.fetchCartDetailsByCartId(self.fetch_cart_id[0]) if self.fetch_cart_id[0] else None
        
        if not self.fetch_cart:
            # Empty cart design yang menarik
            empty_frame = Frame(self.root, bg="white")
            empty_frame.pack(fill="both", expand=True)
            
            Label(
                empty_frame,
                text="🛒",
                font=("Arial", 100),
                bg="white"
            ).pack(pady=50)
            
            Label(
                empty_frame,
                text="Your cart is empty",
                font=("Arial", 20, "bold"),
                bg="white",
                fg="#666"
            ).pack()
            
            Label(
                empty_frame,
                text="Add some products to get started!",
                font=("Arial", 14),
                bg="white",
                fg="#999"
            ).pack(pady=10)
        
        else:
         
            self.cart_detail_info = cart_detail_service.fetchCartDetailsByCartId(self.fetch_cart_id[0])
            
            # Main container dengan background
            main_container = Frame(self.root, bg="#f5f5f5")
            main_container.pack(fill="both", expand=True)
            
            # Cart content frame dengan padding untuk centering
            content_frame = Frame(main_container, bg="#f5f5f5")
            content_frame.pack(fill="both", expand=True, padx=50, pady=20)
            
            # Canvas dan Scrollbar dengan center alignment
            self.canvas_cart = Canvas(content_frame, bg="#f5f5f5", highlightthickness=0)
            self.scrollbar_cart = Scrollbar(content_frame, orient="vertical", command=self.canvas_cart.yview)
            self.scrollable_cart_frame = Frame(self.canvas_cart, bg="#f5f5f5")

            def center_window(event=None):
                self.canvas_cart.configure(scrollregion=self.canvas_cart.bbox("all"))
                canvas_width = self.canvas_cart.winfo_width()

               
                self.canvas_cart.itemconfig(self.cart_window_id, width=canvas_width)

            self.scrollable_cart_frame.bind("<Configure>", center_window)

            self.cart_window_id = self.canvas_cart.create_window((0, 0), window=self.scrollable_cart_frame, anchor="n")
            self.canvas_cart.configure(yscrollcommand=self.scrollbar_cart.set)

            self.canvas_cart.pack(side="left", fill="both", expand=True)
            self.scrollbar_cart.pack(side="right", fill="y")
            
            # Bind canvas resize untuk re-center
            
            self.scrollable_cart_frame.bind("<Configure>", center_window)
            self.canvas_cart.bind("<Configure>", center_window)

            self.total = self.render_cart()

            # Footer dengan total dan checkout yang menarik
            footer_frame = Frame(self.root, bg="white", bd=1, relief="solid")
            footer_frame.pack(fill=X, pady=10, padx=50)
            
            # Total price container
            total_container = Frame(footer_frame, bg="white")
            total_container.pack(pady=10)
            
            Label(
                total_container,
                text=f"Balance: Rp{self.balance:,}",
                font=("Arial", 22, "bold"),
                bg="white",
                fg="black",
            ).pack(pady=10)
            
            Label(
                total_container,
                text="Total Amount:",
                font=("Arial", 16),
                bg="white",
                fg="#666"
            ).pack(side=LEFT, padx=10)
            
            self.total_label = Label(
                total_container,
                text=f"Rp {self.total:,}",
                font=("Arial", 22, "bold"),
                bg="white",
                fg="#1976d2"
            )
            self.total_label.pack(side=LEFT)
            
            # Checkout button dengan styling modern
            checkout_btn = Button(
                footer_frame,
                text="Proceed to Checkout",
                font=("Arial", 14, "bold"),
                bg="#4A70A9",
                fg="white",
                relief="flat",
                padx=30,
                pady=7,
                cursor="hand2",
                command=lambda: self.checkout(self.current_customer_id)
            )
            checkout_btn.pack(pady=10)



    def render_cart(self):
        for widget in self.scrollable_cart_frame.winfo_children():
            widget.destroy()


        total_all = 0
      
        for item in self.fetch_cart:

            cartId = item[4]
            transactionDate = cart_services.getCartById(cartId)
  
            if transactionDate[0][0] == None:
                name = item[1]
                price = item[2]
                quantity = item[3]
                image_url = item[5]

                subtotal = price * quantity
                total_all += subtotal

                # Card wrapper untuk centering
                card_wrapper = Frame(self.scrollable_cart_frame, bg="#f5f5f5")
                card_wrapper.pack(pady=8, fill=X)
                
                # Card dengan styling menarik dan center
                card = Frame(card_wrapper, bd=2, relief="solid", bg="white", height=120, width=800)
                card.pack(anchor="center")
                card.pack_propagate(False)
                
                # Grid configuration untuk layout yang rapi
                card.grid_columnconfigure(1, weight=1)

                # Image frame dengan ukuran tetap
                img_frame = Frame(card, bg="white", width=100, height=100)
                img_frame.grid(row=0, column=0, rowspan=3, padx=15, pady=10, sticky="w")
                img_frame.pack_propagate(False)
                
                try:
                    response = requests.get(image_url)
                    img = Image.open(BytesIO(response.content))
                    # Gunakan ImageOps.fit untuk crop yang tepat
                    img = ImageOps.fit(img, (90, 90), Image.LANCZOS)
                    photo = ImageTk.PhotoImage(img)

                    if not hasattr(self, "image_refs"):
                        self.image_refs = []
                    self.image_refs.append(photo)

                    img_label = Label(img_frame, image=photo, bg="white", bd=1, relief="solid")
                    img_label.pack(expand=True)
                except:
                    placeholder = Label(
                        img_frame, 
                        text="📷\nNo Image", 
                        bg="#f0f0f0", 
                        font=("Arial", 10),
                        justify="center",
                        bd=1,
                        relief="solid"
                    )
                    placeholder.pack(expand=True)

                # Product info frame dengan styling yang lebih baik
                info_frame = Frame(card, bg="white")
                info_frame.grid(row=0, column=1, rowspan=3, sticky="ew", padx=15)
                
                Label(
                    info_frame, 
                    text=name, 
                    font=("Arial", 14, "bold"), 
                    bg="white", 
                    fg="#333",
                    anchor="w"
                ).pack(anchor="w", pady=(5, 2))
                
                Label(
                    info_frame, 
                    text=f"Unit Price: Rp {price:,}", 
                    font=("Arial", 11), 
                    bg="white", 
                    fg="#666",
                    anchor="w"
                ).pack(anchor="w")
                
                Label(
                    info_frame, 
                    text=f"Subtotal: Rp {subtotal:,}", 
                    font=("Arial", 12, "bold"), 
                    bg="white", 
                    fg="#2e7d32",
                    anchor="w"
                ).pack(anchor="w", pady=(2, 5))

                # Quantity controls dengan styling modern
                qty_frame = Frame(card, bg="white")
                qty_frame.grid(row=0, column=2, rowspan=3, padx=15)
                
                Label(qty_frame, text="Quantity", font=("Arial", 9), bg="white", fg="#666").pack()
                
                qty_control = Frame(qty_frame, bg="white")
                qty_control.pack(pady=5)
                
                btn_decrease = Button(
                    qty_control, 
                    text="−", 
                    font=("Arial", 12, "bold"), 
                    width=2,
                    bg="#f0f0f0",
                    fg="#333",
                    relief="flat",
                    cursor="hand2",
                    command=lambda n=name: self.decrease_qty(n)
                )
                btn_decrease.pack(side="left", padx=2)
                
                qty_display = Label(
                    qty_control, 
                    text=str(quantity), 
                    width=3, 
                    font=("Arial", 12, "bold"), 
                    bg="white", 
                    bd=1, 
                    relief="solid"
                )
                qty_display.pack(side="left", padx=2)
                
                btn_increase = Button(
                    qty_control, 
                    text="+", 
                    font=("Arial", 12, "bold"), 
                    width=2,
                    bg="#4A70A9",
                    fg="white",
                    relief="flat",
                    cursor="hand2",
                    command=lambda n=name: self.increase_qty(n)
                )
                btn_increase.pack(side="left", padx=2)

                # Remove button dengan styling modern
                remove_btn = Button(
                    card, 
                    text="Remove", 
                    font=("Arial", 10, "bold"), 
                    fg="white", 
                    bg="#e53935", 
                    relief="flat",
                    cursor="hand2",
                    command=lambda n=name: self.remove_item(n)
                )
                remove_btn.grid(row=0, column=3, rowspan=3, padx=15, pady=10, sticky="e")
            
        return total_all
            
    def increase_qty(self, name):
        cart_detail_service.increaseQuantity(self.fetch_cart_id[0], name)
        self.fetch_cart = cart_detail_service.fetchCartDetailsByCartId(self.fetch_cart_id[0])
        
        # Clear old widgets
        for widget in self.scrollable_cart_frame.winfo_children():
            widget.destroy()
        
        # Re-render and get new total
        self.total = self.render_cart()
        
        # Update total label
        self.total_label.config(text=f"Rp {self.total:,}")
        
    def decrease_qty(self, name):
        cart_detail_service.decreaseQuantity(self.fetch_cart_id[0], name)
        self.fetch_cart = cart_detail_service.fetchCartDetailsByCartId(self.fetch_cart_id[0])
        
        # Clear old widgets
        for widget in self.scrollable_cart_frame.winfo_children():
            widget.destroy()
        
        # Re-render and get new total
        self.total = self.render_cart()
        
        # Update total label
        self.total_label.config(text=f"Rp {self.total:,}")

    def remove_item(self, name):
        cart_detail_service.removeItemFromCart(self.fetch_cart_id[0], name)
        self.fetch_cart = cart_detail_service.fetchCartDetailsByCartId(self.fetch_cart_id[0])
        
        # Check if cart is now empty
        if not self.fetch_cart or len(self.fetch_cart) == 0:
            self.view_cart()
            return
        
        # Clear old widgets
        for widget in self.scrollable_cart_frame.winfo_children():
            widget.destroy()
        
        # Re-render and get new total
        self.total = self.render_cart()
        
        # Update total label
        self.total_label.config(text=f"Rp {self.total:,}")

    def checkout(self, current_user_id):
        if not self.fetch_cart or len(self.fetch_cart) == 0:
            messagebox.showinfo("Info", "Your cart is empty!")
            return
        
        if self.balance < self.total:
            messagebox.showinfo("Info", "Your balance is insufficient!")
            return
        
        for item in self.fetch_cart:
         
            name = item[1]
            quantity = item[3]

            
            product = product_services.getProductByName(name)

         

            current_stock = product[5]

            if quantity > current_stock:
                messagebox.showinfo("Info", f"Insufficient stock for {name}!")
                return

            # Update stock produk
            new_stock = current_stock - quantity
            product_services.updateStock(product[0], new_stock)

        user_services.updateBalance(current_user_id, self.balance - self.total)

        cart_services.checkoutCart(current_user_id, self.fetch_cart_id[0], self.total)

        messagebox.showinfo("Success", "Checkout successful!")
        self.home_screen_customer()

        

        
    
    def create_product_card(self, parent, image_url, name, price, stock, seller):
        card = Frame(parent, bg="white", bd=1, relief=SOLID)

        # Biar card tidak mengecil
        card.config(width=230, height=350)
        card.pack_propagate(False)

        # Gunakan Canvas untuk image
        img_canvas = Canvas(card, width=220, height=200, bg="white", highlightthickness=0)
        img_canvas.pack(pady=5)

        if not hasattr(self, "image_cache"):
            self.image_cache = {}

        if not hasattr(self, "image_refs"):
            self.image_refs = []

        # Function untuk load image di background
        def load_image_async():
            try:
                # Kalau sudah ada di cache
                if image_url in self.image_cache:
                    photo = self.image_cache[image_url]

                    def show_cached():
                        try:
                            if img_canvas.winfo_exists():
                                img_canvas.delete("all")
                                img_canvas.create_image(110, 100, image=photo)
                        except:
                            pass

                    try:
                        img_canvas.after(0, show_cached)
                    except:
                        pass
                    return

                # Download gambar
                response = requests.get(image_url, timeout=10)
                img_data = response.content

                img = Image.open(BytesIO(img_data))
                img = img.convert("RGB")

                # Paksa ukuran pas, tidak kecil, tidak gepeng
                img = ImageOps.fit(img, (220, 200), Image.LANCZOS)

                photo = ImageTk.PhotoImage(img)

                # Simpan di cache
                self.image_cache[image_url] = photo
                self.image_refs.append(photo)

                # Tampilkan di canvas
                def show_image():
                    try:
                        if img_canvas.winfo_exists():
                            img_canvas.delete("all")
                            img_canvas.create_image(110, 100, image=photo)
                    except:
                        pass

                try:
                    img_canvas.after(0, show_image)
                except:
                    pass

            except Exception as e:
         
                try:
                    img_canvas.after(0, lambda: img_canvas.create_text(
                        110, 100, text="Image not available"
                    ) if img_canvas.winfo_exists() else None)
                except:
                    pass

        # Jalankan thread
        threading.Thread(target=load_image_async, daemon=True).start()

        # Info produk
        Label(card, text=name, font=("Arial", 12, "bold"), bg="white").pack()
        price_formatted = f"Rp {price:,}".replace(",", ".")
        Label(card, text=price_formatted, fg="black", bg="white").pack()
        Label(card, text=f"Stock: {stock}", fg="black", bg="white").pack()
        
        Label(card, text=f"🏪 {seller[1]}", fg="black", bg="white").pack()

        self.btn_add_to_cart = ttk.Button(
            card,
            text="Add to Cart",
            command=lambda: self.add_to_cart_process(
                seller[0], name, price, image_url
            )
        )
        self.btn_add_to_cart.pack(pady=10)

        return card

    # ----------------------------
    # Tambahan: fungsi Add Balance
    # ----------------------------
    def add_balance(self):
        top = Toplevel(self.root)
        top.title("Add Balance")
        top.geometry("400x280")
        top.resizable(False, False)
        top.configure(bg=self.LIGHT_BG)

        # Header frame dengan warna #4A70A9
        header_frame = Frame(top, bg="#4A70A9", height=60)
        header_frame.pack(fill=X)
        header_frame.pack_propagate(False)
        
        Label(
            header_frame,
            text="Add Balance",
            font=("Arial", 18, "bold"),
            bg="#4A70A9",
            fg="white"
        ).pack(pady=15)
        
        # Content frame
        content_frame = Frame(top, bg=self.LIGHT_BG)
        content_frame.pack(fill=BOTH, expand=True, padx=30, pady=20)
        
        Label(
            content_frame,
            text="Enter top-up amount:",
            font=("Arial", 12, "bold"),
            bg=self.LIGHT_BG,
            fg=self.TEXT_COLOR
        ).pack(pady=(0, 10))

        entry_amount = Entry(
            content_frame,
            font=("Arial", 13),
            bd=1,
            relief=SOLID,
            highlightthickness=2,
            highlightbackground="#D9D9D9",
            highlightcolor="#4A70A9",
            justify="center"
        )
        entry_amount.pack(pady=5, ipady=8, padx=20)

        def process_add():
            # Validasi input
            try:
                amount = int(entry_amount.get())
                if amount <= 0:
                    messagebox.showerror("Error", "Amount must be greater than 0!")
                    return
            except ValueError:
                messagebox.showerror("Error", "Input must be a number!")
                return

            # Ambil balance dari DB
            user = user_services.getUserById(self.current_customer_id)
            if not user:
                messagebox.showerror("Error", "User not found!")
                return
            current_balance = user[5] if user[5] is not None else 0

            # Maksimal saldo 1.000.000.000
            if current_balance + amount > 1_000_000_000:
                messagebox.showwarning("Error", "Balance Must not Greater than 1.000.000.000")
                return

            # Update saldo di DB
            user_services.updateBalance(self.current_customer_id, current_balance + amount)

            messagebox.showinfo("Success", "Balance successfully added!")
            top.destroy()

            # Refresh tampilan home & saldo
            self.home_screen_customer()

        # Button frame
        button_frame = Frame(content_frame, bg=self.LIGHT_BG)
        button_frame.pack(pady=20)
        
        # Add button
        btn_add = Button(
            button_frame,
            text="Add Balance",
            font=("Arial", 12, "bold"),
            bg="#4A70A9",
            fg="white",
            activebackground="#4A70A9",
            activeforeground="white",
            relief=FLAT,
            bd=0,
            padx=25,
            pady=10,
            cursor="hand2",
            command=process_add
        )
        btn_add.pack(side=RIGHT, padx=5)

        
        # Cancel button
        btn_cancel = Button(
            button_frame,
            text="Cancel",
            font=("Arial", 12, "bold"),
            bg=self.LIGHT_BG,
            fg=self.SECONDARY_TEXT,
            activebackground=self.GRAY_BG,
            relief=FLAT,
            bd=1,
            padx=25,
            pady=10,
            cursor="hand2",
            command=top.destroy
        )
        btn_cancel.pack(side=LEFT, padx=5)
        btn_cancel.bind("<Enter>", lambda e: e.widget.config(bg=self.GRAY_BG))
        btn_cancel.bind("<Leave>", lambda e: e.widget.config(bg=self.LIGHT_BG))

    # ----------------------------
    # End Add Balance
    # ----------------------------

    def logout(self):
        self.clear_window()
        self.home_screen()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()



 
    def show_profile(self):
        self.clear_window()  
        fetchUserData  = user_services.getUserById(self.current_customer_id)
        

        main_frame = Frame(self.root, bg=self.GRAY_BG)
        main_frame.pack(fill=BOTH, expand=YES)
        
       
        header_frame = Frame(main_frame, bg="#4A70A9", height=100)
        header_frame.pack(fill=X)
        header_frame.pack_propagate(False)
        
        Label(
            header_frame,
            text="User Profile",
            font=("Arial", 28, "bold"),
            bg="#4A70A9",
            fg="white"
        ).pack(pady=30)
        
  
        content_frame = Frame(main_frame, bg=self.LIGHT_BG)
        content_frame.pack(pady=60, padx=200, fill=BOTH, expand=YES)
        
        inner_frame = Frame(content_frame, bg=self.LIGHT_BG)
        inner_frame.pack(padx=60, pady=40)
        
        profile_card = Frame(inner_frame, bg=self.LIGHT_BG)
        profile_card.pack(fill=X, pady=20)
        
      
        user_frame = Frame(profile_card, bg=self.LIGHT_BG)
        user_frame.pack(fill=X, pady=15)
        
        Label(
            user_frame,
            text="Username:",
            font=("Arial", 14, "bold"),
            bg=self.LIGHT_BG,
            fg=self.TEXT_COLOR,
            width=15,
            anchor=W
        ).pack(side=LEFT, padx=(0, 20))
        
        Label(
            user_frame,
            text=fetchUserData[1],
            font=("Arial", 14),
            bg=self.LIGHT_BG,
            fg=self.TEXT_COLOR,
            anchor=W
        ).pack(side=LEFT)
        

        email_frame = Frame(profile_card, bg=self.LIGHT_BG)
        email_frame.pack(fill=X, pady=15)
        
        Label(
            email_frame,
            text="Email:",
            font=("Arial", 14, "bold"),
            bg=self.LIGHT_BG,
            fg=self.TEXT_COLOR,
            width=15,
            anchor=W
        ).pack(side=LEFT, padx=(0, 20))
        
        Label(
            email_frame,
            text=fetchUserData[2],
            font=("Arial", 14),
            bg=self.LIGHT_BG,
            fg=self.TEXT_COLOR,
            anchor=W
        ).pack(side=LEFT)
        
    
        role_frame = Frame(profile_card, bg=self.LIGHT_BG)
        role_frame.pack(fill=X, pady=15)
        
        Label(
            role_frame,
            text="Role:",
            font=("Arial", 14, "bold"),
            bg=self.LIGHT_BG,
            fg=self.TEXT_COLOR,
            width=15,
            anchor=W
        ).pack(side=LEFT, padx=(0, 20))
        
        Label(
            role_frame,
            text=fetchUserData[4].capitalize(),
            font=("Arial", 14),
            bg=self.LIGHT_BG,
            fg=self.TEXT_COLOR,
            anchor=W
        ).pack(side=LEFT)
        
    
        balance_frame = Frame(profile_card, bg=self.LIGHT_BG)
        balance_frame.pack(fill=X, pady=15)
        
        Label(
            balance_frame,
            text="Balance:",
            font=("Arial", 14, "bold"),
            bg=self.LIGHT_BG,
            fg=self.TEXT_COLOR,
            width=15,
            anchor=W
        ).pack(side=LEFT, padx=(0, 20))
        
        Label(
            balance_frame,
            text=f"Rp {fetchUserData[5]:,}",
            font=("Arial", 14, "bold"),
            bg=self.LIGHT_BG,
            fg=self.SUCCESS_COLOR,
            anchor=W
        ).pack(side=LEFT)
        
   
        btn_back = Button(
            inner_frame,
            text="← Back to Home",
            font=("Arial", 14, "bold"),
            bg="#4A70A9",
            fg="white",
            activebackground="#096DD9",
            activeforeground="white",
            relief=FLAT,
            bd=0,
            padx=30,
            pady=12,
            cursor="hand2",
            command=self.home_screen_customer
        )
        btn_back.pack(pady=10)
        btn_back.bind("<Enter>", lambda e: e.widget.config(bg="#096DD9"))
        btn_back.bind("<Leave>", lambda e: e.widget.config(bg="#4A70A9"))




root = Tk()
root.configure(bg="#F9F8F6")
app = MainApp(root)
root.mainloop()
