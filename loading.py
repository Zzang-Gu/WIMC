import customtkinter as ctt
from PIL import Image
class Loading(ctt.CTkFrame):
    def __init__(self, master, width, height, **kwargs):
        super().__init__(master, width, height, **kwargs)

        imgBackground = ctt.CTkImage(light_image=Image.open(".\\img\\login\\loading.png"),
                                     dark_image=Image.open(".\\img\\login\\loading.png"),
                                     size=(1432, 805))

        self.background = ctt.CTkLabel(self, image=imgBackground, text="")
        self.background.place(x=0, y=0)

    def loginProcess(self):
        inputText = self.input.get()

class App(ctt.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1432x805")

        self.frameMyCloset = Loading(master=self, width=1432, height=805)
        self.frameMyCloset.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

if __name__ == "__main__":
    app = App()
    app.mainloop()
