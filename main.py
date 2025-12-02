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
import TKinterModernThemes as TKMT
from cart_service import cart_services 
from CartDetail import CartDetail
from cart_detail_service import cart_detail_service

# from ttkbootstrap import Style


class MainApp(TKMT.ThemedTKinterFrame):
    def __init__(self, root):
        # self.style = Style(theme="cosmo")

        # super().__init__("Elektronikku", theme="azure", mode="light")
        self.root = root
        self.root.title("Elektronikku")
        self.root.state("zoomed")

        # self.root.geometry("800x600")
        self.home_screen()

    def home_screen(self):
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
        self.btn_register = ttk.Button(self.root, text="Register", command=self.register_user)
        self.btn_register.pack(pady=30)

    def register_user(self):
        self.clear_window()
        ttk.Label(self.root, text="User Registration", font=("Helvetica", 16)).pack(pady=20)
        ttk.Label(self.root, text="Username", font=("Helvetica", 14)).pack(pady=10)
        self.entry_username = ttk.Entry(self.root)
        self.entry_username.pack()
        ttk.Label(self.root, text="Email", font=("Helvetica", 14)).pack(pady=10)
        self.entry_email = ttk.Entry(self.root)
        self.entry_email.pack()
        ttk.Label(self.root, text="Password", font=("Helvetica", 14)).pack(pady=10)
        self.entry_password = ttk.Entry(self.root, show="*")
        self.entry_password.pack()
        ttk.Label(self.root, text="Balance", font=("Helvetica", 14)).pack(pady=10)
        self.entry_balance = ttk.Entry(self.root)
        self.entry_balance.pack()
        self.btn_register = ttk.Button(self.root, text="Register", command=self.process_register)
        self.btn_register.pack(pady=20)

    def process_register(self):
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

        sidebar = Frame(body, width=250, bg="#d4eded")
        sidebar.pack(side="left", fill="y")

        product_area = Frame(body, bg="white")
        product_area.pack(side="right", fill="both", expand=True)

        Button(sidebar,
           text="Profile",
           font=("Arial", 14, "bold"),
           bg="#69a7a7",
           fg="black",
           height=2).pack(fill="x", padx=10, pady=20)
        
        Button(sidebar,
           text="Add Balance",
           font=("Arial", 14, "bold"),
           bg="#69a7a7",
           fg="black",
           height=2).pack(fill="x", padx=10, pady=20)
        
        Button(sidebar,
           text="History",
           font=("Arial", 14, "bold"),
           bg="#69a7a7",
           fg="black",
           height=2).pack(fill="x", padx=10, pady=20)
        
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
                                        seller
                                        )
            card.grid(row=row, column=col, padx=20, pady=20)


            col += 1
            if col == 5:
                col = 0
                row += 1

    def add_to_cart_process(self, sellerId, name, price, image_url):
        checkCart = cart_services.checkCartActive(self.current_customer_id, sellerId)

        if not checkCart:
            cart_services.createCart(self.current_customer_id, sellerId)
            

        self.cartId = cart_services.getCartByUserAndSeller(self.current_customer_id, sellerId)
        print(self.cartId)

       
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
            text="🛒 My Shopping Cart",
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
        print(self.fetch_cart_id)
        
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

            def center_window(event):
                self.canvas_cart.configure(scrollregion=self.canvas_cart.bbox("all"))
                # Center horizontally
                canvas_width = self.canvas_cart.winfo_width()
                if canvas_width > 1:
                    self.canvas_cart.coords(self.cart_window_id, canvas_width // 2, 0)

            self.scrollable_cart_frame.bind("<Configure>", center_window)

            self.cart_window_id = self.canvas_cart.create_window((0, 0), window=self.scrollable_cart_frame, anchor="n")
            self.canvas_cart.configure(yscrollcommand=self.scrollbar_cart.set)

            self.canvas_cart.pack(side="left", fill="both", expand=True)
            self.scrollbar_cart.pack(side="right", fill="y")
            
            # Bind canvas resize untuk re-center
            self.canvas_cart.bind("<Configure>", lambda e: center_window(e) if self.canvas_cart.winfo_width() > 1 else None)

            self.total = self.render_cart()

            # Footer dengan total dan checkout yang menarik
            footer_frame = Frame(self.root, bg="white", bd=1, relief="solid")
            footer_frame.pack(fill=X, pady=10, padx=50)
            
            # Total price container
            total_container = Frame(footer_frame, bg="white")
            total_container.pack(pady=15)
            
            Label(
                total_container,
                text=f"Balance: Rp{self.balance:,}",
                font=("Arial", 22, "bold"),
                bg="white",
                fg="black",
            ).pack(pady=20)
            
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
                bg="#4CAF50",
                fg="white",
                relief="flat",
                padx=30,
                pady=12,
                cursor="hand2",
                command=lambda: self.checkout(self.current_customer_id)
            )
            checkout_btn.pack(pady=10)



    def render_cart(self):
        for widget in self.scrollable_cart_frame.winfo_children():
            widget.destroy()


        total_all = 0
      
        for item in self.fetch_cart:
            print(item)
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
                    text="🗑️ Remove", 
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
            print(item, "item")
            name = item[1]
            quantity = item[3]

            
            product = product_services.getProductByName(name)

            print(product, "product")

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

        

        
    
    def create_product_card(self, parent, image_url, name, price, seller):
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
        Label(card, text=f"Rp {price:,}", fg="black", bg="white").pack()
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

    
    def logout(self):
        self.clear_window()
        self.home_screen()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


root = Tk()
app = MainApp(root)
root.mainloop()