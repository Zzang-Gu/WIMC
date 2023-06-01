import customtkinter as ctt
from PIL import Image

class Profile(ctt.CTkFrame):
    def __init__(self, master, width, height, **kwargs):
        super().__init__(master, width, height, **kwargs)

        imgBackground = ctt.CTkImage(light_image=Image.open(".\\img\\winMyCloset\\background1432x805.png"),
                                     dark_image=Image.open(".\\img\\winMyCloset\\background1432x805.png"),
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

        # self.labelTitle = ctt.CTkLabel(self, image=imgBackground, text="")
        # self.labelTitle.place(x=0, y=0)

        self.popupFrame = ctt.CTkLabel(self, image=popupFrame, text="")
        self.popupFrame.place(x=403, y=64)

        # 이름, 성별, 생년월일 입력창
        # 이름
        self.nameLabel = ctt.CTkLabel(self, text="이름", bg_color="#ffffff", font=("Arial", 32))
        self.nameLabel.place(x=473, y=430)

        self.inputGuideLine1 = ctt.CTkLabel(self, image=inputGuideLine, text="", bg_color="#ffffff")
        self.inputGuideLine1.place(x=600, y=460)

        self.nameInput = ctt.CTkEntry(self, placeholder_text="이름 입력", bg_color="#ffffff", border_width=0, width=342, height=45)
        self.nameInput.place(x=600, y=425)

        # 성별
        self.genderLabel = ctt.CTkLabel(self, text="성별", bg_color="#ffffff", font=("Arial", 32))
        self.genderLabel.place(x=473, y=500)

        self.genderSelectBox = ctt.CTkSegmentedButton(self, width=200, height=35)
        self.genderSelectBox.configure(values=["남", "여"])
        self.genderSelectBox.set("남")
        self.genderSelectBox.place(x=600, y=500)

        # 생년월일
        self.birthDateLabel = ctt.CTkLabel(self, text="생년월일", bg_color="#ffffff", font=("Arial", 32))
        self.birthDateLabel.place(x=473, y=570)

        self.inputGuideLine2 = ctt.CTkLabel(self, image=inputGuideLine, text="", bg_color="#ffffff")
        self.inputGuideLine2.place(x=600, y=600)

        self.birthDateInput = ctt.CTkEntry(self, placeholder_text="생년월일 입력", bg_color="#ffffff", border_width=0, width=342,
                                      height=45)
        self.birthDateInput.place(x=600, y=565)

        # 저장 버튼
        self.saveButton = ctt.CTkButton(self, image=saveButton, text="", bg_color="#ffffff", border_width=0, hover_color="#efefef", fg_color="#ffffff")
        self.saveButton.place(x=610, y=630)

class App(ctt.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1432x805")

        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)

        self.frameMyCloset = Profile(master=self, width=1432, height=805)
        self.frameMyCloset.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

if __name__ == "__main__":
    app = App()
    app.mainloop()
