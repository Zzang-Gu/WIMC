import io
from PIL import Image
import customtkinter as ctt

import etcDb
import popRegCloth
import popMdfCloth

class ClothInfo(ctt.CTkFrame):
    def __init__(self, master, row):
        super().__init__(master, width=194, height=225, fg_color="#F5F5ED")

        self.master = master

        self.row = row
        self.clothId = row[0]
        self.clothNm = row[1]
        self.clothImg = row[2]
        self.clothTpCd = row[3]
        self.clothTp = row[4]
        self.clothColorCd = row[5]
        self.clothColor = row[6]

        self.imgPola = ctt.CTkImage(light_image=Image.open(".\\img\\winMyCloset\\polaroid194x225.png"), dark_image=Image.open(".\\img\\winMyCloset\\polaroid194x225.png"), size=(194, 225))
        self.labelPola = ctt.CTkLabel(self, image=self.imgPola, text="")
        self.labelPola.grid()
        self.labelPola.bind("<Double-Button-1>", self.clickClothInfo)

        self.imgCloth = ctt.CTkImage(light_image=Image.open(io.BytesIO(self.clothImg)), dark_image=Image.open(io.BytesIO(self.clothImg)), size=(174, 178))
        self.labelCloth = ctt.CTkLabel(self, image=self.imgCloth, text="")
        self.labelCloth.place(x=10, y=10)
        self.labelCloth.bind("<Double-Button-1>", self.clickClothInfo)

        self.labelText = ctt.CTkLabel(self, text=self.clothNm, fg_color="#FFFFFF", width=180, height=20)
        self.labelText.place(x=7, y=190)
        self.labelText.bind("<Double-Button-1>", self.clickClothInfo)

    def clickClothInfo(self, event):
        if self.master.popup is None or not self.master.popup.winfo_exists():
            self.master.popup = popRegCloth.RegCloth(self.row)
        else:
            self.master.popup.focus()

class ClothList(ctt.CTkScrollableFrame):
    def __init__(self, master, width, height, userId):
        super().__init__(master, width, height, fg_color="#F5F5ED")

        self.userId = userId

        self.imgPola = ctt.CTkImage(light_image=Image.open(".\\img\\winMyCloset\\polaroid194x225.png"), dark_image=Image.open(".\\img\\winMyCloset\\polaroid194x225.png"), size=(194, 225))

        self.popup = None

        self.cloths = []
        self.showCloths("ALL")

    def showCloths(self, tpCd):
        columns, rows = etcDb.selectCloths(self.userId, tpCd)

        for _, cloth in enumerate(self.cloths):
            cloth.destroy()

        self.cloths = []

        for idx, row in enumerate(rows):
            frmClothInfo = ClothInfo(self, row)
            frmClothInfo.grid(row=idx//4, column=idx%4, padx=10, pady=10)

            self.cloths.append(frmClothInfo)

class MyCloset(ctt.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, width=1432, height=805, **kwargs)

        imgBackground = ctt.CTkImage(light_image=Image.open(".\\img\\winMyCloset\\background1432x805.png"), dark_image=Image.open(".\\img\\winMyCloset\\background1432x805.png"), size=(1432, 805))
        self.labelBackground = ctt.CTkLabel(self, image=imgBackground, text="")
        self.labelBackground.place(x=0, y=0)

        imgBack = ctt.CTkImage(light_image=Image.open(".\\img\\winMyCloset\\back54.75x50.25.png"), dark_image=Image.open(".\\img\\winMyCloset\\back54.75x50.25.png"), size=(55, 50))
        self.labelBack = ctt.CTkLabel(self, image=imgBack, text="", fg_color="#E3F2ED")
        self.labelBack.place(x=50, y=50)
        self.labelBack.bind("<Button-1>", self.clickBack)

        imgWindow = ctt.CTkImage(light_image=Image.open(".\\img\\winMyCloset\\window849x531.png"), dark_image=Image.open(".\\img\\winMyCloset\\window849x531.png"), size=(1121, 703))
        ctt.CTkLabel(self, image=imgWindow, fg_color="#E3F2ED", text="").place(x=155, y=61)

        ctt.CTkLabel(self, width=300, height=60, bg_color="#F5F5ED", fg_color="#F5F5ED", text="나의 옷방", font=("JalnanOTF", 45)).place(x=566, y=95)

        # ALL TOP BOTTOM SHOES
        btnAll = ctt.CTkButton(self, width=145, height=47, border_width=3, bg_color="#F5F5ED", fg_color="#FFFFFF", hover_color="#AAAAAA", border_color="#000000", text="전체", text_color="#000000", command= lambda: self.scrFrmClothList.showCloths("ALL"))
        btnTop = ctt.CTkButton(self, width=145, height=47, border_width=3, bg_color="#F5F5ED", fg_color="#FFFFFF", hover_color="#AAAAAA", border_color="#000000", text="상의", text_color="#000000", command= lambda: self.scrFrmClothList.showCloths("TOP"))
        btnBottom = ctt.CTkButton(self, width=145, height=47, border_width=3, bg_color="#F5F5ED", fg_color="#FFFFFF", hover_color="#AAAAAA", border_color="#000000", text="하의", text_color="#000000", command= lambda: self.scrFrmClothList.showCloths("BOTTOM"))
        btnShoes = ctt.CTkButton(self, width=145, height=47, border_width=3, bg_color="#F5F5ED", fg_color="#FFFFFF", hover_color="#AAAAAA", border_color="#000000", text="신발", text_color="#000000", command= lambda: self.scrFrmClothList.showCloths("SHOES"))

        btnAll.place(x=376, y=180)
        btnTop.place(x=551, y=180)
        btnBottom.place(x=736, y=180)
        btnShoes.place(x=911, y=180)

        imgTrash = ctt.CTkImage(light_image=Image.open(".\\img\\winMyCloset\\trash58x58.png"), dark_image=Image.open(".\\img\\winMyCloset\\trash58x58.png"), size=(58, 58))
        self.labelTrash = ctt.CTkLabel(self, image=imgTrash, fg_color="#F5F5ED", text="").place(x=1100, y=170)
        self.labelBack.bind("<Button-1>", self.clickTrash)

        self.scrFrmClothList = ClothList(self, width=855, height=500, userId=master.userId)
        self.scrFrmClothList.place(x=282, y=240)

    def clickBack(self, event):
        self.destroy()

    def clickTrash(self, event):
        print("Trash Click")

class App(ctt.CTk):
    def __init__(self):
        super().__init__()

        self.title("WIMC")
        self.geometry("1432x805")

        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)

        self.frmMyCloset = MyCloset(master=self, userId="20231662")
        self.frmMyCloset.grid()

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

