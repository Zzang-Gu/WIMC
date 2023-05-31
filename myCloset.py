import io
import customtkinter as ctt
from PIL import Image

import db

class ClothInfo(ctt.CTkFrame):
    def __init__(self, master, row):
        super().__init__(master, width=194, height=225, fg_color="#F5F5ED")

        self.clothId = row[0]
        self.clothNm = row[1]
        self.clothImg = row[2]
        self.clothTp = row[3]
        self.clothColor = row[4]

        self.imgPola = ctt.CTkImage(light_image=Image.open(".\\img\\myCloset\\polaroid194x225.png"), dark_image=Image.open(".\\img\\myCloset\\polaroid194x225.png"), size=(194, 225))
        ctt.CTkLabel(self, image=self.imgPola, text="").grid()

        self.imgCloth = ctt.CTkImage(light_image=Image.open(io.BytesIO(self.clothImg)), dark_image=Image.open(io.BytesIO(self.clothImg)), size=(174, 178))
        ctt.CTkLabel(self, image=self.imgCloth, text="").place(x=10, y=10)

        ctt.CTkLabel(self, text=self.clothNm, fg_color="#FFFFFF", width=180, height=20).place(x=7, y=190)

class ClothList(ctt.CTkScrollableFrame):
    def __init__(self, master, width, height, userId):
        super().__init__(master, width, height, fg_color="#F5F5ED")

        self.userId = userId

        self.imgPola = ctt.CTkImage(light_image=Image.open(".\\img\\myCloset\\polaroid194x225.png"), dark_image=Image.open(".\\img\\myCloset\\polaroid194x225.png"), size=(194, 225))

        # TOP BOTTOM SHOES
        self.tpCd = "TOP"

        self.showCloths()

    def showCloths(self):
        # self.cloths = []

        columns, rows = db.selectCloths(self.userId, self.tpCd)

        for idx, row in enumerate(rows):
            frmClothInfo = ClothInfo(self, row)
            frmClothInfo.grid(row=idx//4, column=idx%4, padx=10, pady=10)

    def refresh(self):
        self.showCloths()

class MyCloset(ctt.CTkFrame):
    def __init__(self, master, userId, **kwargs):
        super().__init__(master, width=1432, height=805, **kwargs)

        imgBackground = ctt.CTkImage(light_image=Image.open(".\\img\\myCloset\\background1432x805.png"), dark_image=Image.open(".\\img\\myCloset\\background1432x805.png"), size=(1432, 805))
        self.labelBackground = ctt.CTkLabel(self, image=imgBackground, text="")
        self.labelBackground.place(x=0, y=0)

        imgWindow = ctt.CTkImage(light_image=Image.open(".\\img\\myCloset\\window849x531.png"), dark_image=Image.open(".\\img\\myCloset\\window849x531.png"), size=(1121, 703))
        ctt.CTkLabel(self, image=imgWindow, text="", fg_color="transparent").place(x=155, y=61)

        self.scrFrmClothList = ClothList(self, width=855, height=500, userId=userId)
        self.scrFrmClothList.place(x=289, y=240)

        btnTop = ctt.CTkButton(self, text="상의", width=145, height=47)
        btnBottom = ctt.CTkButton(self, text="하의", width=145, height=47)
        btnShoes = ctt.CTkButton(self, text="신발", width=145, height=47)
        btnTop.place(x=0, y=0)
        btnBottom.place(x=200, y=0)
        btnShoes.place(x=400, y=0)

class App(ctt.CTk):
    def __init__(self):
        super().__init__()

        self.title("WIMC")
        self.geometry("1432x805")

        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)

        self.frmMyCloset = MyCloset(master=self, userId="20231662")
        self.frmMyCloset.place(x=0, y=0)

if __name__ == "__main__":
    app = App()
    app.mainloop()

    # app = ctt.CTk()
    # app.title("my app")
    # app.geometry("400x150")

    # button = ctt.CTkButton(app, text="my button")
    # button.grid(row=0, column=0, padx=20, pady=20)

    # label = ctt.CTkLabel(app, text="CTkLabel", fg_color="transparent")
    # label.grid(row=0, column=1, padx=20, pady=20)

    # app.mainloop()

