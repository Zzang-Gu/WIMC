import customtkinter
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1400x720")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


app = App()
app.mainloop()
