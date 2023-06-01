from PIL import Image
import customtkinter as ctt

import winMyCloset
from profile import Profile

class Lobby(ctt.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, 1432, 805, **kwargs)

        self.master = master

        background = ctt.CTkImage(light_image=Image.open(".\\img\\winMyCloset\\background1432x805.png"),
                                     dark_image=Image.open(".\\img\\winMyCloset\\background1432x805.png"),
                                     size=(1432, 805))

        self.background = ctt.CTkLabel(self, image=background, text="")
        self.background.grid()

        title = ctt.CTkImage(light_image=Image.open(".\\img\\lobby\\title.png"),
                                     dark_image=Image.open(".\\img\\lobby\\title.png"),
                                     size=(590, 63))
        self.title = ctt.CTkLabel(self, image=title, text="", bg_color="#E3F2ED")
        self.title.place(x=421, y=50)

        profile = ctt.CTkImage(light_image=Image.open(".\\img\\lobby\\profile2.png"),
                             dark_image=Image.open(".\\img\\lobby\\profile2.png"),
                             size=(89, 111))
        self.profile = ctt.CTkLabel(self, image=profile, text="", bg_color="#E3F2ED", fg_color="#E3F2ED")
        self.profile.place(x=1260, y=50)
        self.profile.bind("<Button-1>", self.callProfileEdit)

        postIt1 = ctt.CTkImage(light_image=Image.open(".\\img\\lobby\\post-it1.png"),
                               dark_image=Image.open(".\\img\\lobby\\post-it1.png"),
                               size=(220, 234))
        postIt2 = ctt.CTkImage(light_image=Image.open(".\\img\\lobby\\post-it2.png"),
                               dark_image=Image.open(".\\img\\lobby\\post-it2.png"),
                               size=(220, 234))
        postIt3 = ctt.CTkImage(light_image=Image.open(".\\img\\lobby\\post-it3.png"),
                                    dark_image=Image.open(".\\img\\lobby\\post-it3.png"),
                                    size=(220, 234))

        self.menu1 = ctt.CTkLabel(self, image=postIt2, bg_color="#E3F2ED", fg_color="#E3F2ED", text="내 옷방 열기", font=("Arial", 24))
        self.menu1.place(x=200, y=160)
        self.menu1.bind("<Button-1>", self.callMenu1)

        self.menu2 = ctt.CTkLabel(self, image=postIt3, bg_color="#E3F2ED", fg_color="#E3F2ED", text="새 아이템 추가", font=("Arial", 24))
        self.menu2.place(x=620, y=160)
        self.menu2.bind("<Button-1>", self.callMenu2)

        self.menu3 = ctt.CTkLabel(self, image=postIt1, bg_color="#E3F2ED", fg_color="#E3F2ED", text="데일리 코디 등록", font=("Arial", 24))
        self.menu3.place(x=1000, y=160)
        self.menu3.bind("<Button-1>", self.callMenu3)

        self.menu4 = ctt.CTkLabel(self, image=postIt1, bg_color="#E3F2ED", fg_color="#E3F2ED", text="옷 컬러 추천 조합", font=("Arial", 24))
        self.menu4.place(x=200, y=460)
        self.menu4.bind("<Button-1>", self.callMenu4)

        self.menu5 = ctt.CTkLabel(self, image=postIt2, bg_color="#E3F2ED", fg_color="#E3F2ED", text="나의 먼슬리 코디", font=("Arial", 24))
        self.menu5.place(x=620, y=460)
        self.menu5.bind("<Button-1>", self.callMenu5)

        self.menu6 = ctt.CTkLabel(self, image=postIt3, bg_color="#E3F2ED", fg_color="#E3F2ED", text="오늘의 코디 추천", font=("Arial", 24))
        self.menu6.place(x=1000, y=460)
        self.menu6.bind("<Button-1>", self.callMenu6)

    def callProfileEdit(self):
        self.master.updatePage(Profile)

    def callMenu1(self, event):
        self.master.updatePage(winMyCloset.MyCloset)

    def callMenu2(self, event):
        self.master.updatePage(winMyCloset.MyCloset)

    def callMenu3(self, event):
        self.master.updatePage(winMyCloset.MyCloset)

    def callMenu4(self, event):
        self.master.updatePage(winMyCloset.MyCloset)

    def callMenu5(self, event):
        self.master.updatePage(winMyCloset.MyCloset)

    def callMenu6(self, event):
        self.master.updatePage(winMyCloset.MyCloset)
