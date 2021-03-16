# MADE BY: Lisette Spalding
# PROJECT NAME: third_term_tkinter_project
# DATE CREATED: 02/11/2021
# DATE LAST MODIFIED: 03/13/2021
# FILE NAME: guess_num.py

###### IMPORTS ######
from tkinter import *
from tkinter import messagebox as mb
import random
######## FIN ########

##### CONSTANTS #####
HEIGHT = 215
WIDTH = 460
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
        self.grid()

        ###### VARIABLES ######
        self.difficultyLevel = 0
        self.maximumRange = 0
        self.guessNum = 0
        self.theNum = 0

        self.win = False
        ###### FINISHED #######

        self.create()

    def create(self):
        """ To use: create()
         This is the create function, it creates the app widgets."""
        ########### !! SETUP !! ############
        ######## .. LABEL .. ########
        self.difficultyLabel = Label(self, text = "Choose Difficulty: ")
        self.numGuessedLabel = Label(self, text = "Numbers Guessed: ")
        self.numEntryLabel =  Label(self, text = "Enter Number: ")
        ###### .. FINISHED .. ######

        ######## .. TEXT .. ########
        self.pastGuesses = Text(self)
        ###### .. FINISHED .. ######

        ###### .. ENTRIES .. #######
        self.numEntry = Entry(self)
        ###### .. FINISHED .. ######

        ###### .. BUTTONS .. #######
        self.easyBttn = Button(self, text = "Easy",
                                     command = self.easy)

        self.mediumBttn = Button(self, text = "Medium",
                                 command = self.medium)

        self.hardBttn = Button(self, text = "Hard",
                               command = self.hard)

        self.submit = Button(self, text = "Submit",
                             command = self.submitFunc)
        ###### .. FINISHED .. ######
        ###### !! SETUP FINISHED !! ########

        ###### !! GRID PLACEMENT !! #######
        ## Label Grid Placement
        self.difficultyLabel.grid(column = 1, row = 1)
        self.numGuessedLabel.grid(column = 1, row = 3)
        self.numEntryLabel.grid(column = 1, row =4)

        ## Text Grid Placement
        self.pastGuesses.grid(column = 2, row = 3, columnspan = 3, pady = 15, padx = 15)

        ## Entry Grid Placement
        self.numEntry.grid(column = 2, row = 4, columnspan = 4)

        ## Button Grid Placement
        self.easyBttn.grid(column = 2, row = 1)

        self.mediumBttn.grid(column = 3, row = 1)

        self.hardBttn.grid(column = 4, row = 1)

        self.submit.grid(column = 2, row = 5, columnspan =  4, pady = 15)
        ###### !! GRID FINISHED !! ########

        ###### !! CONFIGURATION !! ########
        ## .. Text .. ##
        self.pastGuesses.config(height = 5, width = 40)
        ## .. Fin  .. ##
        ###### !! CONFIG FINISH !! ########

    def easy(self):
        """ To use: self.easy()
        This is the Easy Difficulty function. It will determine how the game is played."""
        #### Difficulty variables ####
        self.difficultyLevel = 1
        self.guessNum = 3
        self.theNum = random.randint(1, 10)
        ## Finished Difficulty Var ##

        print(self.theNum)

        # Disabling the buttons:
        self.easyBttn.configure(state = DISABLED)
        self.mediumBttn.configure(state = DISABLED)
        self.hardBttn.configure(state = DISABLED)

        return self.guessNum, self.theNum

    def medium(self):
        """ To use: self.medium()
        This is the Medium Difficulty function. It will determine how the game is played."""
        #### Difficulty variables ####
        self.difficultyLevel = 2
        self.guessNum = 5
        self.theNum = random.randint(1, 50)
        ## Finished Difficulty Var ##

        # Disabling the buttons:
        self.easyBttn.configure(state=DISABLED)
        self.mediumBttn.configure(state=DISABLED)
        self.hardBttn.configure(state=DISABLED)

        return self.guessNum, self.theNum

    def hard(self):
        """ To use: self.hard()
        This is the Hard Difficulty function. It will determine how the game is played."""
        #### Difficulty variables ####
        self.difficultyLevel = 3
        self.guessNum = 10
        self.theNum = random.randint(1, 100)
        ## Finished Difficulty Var ##

        # Disabling the buttons:
        self.easyBttn.configure(state=DISABLED)
        self.mediumBttn.configure(state=DISABLED)
        self.hardBttn.configure(state=DISABLED)

        return self.guessNum, self.theNum

    def submitFunc(self):
        self.guess = self.guessNum # Tying the guessNum variable to the self.guess variable\


        if self.guess == self.theNum: # Saying that if the guess equals the determined number...
            mb.showinfo("You won!", "You won! Congratulations!")
            self.play = mb.askquestion("Play Again?", "Would you like to play again?")

            if self.play == True:
                self.easyBttn.configure(state = ACTIVE)
                self.mediumBttn.configure(state = ACTIVE)
                self.hardBttn.configure(state = ACTIVE)

                self.pastGuesses.delete(0, "end")
            else:
                mb.showinfo("Goodbye!", "Goodbye then.")
                self.quit()
        elif self.guess > self.theNum:
            mb.showinfo("Pertaining to your guess...", "Guess lower!")
        else:
            mb.showinfo("Pertaining to your guess...", "Guess higher!")

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
