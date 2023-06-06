import io
from dateutil import relativedelta
from datetime import date, datetime, timedelta

from PIL import Image
import customtkinter as ctt

import db

class MonthlyCody(ctt.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, 1432, 805, **kwargs)
        self.master = master

        self.today = datetime.today()
        self.year = self.today.year
        self.month = self.today.month
        self.day = self.today.day

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

        modalFrame2 = ctt.CTkImage(light_image=Image.open("img/monthlyCody/frame2_900x632.png"),
                                   dark_image=Image.open("img/monthlyCody/frame2_900x632.png"),
                                   size=(900, 632))

        self.modalFrame2 = ctt.CTkLabel(self, image=modalFrame2, text="", fg_color="#E3F2ED")
        self.modalFrame2.place(x=266, y=119)

        imgBack = ctt.CTkImage(light_image=Image.open(".\\img\\myCloset\\back55x50.png"),
                               dark_image=Image.open(".\\img\\myCloset\\back55x50.png"), size=(55, 50))
        self.labelBack = ctt.CTkLabel(self, image=imgBack, text="", fg_color="#E3F2ED")
        self.labelBack.place(x=50, y=50)
        self.labelBack.bind("<Button-1>", self.clickBack)

        # 이전, 다음 달 버튼
        prevButton = ctt.CTkImage(light_image=Image.open(".\\img\\monthlyCody\\prevButton36x44.png"),
                                  dark_image=Image.open(".\\img\\monthlyCody\\prevButton36x44.png"),
                                  size=(36, 44))
        self.prevButton = ctt.CTkLabel(self, image=prevButton, text="")
        self.prevButton.place(x=218, y=149)
        self.prevButton.bind("<Button-1>", self.prevMonth)

        nextButton = ctt.CTkImage(light_image=Image.open(".\\img\\monthlyCody\\nextButton36x42.png"),
                                  dark_image=Image.open(".\\img\\monthlyCody\\nextButton36x42.png"),
                                  size=(36, 44))
        self.nextButton = ctt.CTkLabel(self, image=nextButton, text="")
        self.nextButton.place(x=1186, y=152)
        self.nextButton.bind("<Button-1>", self.nextMonth)


        self.monthLabel = ctt.CTkLabel(self, text=self.month, bg_color="#f5f5ed", fg_color="#f5f5ed", text_color="#042f95", font=("Arial", 72), width=132)
        self.monthLabel.place(x=634, y=138)

        monthTextList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        monthText = monthTextList[self.month - 1]

        self.monthLabel2 = ctt.CTkLabel(self, text=monthText, bg_color="#f5f5ed", fg_color="#f5f5ed",
                                       text_color="#042f95", font=("Arial", 24), width=132, height=27)
        self.monthLabel2.place(x=634, y=210)

        self.monthLabel = ctt.CTkLabel(self, text=self.year, bg_color="#f5f5ed", fg_color="#f5f5ed",
                                       text_color="#042f95", font=("Arial", 16))
        self.monthLabel.place(x=849, y=227)

        firstWeekday = datetime(year=self.year, month=self.month, day=1).weekday()
        currentDate = datetime(year=self.year, month=self.month, day=1).date()
        lastDate = currentDate + relativedelta.relativedelta(month=1) - timedelta(days=1)

        clothList = db.selectClothsUseHist(self.master.userId)
        clothList = list(filter(lambda item: datetime.fromisoformat(item[0]).year == self.year and datetime.fromisoformat(item[0]).month == self.month, clothList))

        self.dayFont = ctt.CTkFont(family="Arial", size=16, weight="bold")
        for i in range(lastDate.day):
            self.drawDay(clothList, firstWeekday, i)

    def drawDay(self, clothList, firstWeekday, i):
        day = ctt.CTkLabel(self, text=str(i + 1), bg_color="#f5f5ed", text_color="#042f95", font=self.dayFont, width=60,
                           height=60)
        isClothExists = list(filter(lambda item: datetime.fromisoformat(item[0]).day == (i + 1), clothList))
        if len(isClothExists) > 0:
            dayImage = ctt.CTkImage(light_image=Image.open(".\\img\\monthlyCody\\dateActive.png"),
                                    dark_image=Image.open(".\\img\\monthlyCody\\dateActive.png"),
                                    size=(60, 60))
            day = ctt.CTkLabel(self, text=str(i + 1), bg_color="#f5f5ed", text_color="#042f95", font=self.dayFont,
                               width=60, height=60, image=dayImage)
            day.bind("<Button-1>", lambda _: self.detailHist(self.year, self.month, i + 1))
        day.place(x=274 + ((i + firstWeekday) % 7 * 128) + 30, y=348 + ((i + firstWeekday) // 7 * 67) + 1)

    def clickBack(self, event):
        self.destroy()

    def prevMonth(self, event):
        self.month = self.month - 1
        if self.month < 1:
            self.month = 12
            self.year -= 1

        self.initialize()

    def nextMonth(self, event):
        self.month = self.month + 1
        if self.month > 12:
            self.month = 1
            self.year += 1

        self.initialize()

    def detailHist(self, year, month, day):
        # background
        detailBackground = ctt.CTkImage(light_image=Image.open(".\\img\\daily\\background1432x805.png"),
                                  dark_image=Image.open(".\\img\\daily\\background1432x805.png"),
                                  size=(1432, 805))

        self.detailBackground = ctt.CTkLabel(self, image=detailBackground, text="")
        self.detailBackground.place(x=0, y=0)

        detailModalFrame = ctt.CTkImage(light_image=Image.open(".\\img\\clothInfo\\frame634x682.png"),
                                          dark_image=Image.open(".\\img\\clothInfo\\frame634x682.png"), size=(634, 682))
        self.detailModalFrame = ctt.CTkLabel(self, image=detailModalFrame, bg_color="#E3F2ED", fg_color="#E3F2ED",
                                            text="")
        self.detailModalFrame.place(x=399, y=62)

        detailModalFrame2 = ctt.CTkImage(light_image=Image.open(".\\img\\useHistDetail\\frame3.png"),
                                  dark_image=Image.open(".\\img\\useHistDetail\\frame3.png"),
                                  size=(514, 625))

        self.detailModalFrame2 = ctt.CTkLabel(self, image=detailModalFrame2, text="", fg_color="#E3F2ED")
        self.detailModalFrame2.place(x=450, y=80)

        self.closeButton = ctt.CTkLabel(self, text="×", font=("Arial", 48), width=40, height=40, bg_color="#fff")
        self.closeButton.place(x=952, y=75)
        self.closeButton.bind("<Button-1>", lambda _: self.initialize())

        targetDate = date(year=year, month=month, day=day)
        clothDetail = db.selectClothsUseHistByDate(self.master.userId, targetDate.isoformat().replace("-", ""))

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

        fontFormat = ctt.CTkFont(family="Arial", size=24, weight="bold")
        dateText = ctt.CTkLabel(self, text=targetDate.isoformat(), bg_color="#fbffdc", text_color="#333333", font=fontFormat)
        dateText.place(x=589, y=425)

        defaultThumbnail = ctt.CTkImage(light_image=Image.open(".\\img\\useHistDetail\\defaultThumbnail.png"),
                                    dark_image=Image.open(".\\img\\useHistDetail\\defaultThumbnail.png"),
                                    size=(159, 171))
        topImage = defaultThumbnail
        if top is not None:
            topText = ctt.CTkLabel(self, text=top[2], bg_color="#fbffdc",
                                    text_color="#333333", font=fontFormat)
            topText.place(x=589, y=495)

            topImage = ctt.CTkImage(light_image=Image.open(io.BytesIO(top[3])),
                                    dark_image=Image.open(io.BytesIO(top[3])),
                                    size=(159, 171))

        topImageBox = ctt.CTkLabel(self, image=topImage, text="")
        topImageBox.place(x=456, y=154)

        bottomImage = defaultThumbnail
        if bottom is not None:
            bottomText = ctt.CTkLabel(self, text=bottom[2], bg_color="#fbffdc",
                                   text_color="#333333", font=fontFormat)
            bottomText.place(x=589, y=565)

            bottomImage = ctt.CTkImage(light_image=Image.open(io.BytesIO(bottom[3])),
                                    dark_image=Image.open(io.BytesIO(bottom[3])),
                                    size=(159, 171))
        bottomImageBox = ctt.CTkLabel(self, image=bottomImage, text="")
        bottomImageBox.place(x=456 + 171, y=154)

        shoesImage = defaultThumbnail
        if shoes is not None:
            shoesText = ctt.CTkLabel(self, text=shoes[2], bg_color="#fbffdc",
                                   text_color="#333333", font=fontFormat)
            shoesText.place(x=589, y=635)

            shoesImage = ctt.CTkImage(light_image=Image.open(io.BytesIO(shoes[3])),
                                    dark_image=Image.open(io.BytesIO(shoes[3])),
                                    size=(159, 171))
        shoesImageBox = ctt.CTkLabel(self, image=shoesImage, text="")
        shoesImageBox.place(x=456 + 171 * 2, y=154)

        # print(year, month, day)
