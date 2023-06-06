import io
from time import sleep

from PIL import Image
import customtkinter as ctt
import urllib.request
from selenium import webdriver
from bs4 import BeautifulSoup

import db

class CodyInfo(ctt.CTkFrame):
    def __init__(self, master, imgCody):
        super().__init__(master, width=300, height=360, fg_color="#F5F5ED")

        self.imgCody = imgCody

        self.ctkImgCody = ctt.CTkImage(light_image=Image.open(io.BytesIO(self.imgCody)), dark_image=Image.open(io.BytesIO(self.imgCody)), size=(300, 360))
        self.labCody = ctt.CTkLabel(self, image=self.ctkImgCody, text="")
        self.labCody.grid()

class CodyList(ctt.CTkScrollableFrame):
    def __init__(self, master, sexCd):
        super().__init__(master, width=960, height=500, fg_color="#F5F5ED")

        self.sexCd = sexCd

        self.styleCd = {
            "minimal" : 1,
            "bsCasual" : 5,
            "street" : 12,
            "sporty" : 29,
            "unique" : 30
        }

        self.showCodys("minimal")

    def showCodys(self, styleType):
        self.styleType = styleType

        if self.sexCd == "M":
            gender = "MEN"
        else:
            gender = "WOMEN"

        url = 'https://www.onthelook.co.kr/?initFilter={"styleTagIds":[' + str(self.styleCd[self.styleType]) + '],"gender":["' + gender + '"],"height":[],"weight":[],"season":[]}&tab=HOT'
        print(url)

        self.imgCodyList = self.codyCrawling(url)

        for idx, imgCody in enumerate(self.imgCodyList):
            frmCodyInfo = CodyInfo(self, imgCody)
            frmCodyInfo.grid(row=idx//3, column=idx%3, padx=10, pady=10)

    def codyCrawling(self, url):
        # 크롬 드라이버 설정
        # (크롤링할 때 웹 페이지 띄우지 않음, gpu 사용 안함, 한글 지원, user-agent 헤더 추가)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("lang=ko_KR")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36")
        driver = webdriver.Chrome(".\chromedriver.exe",chrome_options=chrome_options)

        #웹 페이지 접근 후 1초동안 로드를 기다림
        driver.get(url)
        sleep(3)

        #크롤링이 가능하도록 html코드 가공
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        reqlList = soup.select("img.sc-hdPSEv.bXSJJM")

        urlList = []

        for idx, req in enumerate(reqlList):
            urlList.append(req.get("src"))

        driver.close()

        imageList = []

        for _, imgUrl in enumerate(urlList):
            if len(imageList) == 9:
                break

            try:
                image = urllib.request.urlopen(imgUrl).read()
                imageList.append(image)
            except Exception as err:
                print(err)
                print(imgUrl)

        return imageList

class CodySgstn(ctt.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, width=1432, height=805, **kwargs)

        self.master = master

        row = db.selectUser(self.master.userId)
        self.userId = row[0][0]
        self.userNm = row[0][1]
        self.sexCd = row[0][2]
        self.brthdDe = row[0][3]

        self.ctkImgBackground = ctt.CTkImage(light_image=Image.open(".\\img\\codySgstn\\background1432x805.png"), dark_image=Image.open(".\\img\\codySgstn\\background1432x805.png"), size=(1432, 805))
        self.labelBackground = ctt.CTkLabel(self, image=self.ctkImgBackground, text="")
        self.labelBackground.grid()

        self.ctkImgBack = ctt.CTkImage(light_image=Image.open(".\\img\\codySgstn\\back55x50.png"), dark_image=Image.open(".\\img\\codySgstn\\back55x50.png"), size=(55, 50))
        self.labelBack = ctt.CTkLabel(self, image=self.ctkImgBack, text="", fg_color="#E3F2ED")
        self.labelBack.place(x=50, y=50)
        self.labelBack.bind("<Button-1>", self.clickBack)

        imgWindow = ctt.CTkImage(light_image=Image.open(".\\img\\codySgstn\\frame849x531.png"), dark_image=Image.open(".\\img\\codySgstn\\frame849x531.png"), size=(1121, 703))
        ctt.CTkLabel(self, image=imgWindow, fg_color="#E3F2ED", text="").place(x=155, y=61)

        ctt.CTkLabel(self, width=300, height=60, bg_color="#F5F5ED", fg_color="#F5F5ED", text="코디 추천", font=("JalnanOTF", 45)).place(x=566, y=95)

        btnMinimal = ctt.CTkButton(self, width=145, height=47, border_width=3, bg_color="#F5F5ED", fg_color="#FFFFFF", hover_color="#AAAAAA", border_color="#000000", text="미니멀", text_color="#000000", command= lambda: self.scrFrmCodyList.showCodys("minimal"))
        btnBsCasual = ctt.CTkButton(self, width=145, height=47, border_width=3, bg_color="#F5F5ED", fg_color="#FFFFFF", hover_color="#AAAAAA", border_color="#000000", text="비즈니스 캐주얼", text_color="#000000", command= lambda: self.scrFrmCodyList.showCodys("bsCasual"))
        btnStreet = ctt.CTkButton(self, width=145, height=47, border_width=3, bg_color="#F5F5ED", fg_color="#FFFFFF", hover_color="#AAAAAA", border_color="#000000", text="스트릿", text_color="#000000", command= lambda: self.scrFrmCodyList.showCodys("street"))
        btnSporty = ctt.CTkButton(self, width=145, height=47, border_width=3, bg_color="#F5F5ED", fg_color="#FFFFFF", hover_color="#AAAAAA", border_color="#000000", text="스포티", text_color="#000000", command= lambda: self.scrFrmCodyList.showCodys("sporty"))
        btnUnique = ctt.CTkButton(self, width=145, height=47, border_width=3, bg_color="#F5F5ED", fg_color="#FFFFFF", hover_color="#AAAAAA", border_color="#000000", text="유니크", text_color="#000000", command= lambda: self.scrFrmCodyList.showCodys("unique"))

        btnMinimal.place(x=284, y=165)
        btnBsCasual.place(x=459, y=165)
        btnStreet.place(x=644, y=165)
        btnSporty.place(x=819, y=165)
        btnUnique.place(x=994, y=165)

        self.scrFrmCodyList = CodyList(self, self.sexCd)
        self.scrFrmCodyList.place(x=230, y=230)

    def clickBack(self, event):
        self.destroy()

class App(ctt.CTk):
    def __init__(self):
        super().__init__()

        self.title("WIMC")
        self.geometry("1432x805")

        self.userId = "20231662"

        self.codySgstn = CodySgstn(self)
        self.codySgstn.grid()

if __name__ == "__main__":
    app = App()
    app.mainloop()
