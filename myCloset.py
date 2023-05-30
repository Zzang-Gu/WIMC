import customtkinter as ctt
from PIL import Image

class MyCloset(ctt.CTkFrame):
    def __init__(self, master, width, height, **kwargs):
        super().__init__(master, width, height, **kwargs)

        imgBackground = ctt.CTkImage(light_image=Image.open(".\\img\\MyCloset\\background.png"),
                                     dark_image=Image.open(".\\img\\MyCloset\\background.png"),
                                     size=(1432, 805))

        self.labelTitle = ctt.CTkLabel(self, image=imgBackground, text="")
        self.labelTitle.grid()

class App(ctt.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1432x805")

        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)

        self.frameMyCloset = MyCloset(master=self, width=1432, height=805)
        self.frameMyCloset.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

if __name__ == "__main__":
    app = App()
    app.mainloop()
