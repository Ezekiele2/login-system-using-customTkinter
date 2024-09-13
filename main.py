import customtkinter as ctk
from components.login_form import LoginForm
from components.dashboard import Dashboard

# ctk to create an alias for customtkinter
def main():
    # Set appearance mode and color theme
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("green")

    root = ctk.CTk()
    #app = Dashboard(root)
    app = LoginForm(root)
    root.mainloop()

if __name__ == "__main__":
    main()