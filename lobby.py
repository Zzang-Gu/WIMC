from PIL import Image
import customtkinter as ctt

import winMyCloset

class Lobby(ctt.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, 1432, 805, **kwargs)

        self.master = master

        imgBackground = ctt.CTkImage(light_image=Image.open(".\\img\\winMyCloset\\background1432x805.png"),
                                     dark_image=Image.open(".\\img\\winMyCloset\\background1432x805.png"),
                                     size=(1432, 805))

        self.labelTitle = ctt.CTkLabel(self, image=imgBackground, text="")
        self.labelTitle.grid()

        self.imgBack = ctt.CTkImage(light_image=Image.open(".\\img\\lobby\\greenPostit220x234.png"), dark_image=Image.open(".\\img\\lobby\\greenPostit220x234.png"), size=(220, 234))
        self.menu1 = ctt.CTkLabel(self, image=self.imgBack, bg_color="#E3F2ED", fg_color="#E3F2ED", text="")
        self.menu1.place(x=100, y=100)
        self.menu1.bind("<Button-1>", self.callMenu1)

    def callMenu1(self, event):
        self.master.updatePage(winMyCloset.MyCloset)

class App(ctt.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1432x805")

        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)

        self.frameMyCloset = Lobby(master=self, width=1432, height=805)
        self.frameMyCloset.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

if __name__ == "__main__":
    app = App()
    app.mainloop()
