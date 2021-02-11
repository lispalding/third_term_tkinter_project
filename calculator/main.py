# MADE BY: Lisette Spalding & Daniel Lehman
# FILE NAME: tkinter_starter_template.py
# DATE CREATED: 02/11/2021
# DATE LAST MODIFIED: 02/11/2021

###### IMPORTS ######
from tkinter import *
######## FIN ########

##### CONSTANTS #####
HEIGHT = 200
WIDTH = 200
TITLE = "New Program"
BACKGROUND = "darkgrey"
FONT = "San_Serif"
######## FIN ########

######## CLASS #######
class App(Frame):
    """ To use: App(root)
        This is the App class, this class creates the application. """
    def __init__(self, master):
        """ To Use: You don't.
         This is the "in it" function. This function determines the constant variables in this class."""
        super(App, self).__init__(master)
        self.create()

    def create(self):
        """ To use: self.create()
         This is the create function, it creates the app widgets."""
        #### !! Operation Buttons !! ####
        multiplyBttn = Button(self, text="×", command=multiply)
        divideBttn = Button(self, text="÷", value="divide")
        addBttn = Button(self, text="+", value="add")
        subtractBttn = Button(self, text="-", value="subtract")
        ###### !! Operation FIN !! ######

        ###### !! Number Buttons !! #####
        numBttn0 = Button(self, text="0", value=0)
        numBttn1 = Button(self, text="1", value=1)
        numBttn2 = Button(self, text="2", value=2)
        numBttn3 = Button(self, text="3", value=3)
        numBttn4 = Button(self, text="4", value=4)
        numBttn5 = Button(self, text="5", value=5)
        numBttn6 = Button(self, text="6", value=6)
        numBttn7 = Button(self, text="7", value=7)
        numBttn8 = Button(self, text="8", value=8)
        numBttn9 = Button(self, text="9", value=9)
        ####### !! Number FIN !! ########

    def multiply(self):
        pass


def main():
    # General Setup
    root = Tk()
    root.geometry(str.format("{}x{}", WIDTH, HEIGHT))
    root.title(TITLE)

    ## Configurations ##
    root.configure(bg=BACKGROUND)
    ####### FIN ########

    # Conjuring the App
    app = App(root)
    root.mainloop() # Running the loop
######## FIN #########

main()