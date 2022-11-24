import os
import random
from tkinter import *

from termcolor import colored


""" CodeNames class which handles word selection, board creation, and board interaction """
class CodeNames(object):
    def __init__(self, root):
        Grid.rowconfigure(root, 0, weight=1)
        Grid.columnconfigure(root, 0, weight=1)
        
        frame = Frame(root)
        frame.grid(row=0, column=0, sticky=N+S+E+W)

        # create board, words, and colors
        self.board = [ [None]*5 for _ in range(5) ]
        self.words = self.create_word_list()
        self.colors = self.create_selection()
        self.clicks = [ [0]*5 for _ in range(5) ]

        # print words to cmd
        self.print(self.words, self.colors)

        # populates board
        k = 0
        for i, row in enumerate(self.board):
            Grid.rowconfigure(frame, i, weight=1)
            for j, _ in enumerate(row):
                Grid.columnconfigure(frame, j, weight=1)
                btn = Button(frame, text=self.words[k].capitalize().center(len(max(self.words, key=len)), ' '), \
                    font=('Arial 24'), bg='grey80', relief='groove')
                btn.grid(row=i, column=j, sticky="nsew")
                btn.bind('<Button-1>', lambda e, i=i, j=j: self.on_click(i,j,e))
                k+=1

        # full screen
        pad = 3
        root.geometry("{0}x{1}+0+0".format(
            root.winfo_screenwidth()-pad, root.winfo_screenheight()-pad))


    " Handle click event "
    def on_click(self,i,j,event):
        if self.clicks[i][j] % 2 == 0:
            color = self.colors[i*5 + j]
            event.widget.config(bg=color)
        else:
            color = "grey80"
            event.widget.config(bg=color)
        self.clicks[i][j] += 1
            

    """ Create word list """
    def create_word_list(self):
        words = set()
        for file in os.listdir(os.path.abspath("words/")):
            words = words | set(line.strip() for line in open(os.path.join("words", file)))
        return random.sample(list(words), 25)


    """ Create colored grid """
    def create_selection(self):
        colors = ["royalblue"]*9 + ["firebrick"]*8 + ["gold"]*7 + ["black"]*1
        random.shuffle(colors)
        return colors


    """ Print words to cmd """
    def print(self, words, colors):
        print(colored("\nThe BLUE team plays first.", "blue"))
        print(colored("\nThe GREEN word is the assassin.\n", "green"))
        print(''.join(['-' for i in range(96)]))
        print("\n")
        for i in range(5):
            for j in range(5):
                if self.colors[i*5 + j] == 'royalblue':
                    color = "blue"
                elif self.colors[i*5 + j] == 'firebrick':
                    color = "red"
                elif self.colors[i*5 + j] == 'gold':
                    color = "yellow"
                else:
                    color = "green"
                print('|', colored(' {0: <15} '.format(words[i*5 + j].capitalize()), color), end="")
            print("|\n")
        print(''.join(['-' for i in range(96)]))
