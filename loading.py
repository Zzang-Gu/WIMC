from PIL import Image
import customtkinter as ctt

import login

class Loading(ctt.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, 1432, 805, **kwargs)
        self.master = master

        ctkImgBackground = ctt.CTkImage(light_image=Image.open(".\\img\\login\\loading.png"), dark_image=Image.open(".\\img\\login\\loading.png"), size=(1432, 805))
        self.labBackground = ctt.CTkLabel(self, image=ctkImgBackground, text="")
        self.labBackground.place(x=0, y=0)

        self.after(3000, self.showLoginPage)

    def showLoginPage(self):
        self.master.updatePage(login.Login)
