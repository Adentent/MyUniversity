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
        try:
            self.StartWindow()
        except TclError:
            pass

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
    
    def NormalButton(self, text="", size=10, command=exit):
        return Button(self.root,
                      text=text,
                      font=("zpix", size),
                      bg="darkkhaki",
                      fg="white",
                      activebackground="darkkhaki",
                      activeforeground="white",
                      command=command)
    
    def RedButton(self, text="", size=10, command=exit):
        return Button(self.root,
                      text = text,
                      font=("zpix", size),
                      bg="grey",
                      fg="white",
                      activebackground="red",
                      activeforeground="white",
                      command=command)
    
    class StartWindow:
        def __init__(self):
            Window.root.title("MyUniversity - Start")
            self.main()

        def quit(self):
            exit()

        def beginGame(self):
            Window.cleanWindow()
            Window.message = "ChoosePlayer"
            # print("Dune")

        def main(self):
            Window.message = "StartWindow"
            NewGame = Window.NormalButton(text="开始游戏",
                                          size=50,
                                          command=self.beginGame)
            Window.pack(NewGame)
            QuitGame = Window.RedButton(text="关闭游戏",
                                        size=30,
                                        command=self.quit)
            Window.pack(QuitGame)

            while True:
                Window.root.update()
                if Window.message == "ChoosePlayer":
                    Window.ChoosePlayer()
                    return

            
    class ChoosePlayer:
        def __init__(self):
            Window.root.title("My University - ChoosePlayer")
            self.main()

        def ChooseLi(self):
            Window.message = "ChooseLi"
        
        def main(self):
            Li = Window.NormalButton(text="小李",
                                     size=40,
                                     command=self.ChooseLi)
            Window.pack(Li)

            while True:
                Window.root.update()
                if Window.message == "ChooseLi":
                    return
                

if __name__ == "__main__":
    Window = Window()
    Window.start()
