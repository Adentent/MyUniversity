# coding: utf-8
"""
DESIGN: Adentent
"""

from tkinter import *


class Window:
    def __init__(self):
        self.root = Tk()
        self.root.title("My University")
        self.showing = []

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
    
    class StartWindow():
        def quit(self):
            exit()

        def beginGame(self):
            pass

        def main(self):
            # main
            NewGame = Button(Window.root,
                             text="开始游戏",
                             font=("zpix", 20),
                             bg="darkkhaki",
                             fg="white",
                             activebackground="darkkhaki",
                             activeforeground="white",
                             command=self.beginGame)
            Window.pack(NewGame)
            QuitGame = Button(Window.root,
                              text="关闭游戏",
                              font=("zpix", 10),
                              bg="grey",
                              fg="white",
                              activebackground="red",
                              activeforeground="white",
                              command=self.quit)
            Window.pack(QuitGame)

            Window.root.mainloop()
    class InGame:
        pass

if __name__ == "__main__":
    Window = Window()
    StartWindow = Window.StartWindow()
    StartWindow.main()
