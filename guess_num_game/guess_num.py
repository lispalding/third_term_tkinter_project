# MADE BY: Lisette Spalding
# FILE NAME: tkinter_starter_template.py
# DATE CREATED: 02/11/2021
# DATE LAST MODIFIED: 03/03/2021
# FILE NAME: guess_num.py

###### IMPORTS ######
from tkinter import *
######## FIN ########

##### CONSTANTS #####
HEIGHT = 200
WIDTH = 200
TITLE = "Guess My Number!!"
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
        """ To use: create()
         This is the create function, it creates the app widgets."""
        ###### .. ENTRIES .. #######
        self.numEntry = Entry(self)
        ###### .. FINISHED .. ######

        ###### .. BUTTONS .. #######
        self.submit = Button(self, text = "Submit")
        ###### .. FINISHED .. ######

    


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
