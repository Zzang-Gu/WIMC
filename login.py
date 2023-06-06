import customtkinter as ctt
from PIL import Image

import etcDb

# pages
from lobby import Lobby


class Login(ctt.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, 1432, 805, **kwargs)
        self.master = master

        self.initialize()

    def initialize(self):
        imgBackground = ctt.CTkImage(light_image=Image.open(".\\img\\myCloset\\background1432x805.png"),
                                     dark_image=Image.open(".\\img\\myCloset\\background1432x805.png"),
                                     size=(1432, 805))

        loginBox = ctt.CTkImage(light_image=Image.open("img/login/login.png"),
                                dark_image=Image.open("img/login/login.png"),
                                size=(627, 770))

        loginButtonImage = ctt.CTkImage(light_image=Image.open("img/login/loginButton.png"),
                                        dark_image=Image.open("img/login/loginButton.png"),
                                        size=(307, 92))

        self.background = ctt.CTkLabel(self, image=imgBackground, text="")
        self.background.place(x=0, y=0)

        self.loginBox = ctt.CTkLabel(self, image=loginBox, text="", fg_color="#ffffff")
        self.loginBox.place(x=403, y=22)

        self.button = ctt.CTkButton(self, text="", command=self.loginProcess, image=loginButtonImage,
                                    fg_color="#ffffff", hover_color="#fafafa")
        self.button.place(x=560, y=580)

        self.input = ctt.CTkEntry(self, placeholder_text="학번을 입력해주세요.", width=440, height=60, border_width=0,
                                  bg_color="#ffffff")
        self.input.place(x=500, y=440)

    def loginProcess(self):
        userId = self.input.get()

        response = etcDb.selectUser(userId)
        if len(response) <= 0:
            self.master.alert("로그인 실패", "일치하는 사용자 정보가 없습니다.")
            return

        self.master.userId = response[0][0]
        self.master.updatePage(Lobby)
