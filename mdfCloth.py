import io

from PIL import Image
import customtkinter as ctt
from CTkMessagebox import CTkMessagebox as ctkmbox

import db

class MdfCloth(ctt.CTkFrame):
    def __init__(self, master, row, **kwargs):
        super().__init__(master, width=1432, height=805, **kwargs)

        self.master = master

        self.clothId = row[0]
        self.clothNm = row[1]
        self.clothImg = row[2]
        self.clothTpCd = row[3]
        self.clothTp = row[4]
        self.clothColorCd = row[5]
        self.clothColor = row[6]
        self.prchsDe = row[7]
        self.lastUseDe = row[8]

        self.colorCdList = []
        self.colorValueList = []

        colorList = db.selectColorCd()
        for _, color in enumerate(colorList):
            self.colorCdList.append(color[0])
            self.colorValueList.append(color[1])

        self.ctkImgBackground = ctt.CTkImage(light_image=Image.open(".\\img\\clothInfo\\background1432x805.png"), dark_image=Image.open(".\\img\\clothInfo\\background1432x805.png"), size=(1432, 805))
        self.labBackground = ctt.CTkLabel(self, image=self.ctkImgBackground, text="")
        self.labBackground.grid()

        ctkImgBack = ctt.CTkImage(light_image=Image.open(".\\img\\clothInfo\\back55x50.png"), dark_image=Image.open(".\\img\\clothInfo\\back55x50.png"), size=(55, 50))
        self.labBack = ctt.CTkLabel(self, image=ctkImgBack, text="", fg_color="#E3F2ED")
        self.labBack.place(x=50, y=50)
        self.labBack.bind("<Button-1>", self.clickBack)

        self.ctkImgFrame = ctt.CTkImage(light_image=Image.open(".\\img\\clothInfo\\frame634x682.png"), dark_image=Image.open(".\\img\\clothInfo\\frame634x682.png"), size=(634, 682))
        self.labFrame = ctt.CTkLabel(self, image=self.ctkImgFrame, bg_color="#E3F2ED", fg_color="#E3F2ED", text="")
        self.labFrame.place(x=399, y=62)

        ctt.CTkLabel(self, width=300, height=50, bg_color="#FFFFFF", fg_color="#FFFFFF", text="아이템 수정", font=("JalnanOTF", 30)).place(x=566, y=67)

        self.ctkImgCloth = ctt.CTkImage(light_image=Image.open(io.BytesIO(self.clothImg)), dark_image=Image.open(io.BytesIO(self.clothImg)), size=(216, 239))
        self.labCloth = ctt.CTkLabel(self, image=self.ctkImgCloth, text="")
        self.labCloth.place(x=209+399, y=55+62)

        self.ctkImgUpload = ctt.CTkImage(light_image=Image.open(".\\img\\clothInfo\\upload45x45.png"), dark_image=Image.open(".\\img\\clothInfo\\upload45x45.png"), size=(45, 45))
        self.labUpload = ctt.CTkLabel(self, image=self.ctkImgUpload, bg_color="#FFFFFF", fg_color="#FFFFFF", text="")
        self.labUpload.place(x=402+399, y=274+62)
        self.labUpload.bind("<Button-1>", self.clothUpload)

        if self.clothTpCd == "TOP":
            radioVar = ctt.IntVar(value=1)
        elif self.clothTpCd == "BOTTOM":
            radioVar = ctt.IntVar(value=2)
        elif self.clothTpCd == "SHOES":
            radioVar = ctt.IntVar(value=3)
        else:
            radioVar = ctt.IntVar(value=0)

        ctt.CTkLabel(self, width=100, height=30, bg_color="#FFFFFF", fg_color="#FFFFFF", text="카테고리", font=("JalnanOTF", 20)).place(x=79+399, y=325+62)
        ctt.CTkRadioButton(self, variable=radioVar, value=1, bg_color="#FFFFFF", text="상의", command=lambda: self.mdfTpCd("TOP")).place(x=209+399, y=329+62)
        ctt.CTkRadioButton(self, variable=radioVar, value=2, bg_color="#FFFFFF", text="하의", command=lambda: self.mdfTpCd("BOTTOM")).place(x=309+399, y=329+62)
        ctt.CTkRadioButton(self, variable=radioVar, value=3, bg_color="#FFFFFF", text="신발", command=lambda: self.mdfTpCd("SHOES")).place(x=409+399, y=329+62)

        self.ctkImgUnderLine = ctt.CTkImage(light_image=Image.open(".\\img\\clothInfo\\underLine338x2.png"), dark_image=Image.open(".\\img\\clothInfo\\underLine338x2.png"), size=(338, 2))

        ctt.CTkLabel(self, width=100, height=30, bg_color="#FFFFFF", fg_color="#FFFFFF", text="아이템명", font=("JalnanOTF", 20)).place(x=79+399, y=380+62)
        ctt.CTkLabel(self, image=self.ctkImgUnderLine, bg_color="#FFFFFF", fg_color="#FFFFFF", text="").place(x=209+399, y=400+62)
        sVarClothNm = ctt.StringVar()
        sVarClothNm.set(self.clothNm)
        self.entClothNm = ctt.CTkEntry(self, width=338, height=30, border_width=0, bg_color="#FFFFFF", textvariable=sVarClothNm)
        self.entClothNm.place(x=209+399, y=380+62)

        ctt.CTkLabel(self, width=100, height=30, bg_color="#FFFFFF", fg_color="#FFFFFF", text="색상", font=("JalnanOTF", 20)).place(x=79+399, y=435+62)
        self.cmboxColor = ctt.CTkComboBox(self, values=self.colorValueList, state="readonly")
        self.cmboxColor.set(self.clothColor)
        self.cmboxColor.place(x=209+399, y=436+62)

        ctt.CTkLabel(self, width=100, height=30, bg_color="#FFFFFF", fg_color="#FFFFFF", text="구입날짜", font=("JalnanOTF", 20)).place(x=79+399, y=490+62)
        ctt.CTkLabel(self, image=self.ctkImgUnderLine, bg_color="#FFFFFF", fg_color="#FFFFFF", text="").place(x=209+399, y=510+62)
        sVarPrchsDe = ctt.StringVar()
        sVarPrchsDe.set(self.prchsDe)
        self.entPrchsDe = ctt.CTkEntry(self, width=338, height=30, border_width=0, bg_color="#FFFFFF", textvariable=sVarPrchsDe)
        self.entPrchsDe.place(x=209+399, y=490+62)

        ctt.CTkLabel(self, width=100, height=30, bg_color="#FFFFFF", fg_color="#FFFFFF", text="사용날짜", font=("JalnanOTF", 20)).place(x=79+399, y=545+62)
        ctt.CTkLabel(self, width=338, height=30, bg_color="#FFFFFF", fg_color="#FFFFFF", text=self.lastUseDe, anchor="w").place(x=216+399, y=545+62)

        btnReg = ctt.CTkButton(self, width=145, height=47, border_width=3, bg_color="#F5F5ED", fg_color="#FFFFFF", hover_color="#AAAAAA", border_color="#000000", text="수정", text_color="#000000", command=self.saveCloth)
        btnReg.place(x=245+399, y=600+62)

    def clickBack(self, event):
        self.destroy()

    def mdfTpCd(self, tpCd):
        self.clothTpCd = tpCd

    def clothUpload(self, event):
        fileNm = ctt.filedialog.askopenfilename(initialdir="/", title = "파일을 선택 해 주세요", filetypes = (("*.png","*png"), ("*.jpg", "*jpg"), ("*.jpeg", "*jpeg")))

        file = open(fileNm, "rb")
        self.clothImg = file.read()

        self.ctkImgCloth = ctt.CTkImage(light_image=Image.open(io.BytesIO(self.clothImg)), dark_image=Image.open(io.BytesIO(self.clothImg)), size=(216, 239))
        self.labCloth.configure(image=self.ctkImgCloth)

    def saveCloth(self):
        self.clothNm = self.entClothNm.get()
        self.clothColorCd = self.colorCdList[self.colorValueList.index(self.cmboxColor.get())]
        self.prchsDe = self.entPrchsDe.get()

        msg = ctkmbox(title="확인", message="수정한 정보를 저장하시겠습니까?", icon="question", option_1="Cancel", option_2="No", option_3="Yes")
        response = msg.get()

        if response=="Yes":
            db.updateCloth(self.clothId, self.clothNm, self.clothImg, self.clothTpCd, self.clothColorCd, self.prchsDe, self.lastUseDe)

            ctkmbox(title="정보", message="수정되었습니다.")

            self.master.scrFrmClothList.showCloths()

            self.destroy()
        elif response=="No":
            self.master.scrFrmClothList.showCloths()
            self.destroy()
