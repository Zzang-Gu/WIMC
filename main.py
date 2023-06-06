import customtkinter
import tkinter.messagebox as tkmb

# Pages
from loading import Loading
from login import Login
from lobby import Lobby

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # initialize
        self.userId = 20231662
        self.geometry("1432x805")

        # Default Page Setting (default=Loading)
        self.currentPage = None
        self.updatePage(Lobby)

    def updatePage(self, targetPage):
        if self.currentPage is not None:
            # self.destory()
            self.currentPage = None

        self.currentPage = targetPage(self)
        self.currentPage.place(x=0, y=0)

    def alert(self, title, message):
        tkmb.showerror(title=title, message=message)

    def info(self, title, message):
        tkmb.showinfo(title=title, message=message)

if __name__ == "__main__":
    app = App()
    app.mainloop()
