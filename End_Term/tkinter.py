import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Polar Decomposition ")
        #setting window size
        width=600
        height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_373=tk.Label(root)
        GLabel_373["anchor"] = "center"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_373["font"] = ft
        GLabel_373["fg"] = "#333333"
        GLabel_373["justify"] = "center"
        GLabel_373["text"] = "Choose size of the matrix"
        GLabel_373["relief"] = "raised"
        GLabel_373.place(x=40,y=10,width=531,height=30)

        GButton_958=tk.Button(root)
        GButton_958["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_958["font"] = ft
        GButton_958["fg"] = "#000000"
        GButton_958["justify"] = "center"
        GButton_958["text"] = "3x3"
        GButton_958.place(x=80,y=60,width=95,height=30)
        GButton_958["command"] = self.GButton_958_command

        GButton_979=tk.Button(root)
        GButton_979["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_979["font"] = ft
        GButton_979["fg"] = "#000000"
        GButton_979["justify"] = "center"
        GButton_979["text"] = "2x2"
        GButton_979.place(x=410,y=60,width=96,height=30)
        GButton_979["command"] = self.GButton_979_command

        GLineEdit_266=tk.Entry(root)
        GLineEdit_266["borderwidth"] = "10px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_266["font"] = ft
        GLineEdit_266["fg"] = "#333333"
        GLineEdit_266["justify"] = "center"
        GLineEdit_266["text"] = "Output_Matrix"
        GLineEdit_266.place(x=150,y=150,width=300,height=300)
        GLineEdit_266["show"] = "undefined"

    def GButton_958_command(self):
        print("command")


    def GButton_979_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
