# MADE BY: Lisette Spalding & Daniel Lehman
# FILE NAME: tkinter_starter_template.py
# DATE CREATED: 02/11/2021
# DATE LAST MODIFIED: 02/11/2021

###### IMPORTS ######
from tkinter import *
######## FIN ########

##### CONSTANTS #####
HEIGHT = 200
WIDTH = 234
TITLE = "Simple Calculator"
BACKGROUND = "#f5d142"
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

        self.grid()

        #### VARIABLES ####
        self.expression = ""
        self.equation = StringVar()
        ####### FIN #######

        self.create()

    def create(self):
        """ To use: self.create()
         This is the create function, it creates the app widgets."""
        #### !! Operation Buttons !! ####

        # Using lambdas because a lambda allows me to assign multiple things to a button
        multiplyBttn = Button(self, text = "×",
                              fg = "#4592bf", bg = "black",
                              command = lambda: self.press("*"), height = 1, width = 7)
        divideBttn = Button(self, text = "÷",
                              fg = "#4592bf", bg = "black",
                              command = lambda: self.press("/"), height = 1, width = 7)
        addBttn = Button(self, text = "+",
                              fg = "#4592bf", bg = "black",
                              command = lambda: self.press("+"), height = 3, width = 7)
        subtractBttn = Button(self, text = "-",
                              fg = "#4592bf", bg = "black",
                              command = lambda: self.press("-"), height = 1, width = 7)
        ###### !! Operation FIN !! ######

        ###### !! MISC. Buttons !! ######
        equalsBttn = Button(self, text = "=",
                            fg="#4592bf", bg = "black",
                            command=self.equalsPress, height=3, width=7)

        clearBttn = Button(self, text = "Clear",
                           fg="#4592bf", bg = "black",
                           command=self.clear, height=1, width=7)

        decimalBttn = Button(self, text = ".",
                             fg="#4592bf", bg = "black",
                             command = lambda: self.press('.'), height=1, width=7)
        ######## !! MISC. FIN !! ########

        ###### !! Number Buttons !! #####
        numBttn0 = Button(self, text = "0",
                          fg = "#d64768", bg = "black",
                          command = lambda: self.press(0), height = 1, width = 7)
        numBttn1 = Button(self, text = "1",
                          fg = "#d64768", bg = "black",
                          command = lambda: self.press(1), height = 1, width = 7)
        numBttn2 = Button(self, text = "2",
                          fg = "#d64768", bg = "black",
                          command = lambda: self.press(2), height = 1, width = 7)
        numBttn3 = Button(self, text = "3",
                          fg = "#d64768", bg = "black",
                          command = lambda: self.press(3), height = 1, width = 7)
        numBttn4 = Button(self, text = "4",
                          fg = "#d64768", bg = "black",
                          command = lambda: self.press(4), height = 1, width = 7)
        numBttn5 = Button(self, text = "5",
                          fg = "#d64768", bg = "black",
                          command = lambda: self.press(5), height = 1, width = 7)
        numBttn6 = Button(self, text = "6",
                          fg = "#d64768", bg = "black",
                          command = lambda: self.press(6), height = 1, width = 7)
        numBttn7 = Button(self, text = "7",
                          fg = "#d64768", bg = "black",
                          command = lambda: self.press(7), height = 1, width = 7)
        numBttn8 = Button(self, text = "8",
                          fg = "#d64768", bg = "black",
                          command = lambda: self.press(8), height = 1, width = 7)
        numBttn9 = Button(self, text = "9",
                          fg = "#d64768", bg = "black",
                          command = lambda: self.press(9), height = 1, width = 7)
        ####### !! Number FIN !! ########

        ######## !! Text Entry !! #######
        expressionField = Entry(self, textvariable = self.equation)
        ######## !! Entry FIN !! ########

        ###### !! GRID PLACEMENT !! #######

        ##### .. Entry Placement .. #####
        expressionField.grid(columnspan = 4)
        ######## .. Entry FIN .. ########

        #### .. Button Placement .. #####
        ####### NUM BUTTONS
        numBttn7.grid(row = 2, column = 0)
        numBttn8.grid(row = 2, column = 1)
        numBttn9.grid(row = 2, column = 2)
        numBttn4.grid(row = 3, column = 0)
        numBttn5.grid(row = 3, column = 1)
        numBttn6.grid(row = 3, column = 2)
        numBttn1.grid(row = 4, column = 0)
        numBttn2.grid(row = 4, column = 1)
        numBttn3.grid(row = 4, column = 2)
        numBttn0.grid(rowspan = 2, row = 5, column = 0)
        ####### NUM BUTTON FIN

        decimalBttn.grid(row = 5, column = 2)

        ####### OPERATION BUTTONS
        clearBttn.grid(row = 1, column = 0)
        divideBttn.grid(row = 1, column = 1)
        multiplyBttn.grid(row = 1, column = 2)
        subtractBttn.grid(row = 1, column = 3)
        addBttn.grid(row = 2, column = 3, columnspan = 2)
        equalsBttn.grid(row = 4, column = 3, columnspan = 2)
        ####### OPERATION BUTTON FIN
        ####### .. Button FIN .. ########

        ######### !! GRID FIN !! ##########

    def press(self, num):
        """ To use: self.press()
         This is a function that is used in order to register button presses. """
        self.expression = self.expression + str(num) # String concatenation

        # Updating the expression by using the "set" method:
        self.equation.set(self.expression)

    def equalsPress(self):
        """ To use: self.equalsPress()
        This is a function that is used to register what happens when the equals button is pressed."""

        try: # This "Try" statement is used in order to register what happens with errors
            # Used "eval" function to evaluate expression & str function in order to convert result into string
            total = str(eval(self.expression))

            self.equation.set(total)

            # Initializing the expression variable with empty string
            self.expression = ""
        except: # If an error is generated then this happens
            self.equation.set("Error")
            self.expression =  ""

    def clear(self):
        """ To use: self.clear()
         This is a function that will be used to clear the contents of the text entry box. """
        self.expression = ""
        self.equation.set("")

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