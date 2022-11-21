import tkinter as tk
from codenames import CodeNames


if __name__ == "__main__":
    root = tk.Tk()
    root.title("CodeNames")
    #root.config(bg="white")   
    app = CodeNames(root)
    root.mainloop()