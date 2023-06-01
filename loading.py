import customtkinter as ctt
from PIL import Image

# pages
from login import Login

class Loading(ctt.CTkFrame):
    def __init__(self, master, width, height, **kwargs):
        super().__init__(master, width, height, **kwargs)
        self.master = master

        self.initialize()
        self.after(3000, self.showLoginPage)

    def initialize(self):
        # background
        background = ctt.CTkImage(light_image=Image.open(".\\img\\login\\loading.png"),
                                  dark_image=Image.open(".\\img\\login\\loading.png"),
                                  size=(1432, 805))
        self.background = ctt.CTkLabel(self, image=background, text="")
        self.background.place(x=0, y=0)

    def showLoginPage(self):
        self.master.updatePage(Login)
