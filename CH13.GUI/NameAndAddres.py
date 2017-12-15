import tkinter
class MyGUI:
    def __init__(self):
        message1 = ""
        message2 = ""
        self.main_window = tkinter.Tk()
        self.label1 = tkinter.Label(self.main_window,text=message1)
        self.label2 = tkinter.Label(self.main_window, text=message2)
        self.my_button = tkinter.Button(self.main_window, text = 'Click Me!', command = self.magicTime)
        self.label1.pack()
        self.label2.pack()
        self.my_button.pack()
        tkinter.mainloop()

    def magicTime(self):
        self.label2.config(text="Ever green terrace 123")
        self.label1.config(text="Homer Simpson")
myGui = MyGUI()