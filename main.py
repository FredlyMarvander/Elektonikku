from User import User
from tkinter import *
from tkinter import ttk
from user_service import user_services
from tkinter import messagebox
from product_service import product_services


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Elektronikku")
        self.root.state("zoomed")

        # self.root.geometry("800x600")
        ttk.Label(self.root, text="Welcome to Elektronikku", font=("Helvetica", 16)).pack(pady=20)
        self.buttonAdmin = ttk.Button(self.root, text="Admin", command=self.admin)
        self.buttonAdmin.pack()
        self.buttonCustomer = ttk.Button(self.root, text="Customer", command=self.customer)
        self.buttonCustomer.pack()

    def admin(self):
        self.clear_window()
        ttk.Label(self.root, text="Admin Login", font=("Helvetica", 16)).pack(pady=20)
        ttk.Label(self.root, text="Email", font=("Helvetica", 16)).pack(pady=10)
        self.entry_email = ttk.Entry(self.root)
        self.entry_email.pack()
        ttk.Label(self.root, text="Password", font=("Helvetica", 16)).pack(pady=10)
        self.entry_password = ttk.Entry(self.root, show="*")
        self.entry_password.pack()
        self.btn_login = ttk.Button(self.root, text="Login", command=self.proses_login_admin)
        self.btn_login.pack(pady=20)

    def customer(self):
        self.clear_window()
        ttk.Label(self.root, text="Customer Login", font=("Helvetica", 16)).pack(pady=20)
        ttk.Label(self.root, text="Email", font=("Helvetica", 16)).pack(pady=10)
        self.entry_email = ttk.Entry(self.root)
        self.entry_email.pack()
        ttk.Label(self.root, text="Password", font=("Helvetica", 16)).pack(pady=10)
        self.entry_password = ttk.Entry(self.root, show="*")
        self.entry_password.pack()
        self.btn_login = ttk.Button(self.root, text="Login", command=self.proses_login_customer)
        self.btn_login.pack(pady=20)

    def proses_login_customer(self):
        email = self.entry_email.get()
        password = self.entry_password.get()
       
        if (user_services.login_customer(email, password)):
            messagebox.showinfo("Info", "Login Successfully!")
            self.clear_window()
            self.home_screen_customer()
        else:
            messagebox.showerror("Error", "Email or Password is Wrong")

    def proses_login_admin(self):
        email = self.entry_email.get()
        password = self.entry_password.get()
        
        if (user_services.login_admin(email, password)):
            messagebox.showinfo("Info", "Login Successfully!")
            self.clear_window()
            self.home_screen_admin()
        else:
            messagebox.showerror("Error", "Email or Password is Wrong")
            
    def home_screen_admin(self):
        ttk.Label(self.root, text="Admin Dashboard", font=("Helvetica", 16)).pack(pady=20)
        self.btn_logout = ttk.Button(self.root, text="Logout", command=self.logout)
        self.btn_logout.pack(pady=20)
        self.btn_view_products = ttk.Button(self.root, text="View Products", command=self.view_products)
        self.btn_view_products.pack(pady=10)
    
    def view_products(self):
        self.clear_window()
        ttk.Label(self.root, text="Product List", font=("Helvetica", 14)).pack(pady=10)
        
        
        top_frame = ttk.Frame(self.root)
        top_frame.pack(fill=X, padx=20)

        self.table = ttk.Treeview(self.root, columns=("No", "Name", "Description", "Price", "Stock"), show="headings")
        self.table.heading("No", text="No")
        self.table.heading("Name", text="Product Name")
        self.table.heading("Description", text="Description")
        self.table.heading("Price", text="Price")
        self.table.heading("Stock", text="Stock")

        self.table.column("No", width=50, anchor="center")
        self.table.column("Name", width=150, anchor="center")
        self.table.column("Description", width=300, anchor="center")
        self.table.column("Price", width=100, anchor="center")
        self.table.column("Stock", width=100, anchor="center")

        self.table.pack(fill="both", expand=True)
        self.load_table_data()

    def load_table_data(self):
        self.products = product_services.fetchProducts()
        i = 1
        for product in self.products:
            self.table.insert("", "end", values=(i, product[0], product[1], product[2], product[3], product[4]))
            i += 1

    def home_screen_customer(self):
        ttk.Label(self.root, text="Customer Dashboard", font=("Helvetica", 16)).pack(pady=20)
        self.btn_logout = ttk.Button(self.root, text="Logout", command=self.logout)
        self.btn_logout.pack(pady=20)

    def logout(self):
        self.clear_window()
        self.__init__(self.root)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

root = Tk()
app = MainApp(root)
root.mainloop()