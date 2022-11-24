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
        frame.grid(row=0, column=0, sticky=N+S+E+W, padx=(10,10), pady=(10,10))

        # create board, words, and colors
        self.board = [ [None]*5 for _ in range(5) ]
        self.words = self.create_words()
        self.colors = self.create_colors()
        self.clicks = [ [0]*5 for _ in range(5) ]

        # print words to cmd
        self.print(self.words, self.colors)

        # populates board
        for i, row in enumerate(self.board):
            Grid.rowconfigure(frame, i, weight=1)
            for j, _ in enumerate(row):
                Grid.columnconfigure(frame, j, weight=1)
                btn = Button(frame, text=self.words[i][j].capitalize().center(len(max(self.words, key=len)), ' '), \
                    font=('Arial 24'), bg='grey80', relief='groove')
                btn.grid(row=i, column=j, sticky="nsew")
                btn.bind('<Button-1>', lambda e, i=i, j=j: self.on_click(i,j,e))


    " Handle click event "
    def on_click(self,i,j,event):
        if self.clicks[i][j] % 2 == 0:
            color = self.colors[i][j]
            event.widget.config(bg=color)
        else:
            color = "grey80"
            event.widget.config(bg=color)
        self.clicks[i][j] += 1
            

    """ Create word list """
    def create_words(self):
        words = set()
        for file in os.listdir(os.path.abspath("words/")):
            words = words | set(line.strip() for line in open(os.path.join("words", file)))
        words = random.sample(list(words), 25)
        return [words[i:i+5] for i in range(0, len(words), 5)]


    """ Create colored grid """
    def create_colors(self):
        colors = ["royalblue"]*9 + ["firebrick"]*8 + ["gold"]*7 + ["black"]*1
        random.shuffle(colors)
        return [colors[i:i+5] for i in range(0, len(colors), 5)]


    """ Print words to cmd """
    def print(self, words, colors):
        print("\nThe", colored("BLUE", "blue"), "team plays first,", end=" ")
        print("the", colored("GREEN", "green"), "word is the assassin,", end=" ")
        print("and the", colored("YELLOW", color="yellow"), "words are free.\n")
        print(''.join(['-' for i in range(96)]))
        for i in range(5):
            for j in range(5):
                if colors[i][j] == 'royalblue':
                    color = "blue"
                elif colors[i][j] == 'firebrick':
                    color = "red"
                elif colors[i][j] == 'gold':
                    color = "yellow"
                else:
                    color = "green"
                print('|', colored(' {x} '.format(x=words[i][j].capitalize().center(15)), color), end="")
            print("|")
            print(''.join(['-' for i in range(96)]))