import tkinter as tk
from login.gui import Login
# from main_window.main import mainWindow

# Main window constructor
root = tk.Tk()  # Make temporary window for app to start
root.withdraw()  # WithDraw the window


if __name__ == "__main__":

    Login()
    # mainWindow()

    root.mainloop()
