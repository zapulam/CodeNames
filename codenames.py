import os
import random
from tkinter import Button, Frame, Grid, Tk
from tkinter import E, N, S, W
from termcolor import colored

# For the custom bill version
Bill_Words = {"hot", "tub", "mountain", "dew", "grape", "jelly", "sub", "smoke", "ribs"}
Non_Bill_Words = {"chicken", "tree", "ladybug", "handle", "berlin", "mom", "stairs", 
"beanstalk", "bleach", "observatory", "applesauce", "tornado", "tournament", 
"mail", "flutter", "intern"}


""" CodeNames class which handles word selection, board creation, and board interaction """
class CodeNames(object):
    def __init__(self, root: Tk, bill: bool):
        Grid.rowconfigure(root, 0, weight=1)
        Grid.columnconfigure(root, 0, weight=1)
        
        frame = Frame(root)
        frame.grid(row=0, column=0, sticky=N+S+E+W, padx=(10,10), pady=(10,10))

        # create board, words, and colors
        self.board = [ [None]*5 for _ in range(5) ]
        self.words = self.create_words(bill)
        self.colors = self.create_colors(bill)
        self.clicks = [ [0]*5 for _ in range(5) ]

        # print words to cmd
        self.print(self.words, self.colors)

        # populates board
        for i, row in enumerate(self.board):
            Grid.rowconfigure(frame, i, weight=1)
            for j, _ in enumerate(row):
                Grid.columnconfigure(frame, j, weight=1)
                btn = Button(frame, text=self.words[i][j].capitalize().center(max(len(x) for sublist in self.words for x in sublist), ' '), \
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
    def create_words(self, bill: bool = False):
        words = set()
        for file in os.listdir(os.path.abspath("words/")):
            words = words | set(line.strip().lower() for line in open(os.path.join("words", file)))
        words = random.sample(list(words), 25)
        
        # For the custom bill version
        if(bill):
            words = list(Bill_Words) + list(Non_Bill_Words)
            random.shuffle(words)
        return [words[i:i+5] for i in range(0, len(words), 5)]


    """ Create colored grid """
    def create_colors(self, bill: bool = False):
        colors = ["royalblue"]*9 + ["firebrick"]*8 + ["gold"]*7 + ["black"]*1
        random.shuffle(colors)

        # For the custom bill version
        if(bill):
            gold_words = set(random.sample(list(Non_Bill_Words), 7))
            black_word = set(random.sample(list(Non_Bill_Words - gold_words), 1))
            for idx, word in enumerate([word for word_list in self.words for word in word_list]):
                if(word in Bill_Words):
                    colors[idx] = "royalblue"
                elif(word in Non_Bill_Words - gold_words - black_word):
                    colors[idx] = "firebrick"
                elif(word in gold_words):
                    colors[idx] = "gold"
                elif(word in black_word):
                    colors[idx] = "black"
                else:
                    raise Exception("Invalid word")
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
            