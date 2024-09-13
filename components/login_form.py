import tkinter
import customtkinter as ctk
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
from components.dashboard import Dashboard 
from utils.database import Database

class LoginForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1280x720")

        # Load and set the background image
        image = ImageTk.PhotoImage(Image.open("assets/images/pattern.png"))

        self.background_label = ctk.CTkLabel(master=self.root, image=image)
        self.background_label.pack()

        # Main login container (fixed size)
        self.login_container = ctk.CTkFrame(master=self.background_label, width=700, height=360, corner_radius=20, fg_color="#ffffff",bg_color='#282024')
        self.login_container.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        
        # Prevent resizing based on children's sizes
        self.login_container.pack_propagate(False)

        # Create a second container inside login_container for the columns
        self.login_container_2 = ctk.CTkFrame(master=self.login_container, fg_color="transparent")
        self.login_container_2.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Prevent login_container_2 from affecting the size of login_container
        self.login_container_2.pack_propagate(False)

         # Configure grid layout for login_container_2
        self.login_container_2.grid_columnconfigure(0, weight=1)
        self.login_container_2.grid_columnconfigure(1, weight=1)

        # Left column frame
        self.left_column = ctk.CTkFrame(master=self.login_container_2, fg_color="#e0e0e0", corner_radius=0)
        self.left_column.grid(row=0, column=0, sticky="nsew")

        # Content for left column: 
        # Load and set the logo image
        logo_image = ImageTk.PhotoImage(Image.open("assets/images/gg.png"))
        self.logo_label = ctk.CTkLabel(master=self.left_column, image=logo_image)
        self.logo_label.pack(pady=(20,0))

        self.logo_label.image = logo_image

        # Right column frame
        self.right_column = ctk.CTkFrame(master=self.login_container_2, fg_color="#e0e0e0", corner_radius=0)
        self.right_column.grid(row=0, column=1, sticky="nsew")

        # Content for right column: "Gear & Grease" text
        self.gear_grease_label = ctk.CTkLabel(master=self.right_column, text="Gear & Grease", font=('Century Gothic', 37, "bold"))
        self.gear_grease_label.pack(pady=(40,20))

        # Username & password field containers
        self.username_frame = ctk.CTkFrame(master=self.right_column, fg_color="#ffffff", border_width=0)
        self.username_frame.pack(pady=5, padx=20, fill="x")

        self.password_frame = ctk.CTkFrame(master=self.right_column, fg_color="#ffffff", border_width=0)
        self.password_frame.pack(pady=10, padx=20, fill="x")

        # Username label and entry
        self.username_label = ctk.CTkLabel(master=self.username_frame, text="👤", font=("Arial", 16))
        self.username_label.pack(side="left", padx=10)

        self.username_entry = ctk.CTkEntry(master=self.username_frame, placeholder_text="Enter username", width=20, border_width=0)
        self.username_entry.pack(side="left", fill="x", expand=True, padx=10, pady=5)

        # Password label and entry
        self.password_label = ctk.CTkLabel(master=self.password_frame, text="🔒", font=("Arial", 16))
        self.password_label.pack(side="left", padx=10)

        self.password_entry = ctk.CTkEntry(master=self.password_frame, placeholder_text="Enter password", show="*", width=20, border_width=0)
        self.password_entry.pack(side="left", fill="x", expand=True, padx=10, pady=(5,0))

        # "Forgot Password?" Label
        self.forgot_password_label = ctk.CTkLabel(master=self.right_column, text="Forgot Password?", font=("Arial", 12, "italic"), text_color="#007bff", cursor="hand2")
        self.forgot_password_label.pack(padx=20, anchor="e")

        # Button Container
        self.button_container = ctk.CTkFrame(master=self.right_column, corner_radius=15)
        self.button_container.pack(pady=(0, 20), padx=20, fill="x")

        # Login Button
        self.go_button = ctk.CTkButton(
            master=self.button_container, text="LOGIN", hover_color="darkblue", width=200, height=50, fg_color="#007bff", command=self.button_clicked
        )
        self.go_button.pack(fill="x", pady=10)

        # Bind the ENTER key to trigger the button click event
        self.root.bind("<Return>", self.button_clicked)


    # Optional: Functionality for Forgot Password
    def forgot_password(self, event):
        messagebox.showinfo("Forgot Password", "Redirecting to password recovery...")

    def button_clicked(self, event=None):
        # Retrieve values from the entry fields
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.validated_admin(username, password)  # Validate the credentials

    def validated_admin(self, username, password):
        db = Database()
        users = db.read("users", "username = %s", (username,))
        if not users:
            messagebox.showerror("Error", "User not found.")
            return

        user = users[0]
        db_password = user['password']

        if password == db_password:
            messagebox.showinfo("Success", "Login successful!")
            self.open_dashboard()
        else:
            messagebox.showerror("Error", "Incorrect password.")

    def open_dashboard(self):
        self.root.destroy()
        dashboard_root = tkinter.Tk()
        dashboard_app = Dashboard(dashboard_root)
        dashboard_root.mainloop()


            
