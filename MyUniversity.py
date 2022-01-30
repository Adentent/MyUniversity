# coding: utf-8
"""
DESIGN: Adentent
"""


from tkinter import *
from threading import *


class Window:
    def __init__(self):
        self.root = Tk()
        self.root.title("My University")
        self.message = ""
        self.showing = []
    
    def start(self):
        self.StartWindow()
        if self.message == "ChoosePlayer":
            self.ChoosePlayer()

    def loop(self):
        self.root.mainloop()

    def pack(self, obj):
        obj.pack()
        self.showing.append(obj)
    
    def pack_forget(self, obj):
        obj.pack_forget()
        self.showing.remove(obj)
    
    def cleanWindow(self):
        for i in self.showing:
            i.pack_forget()
        self.showing = []
    
    class StartWindow:
        def __init__(self):
            Window.root.title("MyUniversity - Start")
            self.main()

        def quit(self):
            exit()

        def beginGame(self):
            Window.cleanWindow()
            Window.message = "ChoosePlayer"

        def main(self):
            Window.message = "StartWindow"
            NewGame = Button(Window.root,
                             text="开始游戏",
                             font=("zpix", 50),
                             bg="darkkhaki",
                             fg="white",
                             activebackground="darkkhaki",
                             activeforeground="white",
                             command=self.beginGame)
            Window.pack(NewGame)
            QuitGame = Button(Window.root,
                              text="关闭游戏",
                              font=("zpix", 30),
                              bg="grey",
                              fg="white",
                              activebackground="red",
                              activeforeground="white",
                              command=self.quit)
            Window.pack(QuitGame)

            if Window.message != "StartWindow":
                return

            
    class ChoosePlayer:
        def __init__(self):
            Window.root.title("My University - ChoosePlayer")
            self.main()

        def main(self):
            Li = Button(Window.root,
                        text="小李")
            Window.pack(Li)

if __name__ == "__main__":
    Window = Window()
    start = Thread(target=Window.start(), name="main")
    loop = Thread(target=Window.loop, name="loop")
    start.run()
    loop.run()
