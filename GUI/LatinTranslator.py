import tkinter
class MyGUI:
    def __init__(self):
        self.mainWindow = tkinter.Tk()
        self.leftFrame = tkinter.Frame(self.mainWindow)
        self.rightFrame = tkinter.Frame(self.mainWindow)
        self.bottomFrame = tkinter.Frame(self.mainWindow)

        self.label1 = tkinter.Label(self.rightFrame, text="")
        self.label2 = tkinter.Label(self.rightFrame, text="")
        self.label3 = tkinter.Label(self.rightFrame, text="")
        self.label4 = tkinter.Label(self.leftFrame, text="")
        self.label5 = tkinter.Label(self.leftFrame, text="")
        self.label6 = tkinter.Label(self.leftFrame, text="")

        self.button1 = tkinter.Button(self.bottomFrame, text = 'Click Me!', command = self.action1)

        self.label1.pack()
        self.label2.pack()
        self.label3.pack()
        self.label4.pack()
        self.label5.pack()
        self.label6.pack()

        self.button1.pack()

        self.leftFrame.pack(side="left")
        self.rightFrame.pack(side="right")
        self.bottomFrame.pack()
        self.latin()
        tkinter.mainloop()

    def action1(self):
        self.label1.config(text="Left")
        self.label2.config(text="Right")
        self.label3.config(text="Center")

    def latin(self):
        self.label4.config(text="Sinister")
        self.label5.config(text="Dexter")
        self.label6.config(text="Medium")

myGui = MyGUI()