from PIL import Image
import customtkinter as ctt

import db
import lobby

class Login(ctt.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, 1432, 805, **kwargs)

        self.master = master

        ctkImgBackground = ctt.CTkImage(light_image=Image.open(".\\img\\login\\background1432x805.png"), dark_image=Image.open(".\\img\\login\\background1432x805.png"), size=(1432, 805))
        ctkImgLoginBox = ctt.CTkImage(light_image=Image.open(".\\img\\login\\login.png"), dark_image=Image.open(".\\img\\login\\login.png"), size=(627, 770))
        ctkImgLoginButton = ctt.CTkImage(light_image=Image.open(".\\img\\login\\loginButton.png"), dark_image=Image.open(".\\img\\login\\loginButton.png"), size=(307, 92))

        self.labBackground = ctt.CTkLabel(self, image=ctkImgBackground, text="")
        self.labBackground.grid()

        self.labLoginBox = ctt.CTkLabel(self, image=ctkImgLoginBox, bg_color="#FFFFFF", fg_color="#FFFFFF", text="")
        self.labLoginBox.place(x=403, y=22)

        self.btnLogin = ctt.CTkButton(self, command=self.loginProcess, image=ctkImgLoginButton, bg_color="#FFFFFF", fg_color="#FFFFFF", hover_color="#FAFAFA", text="")
        self.btnLogin.place(x=560, y=580)

        self.entUserId = ctt.CTkEntry(self, width=440, height=60, border_width=0, bg_color="#FFFFFF", placeholder_text="학번을 입력해주세요.")
        self.entUserId.place(x=500, y=440)

    def loginProcess(self):
        userId = self.entUserId.get()

        response = db.selectUser(userId)
        if len(response) <= 0:
            self.master.alert("로그인 실패", "일치하는 사용자 정보가 없습니다.")
            return

        self.master.userId = response[0][0]
        self.master.updatePage(lobby.Lobby)
        self.destroy()
