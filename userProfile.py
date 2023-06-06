import io

from PIL import Image
import customtkinter as ctt
from CTkMessagebox import CTkMessagebox as ctkmbox

import db

class UserProfile(ctt.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, 1432, 805, **kwargs)
        self.master = master
        self.userName = ctt.StringVar()
        self.birthDate = ctt.StringVar()
        self.gender = ctt.StringVar()

        userInfo = db.selectUser(self.master.userId)
        if len(userInfo) <= 0:
            self.master.alert("사용자 정보 조회 실패", "존재하지 않는 사용자 입니다.")
            self.destroy()
        else:
            self.userName.set(userInfo[0][1])
            self.userImg = userInfo[0][2]
            self.gender.set(userInfo[0][3])
            self.birthDate.set(userInfo[0][4])

        if userInfo[0][2] is None:
            self.userImg = open(".\\img\\userProfile\\defaultUser216x239.png", "rb").read()

        self.ctkImgBackground = ctt.CTkImage(light_image=Image.open(".\\img\\userProfile\\background1432x805.png"), dark_image=Image.open(".\\img\\userProfile\\background1432x805.png"), size=(1432, 805))
        self.ctkImgPopupFrame = ctt.CTkImage(light_image=Image.open(".\\img\\userProfile\\popupFrame634x682.png"), dark_image=Image.open(".\\img\\userProfile\\popupFrame634x682.png"), size=(634, 682))
        self.ctkImgSaveButton = ctt.CTkImage(light_image=Image.open(".\\img\\userProfile\\saveButton282x65.png"), dark_image=Image.open(".\\img\\userProfile\\saveButton282x65.png"), size=(200, 46))
        self.ctkImgInputGuideLine = ctt.CTkImage(light_image=Image.open(".\\img\\userProfile\\inputGuideLine342x3.png"), dark_image=Image.open(".\\img\\userProfile\\inputGuideLine342x3.png"), size=(342, 3))

        self.labTitle = ctt.CTkLabel(self, image=self.ctkImgBackground, text="")
        self.labTitle.place(x=0, y=0)

        self.labPopupFrame = ctt.CTkLabel(self, image=self.ctkImgPopupFrame, text="", bg_color="#E3F2ED")
        self.labPopupFrame.place(x=399, y=62)

        self.ctkImgBack = ctt.CTkImage(light_image=Image.open(".\\img\\userProfile\\back55x50.png"), dark_image=Image.open(".\\img\\userProfile\\back55x50.png"), size=(55, 50))
        self.labBack = ctt.CTkLabel(self, image=self.ctkImgBack, fg_color="#E3F2ED", text="")
        self.labBack.place(x=50, y=50)
        self.labBack.bind("<Button-1>", self.clickBack)

        ctt.CTkLabel(self, width=300, height=50, bg_color="#FFFFFF", fg_color="#FFFFFF", text="프로필 수정", font=("JalnanOTF", 30)).place(x=566, y=87)

        self.ctkImgUser = ctt.CTkImage(light_image=Image.open(io.BytesIO(self.userImg)), dark_image=Image.open(io.BytesIO(self.userImg)), size=(216, 239))
        self.labUserImg = ctt.CTkLabel(self, image=self.ctkImgUser, text="")
        self.labUserImg.place(x=608, y=147)

        self.ctkImgUpload = ctt.CTkImage(light_image=Image.open(".\\img\\clothInfo\\upload45x45.png"), dark_image=Image.open(".\\img\\clothInfo\\upload45x45.png"), size=(45, 45))
        self.labUpload = ctt.CTkLabel(self, image=self.ctkImgUpload, bg_color="#FFFFFF", fg_color="#FFFFFF", text="")
        self.labUpload.place(x=801, y=366)
        self.labUpload.bind("<Button-1>", self.userImgUpload)

        # 이름, 성별, 생년월일 입력창
        # 이름
        self.labName = ctt.CTkLabel(self, width=100, bg_color="#FFFFFF", text="이름", font=("Arial", 24), anchor="center")
        self.labName.place(x=460, y=435)
        ctt.CTkLabel(self, image=self.ctkImgInputGuideLine, bg_color="#FFFFFF", text="").place(x=600, y=460)

        self.entName = ctt.CTkEntry(self, width=342, height=45, border_width=0, bg_color="#FFFFFF", textvariable=self.userName, placeholder_text="이름 입력", font=("Arial", 16))
        self.entName.place(x=600, y=425)

        # 성별
        self.labGender = ctt.CTkLabel(self, width=100, bg_color="#FFFFFF", text="성별", font=("Arial", 24), anchor="center")
        self.labGender.place(x=460, y=505)

        self.sgmbtnGender = ctt.CTkSegmentedButton(self, width=200, height=35, values=["남", "여"])
        self.sgmbtnGender.set("남" if self.gender.get() == "M" else "여")
        self.sgmbtnGender.place(x=600, y=500)

        # 생년월일
        self.labBirthDate = ctt.CTkLabel(self, width=100, bg_color="#FFFFFF", text="생년월일", font=("Arial", 24), anchor="center")
        self.labBirthDate.place(x=460, y=575)
        ctt.CTkLabel(self, image=self.ctkImgInputGuideLine, bg_color="#FFFFFF", text="").place(x=600, y=600)

        self.entBirthDate = ctt.CTkEntry(self, width=342, height=45, border_width=0, bg_color="#FFFFFF", textvariable=self.birthDate, placeholder_text="생년월일 입력", font=("Arial", 16))
        self.entBirthDate.place(x=600, y=565)

        # 저장 버튼
        self.btnSave = ctt.CTkButton(self, image=self.ctkImgSaveButton, border_width=0, bg_color="#FFFFFF", fg_color="#FFFFFF", hover_color="#EFEFEF", text="", command=self.saveEventHandler)
        self.btnSave.place(x=610, y=630)

    def clickBack(self, event):
        self.destroy()

    def userImgUpload(self, event):
        fileNm = ctt.filedialog.askopenfilename(initialdir="/", title = "파일을 선택 해 주세요", filetypes = (("*.png","*png"), ("*.jpg", "*jpg"), ("*.jpeg", "*jpeg")))

        file = open(fileNm, "rb")
        self.userImg = file.read()

        self.ctkImgUser = ctt.CTkImage(light_image=Image.open(io.BytesIO(self.userImg)), dark_image=Image.open(io.BytesIO(self.userImg)), size=(216, 239))
        self.labUserImg.configure(image=self.ctkImgUser)

    def saveEventHandler(self):
        userName = self.entName.get()
        userGender = "M" if self.sgmbtnGender.get() == '남' else 'F'
        userBirthDate = self.entBirthDate.get()

        msg = ctkmbox(title="확인", message="수정한 정보를 저장하시겠습니까?", icon="question", option_1="Cancel", option_2="No", option_3="Yes")
        response = msg.get()

        if response=="Yes":
            db.updateProfile(self.master.userId, userName, self.userImg, userGender, userBirthDate)
            ctkmbox(title="정보", message="수정되었습니다.")
            self.destroy()
        elif response=="No":
            self.destroy()
