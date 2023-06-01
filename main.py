import customtkinter
import tkinter.messagebox as tkmb

# Pages
from loading import Loading
from login import Login

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # initialize
        self.userInfo = None
        self.geometry("1432x805")

        # Default Page Setting (default=Loading)
        self.currentPage = None
        self.updatePage(Loading)

    def updatePage(self, targetPage):
        if self.currentPage is not None:
            # self.destory()
            self.currentPage = None

        self.currentPage = targetPage(self, 1432, 805)
        self.currentPage.place(x=0, y=0)

    def alert(self, title, message):
        tkmb.showerror(title=title, message=message)


app = App()
app.mainloop()
