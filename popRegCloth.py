import io
from PIL import Image
import customtkinter as ctt

class ToplevelWindow(ctt.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("634x682")

        self.imgBack = ctt.CTkImage(light_image=Image.open(".\\img\\popRegCloth\\background634x682.png"), dark_image=Image.open(".\\img\\popRegCloth\\background634x682.png"), size=(634, 682))
        ctt.CTkLabel(self, image=self.imgBack, bg_color="#E3F2ED", fg_color="#E3F2ED", text="").grid()


