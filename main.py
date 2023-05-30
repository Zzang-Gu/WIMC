import customtkinter
class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label1 = customtkinter.CTkLabel(self, text="What's in My Closet2", fg_color="#ffffff",
                                             text_color="#000000",
                                             anchor="center", font=("Arial", 64), width=300, height=200)
        self.label1.grid(row=0, column=0)

        self.label2 = customtkinter.CTkLabel(self, text="What's in My Closet1", fg_color="#ffffff", text_color="#000000", anchor="center", font=("Arial", 64), width=1400, height=500)
        self.label2.grid(row=0, column=0)




class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1400x720")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")


app = App()
app.mainloop()
