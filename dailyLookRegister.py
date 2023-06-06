import customtkinter as ctt
from PIL import Image
from datetime import date, datetime
import etcDb

# pages

class DailyLookRegister(ctt.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, 1432, 805, **kwargs)
        self.master = master

        self.initialize()

    def initialize(self):
        # background
        background = ctt.CTkImage(light_image=Image.open(".\\img\\daily\\background1432x805.png"),
                                  dark_image=Image.open(".\\img\\daily\\background1432x805.png"),
                                  size=(1432, 805))

        self.background = ctt.CTkLabel(self, image=background, text="")
        self.background.place(x=0, y=0)

        modalFrame = ctt.CTkImage(light_image=Image.open(".\\img\\daily\\frame849x531.png"),
                                  dark_image=Image.open(".\\img\\daily\\frame849x531.png"),
                                  size=(1121, 703))

        self.modalFrame = ctt.CTkLabel(self, image=modalFrame, text="", fg_color="#E3F2ED")
        self.modalFrame.place(x=155, y=61)

        imgBack = ctt.CTkImage(light_image=Image.open(".\\img\\myCloset\\back55x50.png"),
                               dark_image=Image.open(".\\img\\myCloset\\back55x50.png"), size=(55, 50))
        self.labelBack = ctt.CTkLabel(self, image=imgBack, text="", fg_color="#E3F2ED")
        self.labelBack.place(x=50, y=50)
        self.labelBack.bind("<Button-1>", self.clickBack)

        titleImage = ctt.CTkImage(light_image=Image.open(".\\img\\daily\\title327x44.png"),
                                  dark_image=Image.open(".\\img\\daily\\title327x44.png"),
                                  size=(327, 44))
        self.title = ctt.CTkLabel(self, image=titleImage, text="")
        self.title.place(x=552, y=98)


        # 일자 선택
        dateLabel = ctt.CTkImage(light_image=Image.open(".\\img\\daily\\dateLabel147x47.png"),
                                  dark_image=Image.open(".\\img\\daily\\dateLabel147x47.png"),
                                  size=(147, 47))
        self.dateLabel = ctt.CTkLabel(self, image=dateLabel, text="")
        self.dateLabel.place(x=514, y=182)


        # 상의, 하의, 신발 라벨
        topLabel = ctt.CTkImage(light_image=Image.open(".\\img\\daily\\topLabel146x47.png"),
                                dark_image=Image.open(".\\img\\daily\\topLabel146x47.png"),
                                size=(146, 47))
        self.topLabel = ctt.CTkLabel(self, image=topLabel, text="")
        self.topLabel.place(x=266, y=264)

        bottomLabel = ctt.CTkImage(light_image=Image.open(".\\img\\daily\\bottom146x47.png"),
                                 dark_image=Image.open(".\\img\\daily\\bottom146x47.png"),
                                 size=(146, 47))
        self.bottomLabel = ctt.CTkLabel(self, image=bottomLabel, text="")
        self.bottomLabel.place(x=642, y=264)

        shoesLabel = ctt.CTkImage(light_image=Image.open(".\\img\\daily\\shoes146x47.png"),
                                 dark_image=Image.open(".\\img\\daily\\shoes146x47.png"),
                                 size=(146, 47))
        self.shoesLabel = ctt.CTkLabel(self, image=shoesLabel, text="")
        self.shoesLabel.place(x=1015, y=264)

        # 상의, 항의, 신발 사진
        topThumbnail = ctt.CTkImage(light_image=Image.open(".\\img\\daily\\itemThumbnail239x265.png"),
                                  dark_image=Image.open(".\\img\\daily\\itemThumbnail239x265.png"),
                                  size=(239, 265))
        self.topThumbnail = ctt.CTkLabel(self, image=topThumbnail, text="")
        self.topThumbnail.place(x=219, y=331)

        bottomThumbnail = ctt.CTkImage(light_image=Image.open(".\\img\\daily\\itemThumbnail239x265.png"),
                                    dark_image=Image.open(".\\img\\daily\\itemThumbnail239x265.png"),
                                    size=(239, 265))
        self.bottomThumbnail = ctt.CTkLabel(self, image=bottomThumbnail, text="")
        self.bottomThumbnail.place(x=595, y=331)

        shoesThumbnail = ctt.CTkImage(light_image=Image.open(".\\img\\daily\\itemThumbnail239x265.png"),
                                    dark_image=Image.open(".\\img\\daily\\itemThumbnail239x265.png"),
                                    size=(239, 265))
        self.shoesThumbnail = ctt.CTkLabel(self, image=shoesThumbnail, text="")
        self.shoesThumbnail.place(x=968, y=331)

        # 등록 버튼
        registerButton = ctt.CTkImage(light_image=Image.open(".\\img\\daily\\registerButton148x41.png"),
                                      dark_image=Image.open(".\\img\\daily\\registerButton148x41.png"),
                                      size=(148, 41))
        self.registerButton = ctt.CTkLabel(self, image=registerButton, text="")
        self.registerButton.place(x=642, y=685)
        self.registerButton.bind("<Button-1>", self.registerDailyLook)

        # 상의, 하의, 신발 선택
        self.topList = etcDb.selectCloths(self.master.userId, "TOP")[1]
        self.topNames = list(map(lambda item: item[1], self.topList))

        self.cmboxTop = ctt.CTkComboBox(self, values=self.topNames, state="readonly")
        self.cmboxTop.set("")
        self.cmboxTop.place(x=270, y=618)

        self.bottomList = etcDb.selectCloths(self.master.userId, "BOTTOM")[1]
        self.bottomNames = list(map(lambda item: item[1], self.bottomList))
        self.cmboxBottom = ctt.CTkComboBox(self, values=self.bottomNames, state="readonly")
        self.cmboxBottom.set("")
        self.cmboxBottom.place(x=653, y=618)

        self.shoesList = etcDb.selectCloths(self.master.userId, "SHOES")[1]
        self.shoesNames = list(map(lambda item: item[1], self.shoesList))
        self.cmboxShoes = ctt.CTkComboBox(self, values=self.shoesNames, state="readonly")
        self.cmboxShoes.set("")
        self.cmboxShoes.place(x=1026, y=618)

        self.targetDate = ctt.StringVar()
        today = date.today().isoformat().replace("-", "")
        self.targetDate.set(today)
        self.dateInput = ctt.CTkEntry(self, textvariable=self.targetDate, placeholder_text="날짜 입력",
                                           bg_color="#ffffff", border_width=0, width=108, height=31)
        self.dateInput.place(x=776, y=190)

    def clickBack(self, event):
        self.destroy()

    def registerDailyLook(self, event):
        top = self.cmboxTop.get()
        bottom = self.cmboxBottom.get()
        shoes = self.cmboxShoes.get()
        targetDate = self.targetDate.get()

        if targetDate == "":
            self.master.alert("등록 오류", "날짜를 입력해주세요. ex) 20230608")
            return

        isValidDate = False
        try:
            datetime.strptime(targetDate, "%Y%m%d")
            isValidDate = True
        except ValueError as ve:
            print("날짜 형식 오류")

        if isValidDate == False:
            self.master.alert("데일리코디 등록", "올바른 날짜를 입력해주세요. ex) 20230608")
            return

        if top == "" and bottom == "" and shoes == "":
            self.master.alert("데일리코디 등록", "1개 이상의 옷을 선택해주세요")
            return

        topClothId = None
        matchTopItem = list(filter(lambda item: item[1] == top, self.topList))
        if len(matchTopItem) > 0:
            topClothId = matchTopItem[0][0]

        bottomClothId = None
        matchBottomItem = list(filter(lambda item: item[1] == bottom, self.bottomList))
        if len(matchBottomItem) > 0:
            bottomClothId = matchBottomItem[0][0]

        shoesClothId = None
        matchShoesItem = list(filter(lambda item: item[1] == shoes, self.shoesList))
        if len(matchShoesItem) > 0:
            shoesClothId = matchShoesItem[0][0]

        if topClothId is not None:
            etcDb.insertClothUseHist(targetDate, "TOP", topClothId, self.master.userId)

        if bottomClothId is not None:
            etcDb.insertClothUseHist(targetDate, "BOTTOM", bottomClothId, self.master.userId)

        if shoesClothId is not None:
            etcDb.insertClothUseHist(targetDate, "SHOES", shoesClothId, self.master.userId)

        self.master.info("데일리코디 등록", "등록 완료되었습니다.")
        self.clickBack(None)