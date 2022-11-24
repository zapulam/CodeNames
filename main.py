from tkinter import *
from codenames import CodeNames


if __name__ == "__main__":
    root = Tk()
    root.title("CodeNames")
    #root.config(bg="white")   
    app = CodeNames(root)
    root.mainloop()