import os
import random
import tkinter as tk


class CodeNames(object):
    def __init__(self, root):
        self.root = root

        self.pad = 3
        self.counter = 0

        # create board
        self.board = [ [None]*5 for _ in range(5) ]

        # create word list; 25 words
        words = self.create_word_list()

        # create colors
        self.colors = self.create_selection()

        # populates board
        k = 0
        for i,row in enumerate(self.board):
            for j,column in enumerate(row):
                L = tk.Button(root, text=words[k].capitalize(), bg='grey80', font=('Arial 36'), width=14, height=3, relief='groove', compound=tk.CENTER)
                L.grid(row=i+1, column=j+1)
                L.bind('<Button-1>',lambda e,i=i,j=j: self.on_click(i,j,e))
                k+=1

        # center rows and cols
        self.root.grid_columnconfigure((0, 6), weight=1)
        self.root.grid_rowconfigure((0, 6), weight=1)

        # full screen
        """ self.root.geometry("{0}x{1}+0+0".format(
            self.root.winfo_screenwidth()-self.pad, self.root.winfo_screenheight()-self.pad)) """

        # spacing
        for col in range(5):
            self.root.grid_columnconfigure(col+1, minsize=410)
        for row in range(5):
            self.root.grid_rowconfigure(row+1, minsize=215)


    def on_click(self,i,j,event):
        color = self.colors[i*5 + j]
        event.widget.config(bg=color)
        self.board[i][j] = color


    def create_word_list(self):
        words = set()
        for file in os.listdir("words"):
            words = words | set(line.strip() for line in open(os.path.join("words", file)))
        return random.sample(list(words), 25)

    def create_selection(self):
        colors = ["royalblue"]*9 + ["firebrick"]*8 + ["gold"]*7 + ["black"]*1
        random.shuffle(colors)
        return colors
