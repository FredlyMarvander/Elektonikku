from User import User
from tkinter import *
from tkinter import ttk
from user_service import user_services
from tkinter import messagebox
from product_service import product_services
from Product import Product
from PIL import Image, ImageTk
import requests
from io import BytesIO
import threading



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
        self.login = user_services.login_admin(email, password)
        
        if (self.login):
            messagebox.showinfo("Info", "Login Successfully!")
            self.userId = user_services.getUserByEmail(email)[0]
            self.clear_window()
            self.home_screen_admin()
        else:
            messagebox.showerror("Error", "Email or Password is Wrong")
            
    def home_screen_admin(self):
        self.clear_window()
        ttk.Label(self.root, text="Admin Dashboard", font=("Helvetica", 16)).pack(pady=20)
        self.btn_logout = ttk.Button(self.root, text="Logout", command=self.logout)
        self.btn_logout.pack(pady=20)
        self.btn_view_products = ttk.Button(self.root, text="View Products", command=self.view_products)
        self.btn_view_products.pack(pady=10)
        self.btn_view_customers = ttk.Button(self.root, text="View Customers", command=self.view_customers)
        self.btn_view_customers.pack(pady=10)
        self.btn_add_admin = ttk.Button(self.root, text="Add Admin", command=self.add_admin)
        self.btn_add_admin.pack(pady=10)

    def add_admin(self):
        self.clear_window()
        ttk.Label(self.root, text="Add New Admin", font=("Helvetica", 16)).pack(pady=20)
        ttk.Label(self.root, text="Username", font=("Helvetica", 14)).pack(pady=10)
        self.entry_username = ttk.Entry(self.root)
        self.entry_username.pack()
        ttk.Label(self.root, text="Email", font=("Helvetica", 14)).pack(pady=10)
        self.entry_email = ttk.Entry(self.root)
        self.entry_email.pack()
        ttk.Label(self.root, text="Password", font=("Helvetica", 14)).pack(pady=10)
        self.entry_password = ttk.Entry(self.root, show="*")
        self.entry_password.pack()
        self.btn_add_admin = ttk.Button(self.root, text="Add Admin", command=self.proses_add_admin)
        self.btn_add_admin.pack(pady=20)

    def proses_add_admin(self):
        username = self.entry_username.get()
        email = self.entry_email.get()
        password = self.entry_password.get()
        role = "admin"
        balance = 0

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
        self.tableCustomers = ttk.Treeview(self.root, columns=("No", "Username", "Email", "Balance"), show="headings")
        self.tableCustomers.heading("No", text="ID")
        self.tableCustomers.heading("Username", text="Username")
        self.tableCustomers.heading("Email", text="Email")
        self.tableCustomers.heading("Balance", text="Balance")
 
        self.tableCustomers.column("No", width=50, anchor="center")
        self.tableCustomers.column("Username", width=150, anchor="center")
        self.tableCustomers.column("Email", width=300, anchor="center")
        self.tableCustomers.column("Balance", width=100, anchor="center")

        self.tableCustomers.pack(fill="both", expand=True)
        self.load_data_customers()

    def load_data_customers(self):
        self.dataCustomers = user_services.getCustomers()
        i = 1

        for customer in self.dataCustomers:
            self.tableCustomers.insert("", "end", values=(i, customer[1], customer[2], customer[5]))
    
    def view_products(self):
        self.clear_window()
        style = ttk.Style()

        table_frame = ttk.Frame(self.root)
        table_frame.pack(fill=BOTH, expand=True, padx=10, pady=5)

        scrollbar_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        style.configure(
            "Custom.Treeview",
            rowheight=70,      
            padding=(5, 3)     
        )

        style.configure(
            "Custom.Treeview.Heading",
            padding=(8, 6)     
        )

        self.image_refs = []
       
        ttk.Label(self.root, text="Product List", font=("Helvetica", 14)).pack(pady=10)
        
        top_frame = ttk.Frame(self.root)
        top_frame.pack(fill=X, padx=20)

        self.table = ttk.Treeview(self.root, columns=("id", "View", "Name", "Description", "Price", "Stock"), show="headings", style="Custom.Treeview",     yscrollcommand=scrollbar_y.set)
        
        # Hubungkan scrollbar ke treeview
        scrollbar_y.config(command=self.table.yview)

        # Layout
        self.table.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar_y.pack(side=RIGHT, fill=Y)

        self.table.heading("id", text="ID")
        self.table.heading("View", text="Image")
        self.table.heading("Name", text="Product Name")
        self.table.heading("Description", text="Description")
        self.table.heading("Price", text="Price")
        self.table.heading("Stock", text="Stock")
 
        self.table.column("id", width=50, anchor="center")
        self.table.column("View", width=70, anchor="center")
        self.table.column("Name", width=150, anchor="center")
        self.table.column("Description", width=300, anchor="center")
        self.table.column("Price", width=100, anchor="center")
        self.table.column("Stock", width=100, anchor="center")

        self.table.bind("<ButtonRelease-1>", self.on_table_click)


        self.table.pack(fill="both", expand=True)

        self.btn_add_product = ttk.Button(self.root, text="Add Product", command=self.add_product)
        self.btn_add_product.pack(pady=5)

        self.btn_edit = ttk.Button(self.root, text="Edit Selected", command=self.edit_selected_product)
        self.btn_edit.pack(pady=5)

        self.btn_delete = ttk.Button(self.root, text="Delete Selected", command=self.delete_selected_product)
        self.btn_delete.pack(pady=5)


        self.load_table_data()

    def load_table_data(self):
        self.products = product_services.fetchProductById(self.userId)
        # self.btn_delete = ttk.Button(self.root, text="Delete Selected Product", command=lambda: self.delete_selected_product(id))
   
        self.image_urls = {}
        for product in self.products:
            
           
            self.table.insert("", "end",  values=(product[0], "View", product[1], product[2], product[4], product[5]))

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
        ttk.Label(self.root, text="Name", font=("Helvetica", 14)).pack(pady=10)
        self.entry_name = ttk.Entry(self.root)
        self.entry_name.pack(pady=20)
        ttk.Label(self.root, text="Description", font=("Helvetica", 14)).pack(pady=10)
        self.entry_description = ttk.Entry(self.root)
        self.entry_description.pack()
        ttk.Label(self.root, text="Image URL", font=("Helvetica", 14)).pack(pady=10)
        self.entry_image_url = ttk.Entry(self.root)
        self.entry_image_url.pack()
        ttk.Label(self.root, text="Price", font=("Helvetica", 14)).pack(pady=10)
        self.entry_price = ttk.Entry(self.root)
        self.entry_price.pack(pady=20)
        ttk.Label(self.root, text="Stock", font=("Helvetica", 14)).pack(pady=10)
        self.entry_stock = ttk.Entry(self.root)
        self.entry_stock.pack(pady=20)
        self.btn_add_product = ttk.Button(self.root, text="Add Product", command=self.proses_add_product)
        self.btn_add_product.pack(pady=10)

    def proses_add_product(self):
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
            ttk.Label(self.root, text="Edit Product", font=("Helvetica", 16)).pack(pady=20)
            ttk.Label(self.root, text="Name", font=("Helvetica", 14)).pack(pady=10)
            self.entry_name = ttk.Entry(self.root)
            self.entry_name.insert(0, product_values[1])
            self.entry_name.pack(pady=20)
            ttk.Label(self.root, text="Description", font=("Helvetica", 14)).pack(pady=10)
            self.entry_description = ttk.Entry(self.root)
            self.entry_description.insert(0, product_values[2])
            self.entry_description.pack()
            ttk.Label(self.root, text="Image URL", font=("Helvetica", 14)).pack(pady=10)
            self.entry_image_url = ttk.Entry(self.root)
            self.entry_image_url.insert(0, image)
            self.entry_image_url.pack(pady=20)
            ttk.Label(self.root, text="Price", font=("Helvetica", 14)).pack(pady=10)
            self.entry_price = ttk.Entry(self.root)
            self.entry_price.insert(0, product_values[3])
            self.entry_price.pack(pady=20)
            ttk.Label(self.root, text="Stock", font=("Helvetica", 14)).pack(pady=10)
            self.entry_stock = ttk.Entry(self.root)
            self.entry_stock.insert(0, product_values[4])
            self.entry_stock.pack(pady=20)
            self.btn_update_product = ttk.Button(self.root, text="Update Product", command=lambda: self.proses_update_product(int(product_values[0])))
            self.btn_update_product.pack(pady=10)

    def proses_update_product(self, id):
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