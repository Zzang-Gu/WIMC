import customtkinter as ctt
from PIL import Image

# pages

class DailyLookRegister(ctt.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, 1432, 805, **kwargs)
        self.master = master

        self.initialize()

    def initialize(self):
        # background
        background = ctt.CTkImage(light_image=Image.open(".\\img\\winMyCloset\\background1432x805.png"),
                                  dark_image=Image.open(".\\img\\winMyCloset\\background1432x805.png"),
                                  size=(1432, 805))

        self.background = ctt.CTkLabel(self, image=background, text="")
        self.background.place(x=0, y=0)
