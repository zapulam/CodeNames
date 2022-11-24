# Play CodeNames on Your Computer! 

*Codenames is a 2015 party card game designed by Vlaada Chvátil and published by Czech Games Edition. Two teams compete by each having a "spymaster" give one-word clues that can point to multiple words on the board. The other players on the team attempt to guess their team's words while avoiding the words of the other team.*

Cloning this repo will give you access to the source code and an executable file, *main.exe*. The game can be run either by running *python main.py* in the terminal or by simply running the executable. The CodeMaster card will be printed to the terminal and a Tkinter window will be opened where the game can be played.

If you wish to use the *main.exe* file, all other files can be removed *except* the files within the **words/** directory and the **words/** directory itself. The *main.exe* references the files within the **words/** directory so the *main.exe* file must remain in the same directory as **words/**.

This can look like...
CodeNames
    |___ main.exe
    |___ words
            |___ words.txt
            |___ original_words.txt

If you wish to add new words, you can create new text files in the **words/** directory and write a single word per line (similar to the structure of *words.txt* or original_words.txt*).
