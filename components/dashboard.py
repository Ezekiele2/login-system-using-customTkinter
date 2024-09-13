import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk, ImageOps, ImageDraw 
from CTkTable import CTkTable

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard")
        self.root.geometry("1280x720")
        self.root.resizable(0, 0)

        # Navbar container
        self.nav_container = ctk.CTkFrame(master=self.root, fg_color='#2e2659', width=200, height=700, corner_radius=0)
        self.nav_container.pack_propagate(0)
        self.nav_container.pack(fill="y", anchor="w", side="left")

        # Logo
        self.logo_img_data = Image.open("assets/images/logo.png")  # Load your logo image
        self.logo_img = ctk.CTkImage(dark_image=self.logo_img_data, light_image=self.logo_img_data, size=(30, 30))
        ctk.CTkLabel(master=self.nav_container, text="Gear & Grease", image=self.logo_img, compound="left",
                     font=("Century Gothic", 16, "bold"), fg_color="#2e2357", text_color="white").pack(pady=(20, 20), anchor="center")

        # Dashboard Button
        self.dashboard_icon = ctk.CTkImage(Image.open("assets/images/analytics_icon.png"), size=(20, 20))
        self.dashboard_button = ctk.CTkButton(master=self.nav_container, text="Dashboard", image=self.dashboard_icon,
                                              fg_color="#2e2357", text_color="white", anchor="w",
                                              compound="left", width=180, height=40, hover_color='#504973')
        self.dashboard_button.pack(pady=(10, 0))

        # Key Metrics Button
        self.keymetrics_icon = ctk.CTkImage(Image.open("assets/images/analytics_icon.png"), size=(20, 20))
        self.keymetrics_button = ctk.CTkButton(master=self.nav_container, text="Key Metrics", image=self.keymetrics_icon,
                                               fg_color="#2e2357", text_color="white", anchor="w",
                                               compound="left", width=180, height=40, hover_color='#504973')
        self.keymetrics_button.pack(pady=(10, 0))

        # Analytics Section with Drop-down Icon
        self.analytics_icon = ctk.CTkImage(Image.open("assets/images/analytics_icon.png"), size=(20, 20))
        self.drop_down_icon = ctk.CTkImage(Image.open("assets/images/drop-down_icon.png"), size=(10, 10))

        # Create a frame to hold the button content
        self.analytics_frame = ctk.CTkFrame(master=self.nav_container, fg_color="#2e2357", width=180, height=40)
        self.analytics_frame.pack_propagate(0)  # Prevent frame from resizing
        self.analytics_frame.pack(pady=(10, 0))

        # Add Analytics icon and text to the left
        self.analytics_label = ctk.CTkLabel(master=self.analytics_frame, text="  Analytics", image=self.analytics_icon,
                                            fg_color="#2e2357", text_color="white", anchor="w",
                                            compound="left", font=("Arial", 14))
        self.analytics_label.pack(side="left", padx=(10, 0))

        # Add Drop-down icon to the right
        self.dropdown_label = ctk.CTkLabel(master=self.analytics_frame, text="", image=self.drop_down_icon, 
                                           fg_color="#2e2357")
        self.dropdown_label.pack(side="right", padx=(0, 10))

        # Make the whole frame clickable
        self.analytics_frame.bind("<Button-1>", lambda event: self.toggle_analytics())
        self.analytics_label.bind("<Button-1>", lambda event: self.toggle_analytics())
        self.dropdown_label.bind("<Button-1>", lambda event: self.toggle_analytics())

        # Sub-items for Analytics (initially hidden)
        self.analytics_subitems = ctk.CTkFrame(master=self.nav_container, fg_color="#3e2c72", corner_radius=0)
        
        self.all_analytics_button = ctk.CTkButton(master=self.analytics_subitems, text="All Analytics",
                                                  fg_color="#3e2c72", text_color="white", anchor="w",
                                                  compound="left", width=160, height=30, hover_color='#504973')
        self.all_analytics_button.pack(pady=(5, 0), padx=(20, 0))

        self.favorites_button = ctk.CTkButton(master=self.analytics_subitems, text="Favorites",
                                              fg_color="#3e2c72", text_color="white", anchor="w",
                                              compound="left", width=160, height=30, hover_color='#504973')
        self.favorites_button.pack(pady=(5, 0), padx=(20, 0))

        self.new_analytics_button = ctk.CTkButton(master=self.analytics_subitems, text="New Analytics",
                                                  fg_color="#3e2c72", text_color="white", anchor="w",
                                                  compound="left", width=160, height=30, hover_color='#504973')
        self.new_analytics_button.pack(pady=(5, 0), padx=(20, 0))
        
        # Separator Line Below Analytics Button
        self.separator_line = ctk.CTkFrame(master=self.nav_container, fg_color="#4e3c82", height=2, width=180)
        self.separator_line.pack(pady=(5, 5))

        # Settings Button
        self.settings_icon = ctk.CTkImage(Image.open("assets/images/set-icon.png"), size=(20, 20))
        self.settings_button = ctk.CTkButton(master=self.nav_container, text="Settings", image=self.settings_icon,
                                               fg_color="#2e2357", text_color="white", anchor="w",
                                               compound="left", width=180, height=40, hover_color='#504973')
        self.settings_button.pack(pady=(10, 0))

        # Help Center Button
        self.help_center_icon = ctk.CTkImage(Image.open("assets/images/help-center_icon.png"), size=(20, 20))
        self.help_center_button = ctk.CTkButton(master=self.nav_container, text="Help center", image=self.help_center_icon,
                                               fg_color="#2e2357", text_color="white", anchor="w",
                                               compound="left", width=180, height=40, hover_color='#504973')
        self.help_center_button.pack(pady=(10, 0))

        # Circular Profile Image (Fixed at bottom of nav_container)
        self.profile_frame = ctk.CTkFrame(master=self.nav_container, fg_color="#514a74")
        self.profile_frame.pack(side="bottom", pady=(10, 20))  # Ensure it's at the bottom with some padding

        self.profile_img_data = Image.open("assets/images/profile_icon.png")
        self.profile_img_data = self.profile_img_data.resize((50, 50))
        self.circular_image = self.create_circular_image(self.profile_img_data)

        # Use CTkButton to make the profile image clickable
        self.profile_image_button = ctk.CTkButton(master=self.profile_frame, image=self.circular_image, text="", hover=False,
                                                  fg_color="transparent", command=self.logout)
        self.profile_image_button.image = self.circular_image  # Keep reference
        self.profile_image_button.pack(pady=(10, 5))

        # Profile Name and Email (inside the fixed bottom frame)
        ctk.CTkLabel(master=self.profile_frame, text="Annette Black", font=("Arial", 16)).pack()
        ctk.CTkLabel(master=self.profile_frame, text="annette.bl@gmail.com", font=("Arial", 12), text_color="gray").pack(pady=(0, 10))

        # main
        self.main_view = ctk.CTkFrame(master=self.root, fg_color="#f3f4f6",  width=1080, height=720, corner_radius=0)
        self.main_view.pack_propagate(0)
        self.main_view.pack(side="left")

        # Title frame
        self.title_frame = ctk.CTkFrame(master=self.main_view, fg_color="#f3f4f6")  # Updated to match the main background color
        self.title_frame.pack(anchor="n", fill="x", pady=(0, 0))

        # Greeting label
        self.greeting_label = ctk.CTkLabel(master=self.title_frame, text="Viewer Dashboard", font=("Century Gothic",25, "bold"), text_color="#1b1730")
        self.greeting_label.pack(anchor="nw", side="left", padx=10, pady=10)

       # Load the icons using PIL and create CTkImage objects
        self.search_icon = ctk.CTkImage(Image.open("assets/images/search_icon.png"), size=(20, 20))
        self.notification_icon = ctk.CTkImage(Image.open("assets/images/notification_icon.png"), size=(15, 20))
        calendar_icon = ctk.CTkImage(Image.open("assets/images/calendar_icon.png"), size=(20, 20))  # Example icon for combobox

        notification_button = ctk.CTkButton(master=self.title_frame, text="", image=self.notification_icon, width=10, height=20, fg_color="#faf9fe", hover_color="#e8e8e8", corner_radius=15)
        notification_button.pack(side="right", padx=(0, 10))

        # Create a frame for the search bar
        self.search_frame = ctk.CTkFrame(master=self.title_frame, fg_color="#faf9fe")
        self.search_frame.pack(side="right", padx=(0, 10), pady=10)

        # Search entry
        self.search_entry = ctk.CTkEntry(master=self.search_frame, placeholder_text="Search", width=150, height=20, fg_color="#faf9fe", border_color="#e8e8e8", border_width=1)
        self.search_entry.pack(side="left", padx=(10, 0), pady=5)

        # Search button
        self.search_button = ctk.CTkButton(master=self.search_frame, text="", image=self.search_icon, width=30, height=30, fg_color="#faf9fe", hover_color="#e8e8e8", corner_radius=15)
        self.search_button.pack(side="right", padx=(5, 10))

        self.category_container = ctk.CTkFrame(master=self.main_view, height=50, fg_color="#f3f4f6")
        self.category_container.pack(fill="x", pady=(5, 0))

        # Create a frame to hold the combobox and the calendar icon
        combobox_frame = ctk.CTkFrame(master=self.category_container, fg_color="#f3f4f6")
        combobox_frame.pack(side="left", padx=(10, 10), pady=10)

        # Create a ComboBox
        combobox = ctk.CTkComboBox(
            master=combobox_frame, 
            values=["Option 1", "Option 2", "Option 3"], 
            fg_color="white", 
            border_color="black", 
            dropdown_fg_color="white",
            width=150, 
            height=25
        )
        combobox.pack(side="left")

        self.data_container = ctk.CTkFrame(master=self.main_view, height=50, fg_color="#f3f4f6")
        self.data_container.pack(fill="x", pady=(5, 0))

        self.stat_data = ctk.CTkFrame(master=self.data_container , fg_color="#d8e2fd", width=430, height=250,border_width=1, border_color='gray', corner_radius=20)
        self.stat_data.grid_propagate(0)
        self.stat_data.pack(side="left", padx=(10,0))

        self.uknown_data = ctk.CTkFrame(master=self.data_container , fg_color="#d9eaeb", width=300, height=250,border_width=1, border_color='gray', corner_radius=20)
        self.uknown_data.grid_propagate(0)
        self.uknown_data.pack(side="left", padx=(10,0))

        self.shipped_metric =  ctk.CTkFrame(master=self.data_container , fg_color="#d9e1fd", width=300, height=130,border_width=1, border_color='gray', corner_radius=15)
        self.shipped_metric.grid_propagate(0)
        self.shipped_metric.pack(side="top",expand=True, anchor="center", pady=(0,0))

        self.delivered_metric =ctk.CTkFrame(master=self.data_container, fg_color="#f0e5e3", width=300, height=130,border_width=1, border_color='gray', corner_radius=15)
        self.delivered_metric.grid_propagate(0)
        self.delivered_metric.pack(side="top",pady=(3,0))



    def toggle_analytics(self):
        if self.analytics_subitems.winfo_ismapped():
            self.analytics_subitems.pack_forget()
            # Move the separator back to its original position
            self.separator_line.pack(pady=(10, 5), before=self.settings_button)
        else:
            self.analytics_subitems.pack(after=self.separator_line, fill="x", pady=(5, 0))
            # Repack the separator after the analytics subitems
            self.separator_line.pack(pady=(10, 5), after=self.analytics_subitems)


    def create_circular_image(self, img):
        # Create a circular image using PIL
        bigsize = (img.size[0] * 3, img.size[1] * 3)
        mask = Image.new("L", bigsize, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(img.size, Image.LANCZOS)
        img.putalpha(mask)
        return ImageTk.PhotoImage(img)
    
    def logout(self):
        # Add your logout logic here
        print("User logged out!")  # Placeholder action

if __name__ == "__main__":
    root = ctk.CTk()
    app = Dashboard(root)
    root.mainloop()
