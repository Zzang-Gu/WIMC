import io

from PIL import Image
import customtkinter as ctt
from CTkMessagebox import CTkMessagebox as ctkmbox

class AmpColorCodeInfo(ctt.CTkFrame):
    def __init__(self, master, imgColorCd):
        super().__init__(master, width=500, height=500, fg_color="#F5F5ED")

        self.master = master

        imgBackground = ctt.CTkImage(light_image=Image.open(".\\img\\colorCd\\ampbackground634x682.png"), dark_image=Image.open(".\\img\\colorCd\\ampbackground634x682.png"), size=(500, 500))
        self.labelBackground = ctt.CTkLabel(self, image=imgBackground, text="")
        self.labelBackground.grid()
        self.labelBackground.bind("<Button-1>", self.clickEventHandler)

        self.imgColorCd = ctt.CTkImage(light_image=Image.open(io.BytesIO(imgColorCd)), dark_image=Image.open(io.BytesIO(imgColorCd)), size=(400, 400))
        self.labelColorCdInfo = ctt.CTkLabel(self, image=self.imgColorCd, text="")
        self.labelColorCdInfo.place(x=50, y=50)
        self.labelColorCdInfo.bind("<Button-1>", self.clickEventHandler)

    def clickEventHandler(self, event):
        self.destroy()

class ColorCodeInfo(ctt.CTkFrame):
    def __init__(self, master, imgColorCd):
        super().__init__(master, width=225, height=225, fg_color="#F5F5ED")

        self.master = master

        self.imgColorCd = imgColorCd

        self.ctkImgColorCd = ctt.CTkImage(light_image=Image.open(io.BytesIO(self.imgColorCd)), dark_image=Image.open(io.BytesIO(self.imgColorCd)), size=(225, 225))
        self.labelColorCdInfo = ctt.CTkLabel(self, image=self.ctkImgColorCd, text="")
        self.labelColorCdInfo.grid()
        self.labelColorCdInfo.bind("<Double-Button-1>", self.clickColorCdInfo)

    def clickColorCdInfo(self, event):
        AmpColorCodeInfo(self.master.master, self.imgColorCd).place(x=466, y=206)

class ColorCodeList(ctt.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, width=1000, height=500, fg_color="#F5F5ED")

        self.master = master
        self.imgColorCdList = []

        for idx in range(14):
            self.imgColorCdList.append(open(".\\img\\colorCd\\colorCode%02d.jpg" % int(idx + 1), "rb").read())

        for idx, imgColorCd in enumerate(self.imgColorCdList):
            ColorCodeInfo(self, imgColorCd).grid(row=idx//4, column=idx%4, padx=10, pady=25)

class ColorCode(ctt.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, width=1432, height=805, **kwargs)

        self.master = master

        imgBackground = ctt.CTkImage(light_image=Image.open(".\\img\\myCloset\\background1432x805.png"), dark_image=Image.open(".\\img\\myCloset\\background1432x805.png"), size=(1432, 805))
        self.labelBackground = ctt.CTkLabel(self, image=imgBackground, text="")
        self.labelBackground.grid()

        imgBack = ctt.CTkImage(light_image=Image.open(".\\img\\myCloset\\back55x50.png"), dark_image=Image.open(".\\img\\myCloset\\back55x50.png"), size=(55, 50))
        self.labelBack = ctt.CTkLabel(self, image=imgBack, text="", fg_color="#E3F2ED")
        self.labelBack.place(x=50, y=50)
        self.labelBack.bind("<Button-1>", self.clickBack)

        imgWindow = ctt.CTkImage(light_image=Image.open(".\\img\\myCloset\\frame849x531.png"), dark_image=Image.open(".\\img\\myCloset\\frame849x531.png"), size=(1121, 703))
        ctt.CTkLabel(self, image=imgWindow, fg_color="#E3F2ED", text="").place(x=155, y=61)

        ctt.CTkLabel(self, width=400, height=60, bg_color="#F5F5ED", fg_color="#F5F5ED", text="옷 컬러 추천 조합", font=("JalnanOTF", 45)).place(x=516, y=110)

        self.scrFrmColorCdList = ColorCodeList(self)
        self.scrFrmColorCdList.place(x=216, y=200)

    def clickBack(self, event):
        self.destroy()

class App(ctt.CTk):
    def __init__(self):
        super().__init__()

        self.title("WIMC")
        self.geometry("1432x805")

        self.userId = "20231662"

        self.frmMyCloset = ColorCode(self)
        self.frmMyCloset.grid()

if __name__ == "__main__":
    app = App()
    app.mainloop()
