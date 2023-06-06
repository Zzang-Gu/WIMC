import customtkinter as ctt
import tkinter.messagebox as tkmb

import loading

class App(ctt.CTk):
    def __init__(self):
        super().__init__()

        # initialize
        self.userId = None
        self.geometry("1432x805")

        # Default Page Setting (default=Loading)
        self.currentPage = None
        self.updatePage(loading.Loading)

    def updatePage(self, targetPage):
        if self.currentPage is not None:
            self.currentPage = None

        self.currentPage = targetPage(self)
        self.currentPage.place(x=0, y=0)

    def alert(self, title, message):
        tkmb.showerror(title=title, message=message)

    def info(self, title, message):
        tkmb.showinfo(title=title, message=message)

if __name__ == "__main__":
    app = App()
    app.title("WIMC")
    app.mainloop()
