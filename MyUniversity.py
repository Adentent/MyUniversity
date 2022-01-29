"""
DESIGN: Adentent
"""

from tkinter import *

def quit():
    exit()

def beginGame():
    pass

def main():
    root = Tk()
    
    # init
    root.title("My University")

    # main
    NewGame = Button(root,
                     text="开始游戏",
                     font=("zpix", 20),
                     bg="darkkhaki",
                     fg="white",
                     activebackground="darkkhaki",
                     activeforeground="white",
                     command=beginGame)
    NewGame.pack()
    QuitGame = Button(root,
                      text="关闭游戏",
                      font=("zpix", 10),
                      bg="grey",
                      fg="white",
                      activebackground="red",
                      activeforeground="white",
                      command=quit)
    QuitGame.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
