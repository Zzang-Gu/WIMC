import io
import customtkinter as ctt
from PIL import Image
from datetime import date, datetime, timedelta
from dateutil import relativedelta
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

        self.cmboxTop = ctt.CTkComboBox(self, values=self.topNames, state="readonly", command=self.updateClothImage)
        self.cmboxTop.set("")
        self.cmboxTop.place(x=270, y=618)

        self.bottomList = etcDb.selectCloths(self.master.userId, "BOTTOM")[1]
        self.bottomNames = list(map(lambda item: item[1], self.bottomList))

        self.cmboxBottom = ctt.CTkComboBox(self, values=self.bottomNames, state="readonly", command=self.updateClothImage)
        self.cmboxBottom.set("")
        self.cmboxBottom.place(x=653, y=618)

        self.shoesList = etcDb.selectCloths(self.master.userId, "SHOES")[1]
        self.shoesNames = list(map(lambda item: item[1], self.shoesList))

        self.cmboxShoes = ctt.CTkComboBox(self, values=self.shoesNames, state="readonly", command=self.updateClothImage)
        self.cmboxShoes.set("")
        self.cmboxShoes.place(x=1026, y=618)

        # self.targetDate = ctt.StringVar()
        # today = date.today().isoformat().replace("-", "")
        # self.targetDate.set(today)
        # self.dateInput = ctt.CTkEntry(self, textvariable=self.targetDate, placeholder_text="날짜 입력",
        #                                    bg_color="#ffffff", border_width=0, width=108, height=31)
        # self.dateInput.place(x=776, y=190)

        today = date.today().isoformat().replace("-", "")
        dateList = []
        for i in range(31):
            date1 = date.today() - timedelta(days=i)
            dateList.append(date1.isoformat().replace("-", ""))
        self.dateInput = ctt.CTkComboBox(self, values=dateList, state="readonly", command=self.initializeClothImage)
        self.dateInput.set(today)
        self.dateInput.place(x=776, y=190)

        self.initializeClothImage(None)

    def clickBack(self, event):
        self.destroy()

    def initializeClothImage(self, event):
        clothDetail = etcDb.selectClothsUseHistByDate(self.master.userId, self.dateInput.get())

        top = None
        bottom = None
        shoes = None

        for clothItem in clothDetail:
            if clothItem[4] == "TOP":
                top = clothItem
            elif clothItem[4] == "BOTTOM":
                bottom = clothItem
            elif clothItem[4] == "SHOES":
                shoes = clothItem

        defaultThumbnail = ctt.CTkImage(light_image=Image.open(".\\img\\daily\\itemThumbnail239x265.png"),
                                    dark_image=Image.open(".\\img\\daily\\itemThumbnail239x265.png"),
                                    size=(239, 265))

        topThumbnail = defaultThumbnail
        bottomThumbnail = defaultThumbnail
        shoesThumbnail = defaultThumbnail

        self.cmboxTop.set("")
        if top is not None:
            topThumbnail = ctt.CTkImage(light_image=Image.open(io.BytesIO(top[3])),
                                       dark_image=Image.open(io.BytesIO(top[3])),
                                       size=(239, 265))
            self.cmboxTop.set(top[2])

        self.cmboxBottom.set("")
        if bottom is not None:
            bottomThumbnail = ctt.CTkImage(light_image=Image.open(io.BytesIO(bottom[3])),
                                        dark_image=Image.open(io.BytesIO(bottom[3])),
                                        size=(239, 265))
            self.cmboxBottom.set(bottom[2])

        self.cmboxShoes.set("")
        if shoes is not None:
            shoesThumbnail = ctt.CTkImage(light_image=Image.open(io.BytesIO(shoes[3])),
                                        dark_image=Image.open(io.BytesIO(shoes[3])),
                                        size=(239, 265))
            self.cmboxShoes.set(shoes[2])


        self.topThumbnail = ctt.CTkLabel(self, image=topThumbnail, text="")
        self.topThumbnail.place(x=219, y=331)

        self.bottomThumbnail = ctt.CTkLabel(self, image=bottomThumbnail, text="")
        self.bottomThumbnail.place(x=595, y=331)

        self.shoesThumbnail = ctt.CTkLabel(self, image=shoesThumbnail, text="")
        self.shoesThumbnail.place(x=968, y=331)
    def updateClothImage(self, event):
        top = self.cmboxTop.get()
        bottom = self.cmboxBottom.get()
        shoes = self.cmboxShoes.get()

        defaultThumbnail = ctt.CTkImage(light_image=Image.open(".\\img\\daily\\itemThumbnail239x265.png"),
                                    dark_image=Image.open(".\\img\\daily\\itemThumbnail239x265.png"),
                                    size=(239, 265))

        topThumbnail = defaultThumbnail
        bottomThumbnail = defaultThumbnail
        shoesThumbnail = defaultThumbnail

        matchTopItem = list(filter(lambda item: item[1] == top, self.topList))
        if len(matchTopItem) > 0:
            topThumbnail = ctt.CTkImage(light_image=Image.open(io.BytesIO(matchTopItem[0][2])),
                                       dark_image=Image.open(io.BytesIO(matchTopItem[0][2])),
                                       size=(239, 265))

        matchBottomItem = list(filter(lambda item: item[1] == bottom, self.bottomList))
        if len(matchBottomItem) > 0:
            bottomThumbnail = ctt.CTkImage(light_image=Image.open(io.BytesIO(matchBottomItem[0][2])),
                                        dark_image=Image.open(io.BytesIO(matchBottomItem[0][2])),
                                        size=(239, 265))

        matchShoesItem = list(filter(lambda item: item[1] == shoes, self.shoesList))
        if len(matchShoesItem) > 0:
            shoesThumbnail = ctt.CTkImage(light_image=Image.open(io.BytesIO(matchShoesItem[0][2])),
                                        dark_image=Image.open(io.BytesIO(matchShoesItem[0][2])),
                                        size=(239, 265))


        self.topThumbnail = ctt.CTkLabel(self, image=topThumbnail, text="")
        self.topThumbnail.place(x=219, y=331)

        self.bottomThumbnail = ctt.CTkLabel(self, image=bottomThumbnail, text="")
        self.bottomThumbnail.place(x=595, y=331)

        self.shoesThumbnail = ctt.CTkLabel(self, image=shoesThumbnail, text="")
        self.shoesThumbnail.place(x=968, y=331)

    def registerDailyLook(self, event):
        top = self.cmboxTop.get()
        bottom = self.cmboxBottom.get()
        shoes = self.cmboxShoes.get()

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


        targetDate = self.dateInput.get()
        clothDetail = etcDb.selectClothsUseHistByDate(self.master.userId, targetDate)

        prevTop = None
        prevBottom = None
        prevShoes = None

        for clothItem in clothDetail:
            if clothItem[4] == "TOP":
                prevTop = clothItem
            elif clothItem[4] == "BOTTOM":
                prevBottom = clothItem
            elif clothItem[4] == "SHOES":
                prevShoes = clothItem

        if topClothId is not None:
            if prevTop is not None:
                etcDb.updateClothUseHist(targetDate, "TOP", topClothId, self.master.userId)
            else:
                etcDb.insertClothUseHist(targetDate, "TOP", topClothId, self.master.userId)

        if bottomClothId is not None:
            if prevBottom is not None:
                etcDb.updateClothUseHist(targetDate, "BOTTOM", bottomClothId, self.master.userId)
            else:
                etcDb.insertClothUseHist(targetDate, "BOTTOM", bottomClothId, self.master.userId)

        if shoesClothId is not None:
            if prevShoes is not None:
                etcDb.updateClothUseHist(targetDate, "SHOES", shoesClothId, self.master.userId)
            else:
                etcDb.insertClothUseHist(targetDate, "SHOES", shoesClothId, self.master.userId)

        self.master.info("데일리코디 등록", "등록 완료되었습니다.")
        self.clickBack(None)