import io

from PIL import Image
import customtkinter as ctt
from CTkMessagebox import CTkMessagebox as ctkmbox

import db
import mdfCloth

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

        self.ctkImgPola = ctt.CTkImage(light_image=Image.open(".\\img\\myCloset\\polaroid194x225.png"), dark_image=Image.open(".\\img\\myCloset\\polaroid194x225.png"), size=(194, 225))
        self.labPola = ctt.CTkLabel(self, image=self.ctkImgPola, text="")
        self.labPola.grid()
        self.labPola.bind("<Double-Button-1>", self.clickClothInfo)

        self.ctkImgCloth = ctt.CTkImage(light_image=Image.open(io.BytesIO(self.clothImg)), dark_image=Image.open(io.BytesIO(self.clothImg)), size=(174, 178))
        self.labCloth = ctt.CTkLabel(self, image=self.ctkImgCloth, text="")
        self.labCloth.place(x=10, y=10)
        self.labCloth.bind("<Double-Button-1>", self.clickClothInfo)

        self.labText = ctt.CTkLabel(self, width=180, height=20, fg_color="#FFFFFF", text=self.clothNm)
        self.labText.place(x=7, y=190)
        self.labText.bind("<Double-Button-1>", self.clickClothInfo)

        self.chkboxTrash = ctt.CTkCheckBox(self, width=0, height=0, onvalue="on", offvalue="off", text="", command=self.udtChkList)

        if self.master.master.isTrash:
            self.chkboxTrash.place(x=0, y=0)

    def clickClothInfo(self, event):
        mdfCloth.MdfCloth(self.master.master, self.row).place(x=0, y=0)

    def udtChkList(self):
        chkVal = self.chkboxTrash.get()

        if chkVal == "on":
            self.master.chkClothList.append(self.clothId)
        else:
            self.master.chkClothList.remove(self.clothId)

class ClothList(ctt.CTkScrollableFrame):
    def __init__(self, master, userId):
        super().__init__(master, width=855, height=500, fg_color="#F5F5ED")

        self.master = master
        self.userId = userId
        self.tpCd = "ALL"
        self.popup = None
        self.clothList = []
        self.chkClothList = []

        self.showCloths("ALL")

    def showCloths(self, tpCd=None):
        if tpCd is not None:
            self.tpCd = tpCd

        _, rows = db.selectCloths(self.userId, self.tpCd)

        for _, cloth in enumerate(self.clothList):
            cloth.destroy()

        self.clothList = []

        for idx, row in enumerate(rows):
            frmClothInfo = ClothInfo(self, row)
            frmClothInfo.grid(row=idx//4, column=idx%4, padx=10, pady=10)

            self.clothList.append(frmClothInfo)

class MyCloset(ctt.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, width=1432, height=805, **kwargs)

        self.master = master

        self.ctkImgBackground = ctt.CTkImage(light_image=Image.open(".\\img\\myCloset\\background1432x805.png"), dark_image=Image.open(".\\img\\myCloset\\background1432x805.png"), size=(1432, 805))
        self.labBackground = ctt.CTkLabel(self, image=self.ctkImgBackground, text="")
        self.labBackground.grid()

        self.ctkImgBack = ctt.CTkImage(light_image=Image.open(".\\img\\myCloset\\back55x50.png"), dark_image=Image.open(".\\img\\myCloset\\back55x50.png"), size=(55, 50))
        self.labBack = ctt.CTkLabel(self, image=self.ctkImgBack, fg_color="#E3F2ED", text="")
        self.labBack.place(x=50, y=50)
        self.labBack.bind("<Button-1>", self.clickBack)

        ctkImgFrame = ctt.CTkImage(light_image=Image.open(".\\img\\myCloset\\frame849x531.png"), dark_image=Image.open(".\\img\\myCloset\\frame849x531.png"), size=(1121, 703))
        ctt.CTkLabel(self, image=ctkImgFrame, fg_color="#E3F2ED", text="").place(x=155, y=61)

        ctt.CTkLabel(self, width=300, height=60, bg_color="#F5F5ED", fg_color="#F5F5ED", text="나의 옷장", font=("JalnanOTF", 45)).place(x=566, y=95)

        # ALL TOP BOTTOM SHOES
        btnAll = ctt.CTkButton(self, width=145, height=47, border_width=3, bg_color="#F5F5ED", fg_color="#FFFFFF", hover_color="#AAAAAA", border_color="#000000", text="전체", text_color="#000000", command= lambda: self.scrFrmClothList.showCloths("ALL"))
        btnTop = ctt.CTkButton(self, width=145, height=47, border_width=3, bg_color="#F5F5ED", fg_color="#FFFFFF", hover_color="#AAAAAA", border_color="#000000", text="상의", text_color="#000000", command= lambda: self.scrFrmClothList.showCloths("TOP"))
        btnBottom = ctt.CTkButton(self, width=145, height=47, border_width=3, bg_color="#F5F5ED", fg_color="#FFFFFF", hover_color="#AAAAAA", border_color="#000000", text="하의", text_color="#000000", command= lambda: self.scrFrmClothList.showCloths("BOTTOM"))
        btnShoes = ctt.CTkButton(self, width=145, height=47, border_width=3, bg_color="#F5F5ED", fg_color="#FFFFFF", hover_color="#AAAAAA", border_color="#000000", text="신발", text_color="#000000", command= lambda: self.scrFrmClothList.showCloths("SHOES"))

        btnAll.place(x=376, y=180)
        btnTop.place(x=551, y=180)
        btnBottom.place(x=736, y=180)
        btnShoes.place(x=911, y=180)

        self.isTrash = False
        self.ctkImgTrash = ctt.CTkImage(light_image=Image.open(".\\img\\myCloset\\trash58x58.png"), dark_image=Image.open(".\\img\\myCloset\\trash58x58.png"), size=(58, 58))
        self.labTrash = ctt.CTkLabel(self, image=self.ctkImgTrash, fg_color="#F5F5ED", text="")
        self.labTrash.place(x=1100, y=170)
        self.labTrash.bind("<Button-1>", self.clickTrash)

        self.scrFrmClothList = ClothList(self, userId=master.userId)
        self.scrFrmClothList.place(x=282, y=240)

    def clickBack(self, event):
        self.destroy()

    def clickTrash(self, event):
        if self.isTrash:
            if self.scrFrmClothList.chkClothList:
                msg = ctkmbox(title="확인", message="선택한 아이템들을 삭제하시겠습니까?", icon="question", option_1="Cancel", option_2="No", option_3="Yes")
                response = msg.get()

                if response=="Yes":
                    db.deleteCloths(self.scrFrmClothList.chkClothList)

                    self.scrFrmClothList.chkClothList = []
                    self.isTrash = False
                    self.scrFrmClothList.showCloths()
                elif response=="No":
                    self.scrFrmClothList.chkClothList = []
                    self.isTrash = False
                    self.scrFrmClothList.showCloths()
            else:
                self.isTrash = False
                self.scrFrmClothList.showCloths()
        else:
            self.isTrash = True
            self.scrFrmClothList.showCloths()
