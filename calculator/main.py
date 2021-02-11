# Daniel Lehman
# Lisette Spalding

from tkinter import *
#from tkinter.ttk import *



class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.indexs = [0, 0, 0, 1, 1, 1, 2, 2, 2]
        self.grid()
        self.pack()
        self.create_widgets()

    #add widgets
    def create_widgets(self):
        self.screen = Label(self, bg="gray")
        for i in range(9):
            self.bttn = Button(self, text=f"{i+1}", bg="orange", command=self.handle_click)
            self.bttn.grid(row=self.indexs[i], column=i % 3)
            self.bttn0 = Button(self, text="0", bg="orange", command=self.handle_click)
            self.addbttn = Button(self, text="+", bg="orange", command=self.opp_click)
            self.subbttn = Button(self, text="-", bg="orange", command=self.opp_click)
            self.multbttn = Button(self, text="x", bg="orange", command=self.opp_click)

            self.screen.grid(row=0, column=0, columnspan=3)
            self.bttn0.grid(row=4, column=1)
            self.addbttn.grid(row=2, column=3)
            self.subbttn.grid(row=1, column=3)
            self.multbttn.grid(row=0, column=3)


    def handle_click(self):
        pass

    def opp_click(self):
        pass



def main():
    root = Tk()
    root.title("Text Boxes")
    root.geometry("300x250")
    root.attributes("-fullscreen",False)
    app = App(root)

    root.mainloop()

main()