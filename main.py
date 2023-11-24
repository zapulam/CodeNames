import argparse 
from tkinter import Tk
from codenames import CodeNames


if __name__ == "__main__":
    # Args for the custom bill version 
    parser = argparse.ArgumentParser()
    parser.add_argument('--custom', action='store_true', help='specifies if the custom bill version should be run')
    args = parser.parse_args()

    root = Tk()
    root.title("CodeNames")  
    app = CodeNames(root, args.custom)
    root.state('normal')
    root.mainloop()
    