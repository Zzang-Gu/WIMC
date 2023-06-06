import customtkinter as ctt
from PIL import Image

import etcDb

# pages
import lobby

class Profile(ctt.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, 1432, 805, **kwargs)
        self.master = master
        self.userName = ctt.StringVar()
        self.birthDate = ctt.StringVar()
        self.gender = ctt.StringVar()

        userInfo = etcDb.selectUser(self.master.userId)
        if len(userInfo) <= 0:
            self.master.alert("사용자 정보 조회 실패", "존재하지 않는 사용자 입니다.")
        else:
            self.userName.set(userInfo[0][1])
            self.gender.set(userInfo[0][2])
            self.birthDate.set(userInfo[0][3])

        imgBackground = ctt.CTkImage(light_image=Image.open(".\\img\\myCloset\\background1432x805.png"),
                                     dark_image=Image.open(".\\img\\myCloset\\background1432x805.png"),
                                     size=(1432, 805))

        popupFrame = ctt.CTkImage(light_image=Image.open(".\\img\\profile\\popupFrame627x673.png"),
                                     dark_image=Image.open(".\\img\\profile\\popupFrame627x673.png"),
                                     size=(627, 673))

        buttonFrame = ctt.CTkImage(light_image=Image.open(".\\img\\profile\\button282x65.png"),
                                     dark_image=Image.open(".\\img\\profile\\button282x65.png"),
                                     size=(282, 65))

        saveButton = ctt.CTkImage(light_image=Image.open(".\\img\\profile\\saveButton282x65.png"),
                                   dark_image=Image.open(".\\img\\profile\\saveButton282x65.png"),
                                   size=(200, 46))

        inputGuideLine = ctt.CTkImage(light_image=Image.open(".\\img\\profile\\inputGuideLine342x3.png"),
                                     dark_image=Image.open(".\\img\\profile\\inputGuideLine342x3.png"),
                                     size=(342, 3))

        self.labelTitle = ctt.CTkLabel(self, image=imgBackground, text="")
        self.labelTitle.place(x=0, y=0)

        self.popupFrame = ctt.CTkLabel(self, image=popupFrame, text="", bg_color="#E3F2ED")
        self.popupFrame.place(x=403, y=64)

        self.closeButton = ctt.CTkLabel(self, text="×", font=("Arial", 48), width=40, height=40, bg_color="#fff")
        self.closeButton.place(x=952, y=95)
        self.closeButton.bind("<Button-1>", self.closeEventHandler)

        # 이름, 성별, 생년월일 입력창
        # 이름
        self.nameLabel = ctt.CTkLabel(self, text="이름", bg_color="#ffffff", font=("Arial", 32))
        self.nameLabel.place(x=460, y=430)

        self.inputGuideLine1 = ctt.CTkLabel(self, image=inputGuideLine, text="", bg_color="#ffffff")
        self.inputGuideLine1.place(x=600, y=460)

        self.nameInput = ctt.CTkEntry(self, textvariable=self.userName, placeholder_text="이름 입력", bg_color="#ffffff", border_width=0, width=342, height=45)
        self.nameInput.place(x=600, y=425)

        # 성별
        self.genderLabel = ctt.CTkLabel(self, text="성별", bg_color="#ffffff", font=("Arial", 32))
        self.genderLabel.place(x=460, y=500)

        self.genderSelectBox = ctt.CTkSegmentedButton(self, width=200, height=35)
        self.genderSelectBox.configure(values=["남", "여"])

        self.genderSelectBox.set("남" if self.gender.get() == "M" else "여")
        self.genderSelectBox.place(x=600, y=500)

        # 생년월일
        self.birthDateLabel = ctt.CTkLabel(self, text="생년월일", bg_color="#ffffff", font=("Arial", 32))
        self.birthDateLabel.place(x=460, y=570)

        self.inputGuideLine2 = ctt.CTkLabel(self, image=inputGuideLine, text="", bg_color="#ffffff")
        self.inputGuideLine2.place(x=600, y=600)

        self.birthDateInput = ctt.CTkEntry(self, textvariable=self.birthDate, placeholder_text="생년월일 입력", bg_color="#ffffff", border_width=0, width=342,
                                      height=45)
        self.birthDateInput.place(x=600, y=565)

        # 저장 버튼
        self.saveButton = ctt.CTkButton(self, image=saveButton, text="", bg_color="#ffffff", border_width=0, hover_color="#efefef", fg_color="#ffffff", command=self.saveEventHandler)
        self.saveButton.place(x=610, y=630)

    def closeEventHandler(self, event):
        self.master.updatePage(lobby.Lobby)

    def saveEventHandler(self):
        userName = self.userName.get()
        userGender = "M" if self.genderSelectBox.get() == '남' else 'F'
        userBirthDate = self.birthDate.get()
        etcDb.updateProfile(self.master.userId, userName, userGender, userBirthDate)