import customtkinter
class Lobby(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("1600x720")
        self.label = customtkinter.CTkLabel(self, text="What's in My Closet", fg_color="#ffffff", text_color="#000000", anchor="center", font=("Arial", 64))
        self.label.grid(row=0, column=0, padx=800)


    def button_callback(self):
        print("button pressed")