from tkinter import *
from codenames import CodeNames


if __name__ == "__main__":
    root = Tk()
    root.title("CodeNames")  
    app = CodeNames(root)
    root.state('zoomed')
    root.mainloop()