from PIL import Image
import customtkinter as ctt

import userProfile
import myCloset
import regCloth
import dailyLookRegister
import monthlyCody
import colorCode
import codySgstn

class Lobby(ctt.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, 1432, 805, **kwargs)

        self.master = master

        ctkImgBackground = ctt.CTkImage(light_image=Image.open(".\\img\\lobby\\background1432x805.png"), dark_image=Image.open(".\\img\\lobby\\background1432x805.png"), size=(1432, 805))
        self.labBackground = ctt.CTkLabel(self, image=ctkImgBackground, text="")
        self.labBackground.grid()

        ctkImgTitle = ctt.CTkImage(light_image=Image.open(".\\img\\lobby\\title.png"), dark_image=Image.open(".\\img\\lobby\\title.png"), size=(590, 63))
        self.labTitle = ctt.CTkLabel(self, image=ctkImgTitle, bg_color="#E3F2ED", text="")
        self.labTitle.place(x=421, y=50)

        ctkImgProfile = ctt.CTkImage(light_image=Image.open(".\\img\\lobby\\profile2.png"), dark_image=Image.open(".\\img\\lobby\\profile2.png"), size=(89, 111))
        self.labProfile = ctt.CTkLabel(self, image=ctkImgProfile, bg_color="#E3F2ED", fg_color="#E3F2ED", text="")
        self.labProfile.place(x=1260, y=50)
        self.labProfile.bind("<Button-1>", self.callProfileEdit)

        ctkImgPostIt1 = ctt.CTkImage(light_image=Image.open(".\\img\\lobby\\post-it1.png"), dark_image=Image.open(".\\img\\lobby\\post-it1.png"), size=(220, 234))
        ctkImgPostIt2 = ctt.CTkImage(light_image=Image.open(".\\img\\lobby\\post-it2.png"), dark_image=Image.open(".\\img\\lobby\\post-it2.png"), size=(220, 234))
        ctkImgPostIt3 = ctt.CTkImage(light_image=Image.open(".\\img\\lobby\\post-it3.png"), dark_image=Image.open(".\\img\\lobby\\post-it3.png"), size=(220, 234))

        self.labMenu1 = ctt.CTkLabel(self, image=ctkImgPostIt2, bg_color="#E3F2ED", fg_color="#E3F2ED", text="내 옷장 열기", font=("Arial", 24))
        self.labMenu1.place(x=200, y=160)
        self.labMenu1.bind("<Button-1>", self.callMenu1)

        self.labMenu2 = ctt.CTkLabel(self, image=ctkImgPostIt3, bg_color="#E3F2ED", fg_color="#E3F2ED", text="새 아이템 추가", font=("Arial", 24))
        self.labMenu2.place(x=620, y=160)
        self.labMenu2.bind("<Button-1>", self.callMenu2)

        self.labMenu3 = ctt.CTkLabel(self, image=ctkImgPostIt1, bg_color="#E3F2ED", fg_color="#E3F2ED", text="데일리 코디 등록", font=("Arial", 24))
        self.labMenu3.place(x=1000, y=160)
        self.labMenu3.bind("<Button-1>", self.callMenu3)

        self.labMenu4 = ctt.CTkLabel(self, image=ctkImgPostIt1, bg_color="#E3F2ED", fg_color="#E3F2ED", text="나의 먼슬리 코디", font=("Arial", 24))
        self.labMenu4.place(x=200, y=460)
        self.labMenu4.bind("<Button-1>", self.callMenu4)

        self.labMenu5 = ctt.CTkLabel(self, image=ctkImgPostIt2, bg_color="#E3F2ED", fg_color="#E3F2ED", text="옷 컬러 추천 조합", font=("Arial", 24))
        self.labMenu5.place(x=620, y=460)
        self.labMenu5.bind("<Button-1>", self.callMenu5)

        self.labMenu6 = ctt.CTkLabel(self, image=ctkImgPostIt3, bg_color="#E3F2ED", fg_color="#E3F2ED", text="오늘의 코디 추천", font=("Arial", 24))
        self.labMenu6.place(x=1000, y=460)
        self.labMenu6.bind("<Button-1>", self.callMenu6)

    def callProfileEdit(self, event):
        self.master.updatePage(userProfile.UserProfile)

    def callMenu1(self, event):
        self.master.updatePage(myCloset.MyCloset)

    def callMenu2(self, event):
        self.master.updatePage(regCloth.RegCloth)

    def callMenu3(self, event):
        self.master.updatePage(dailyLookRegister.DailyLookRegister)

    def callMenu4(self, event):
        self.master.updatePage(monthlyCody.MonthlyCody)

    def callMenu5(self, event):
        self.master.updatePage(colorCode.ColorCode)

    def callMenu6(self, event):
        self.master.updatePage(codySgstn.CodySgstn)
