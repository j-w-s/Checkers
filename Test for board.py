from tkinter import *

#make board in tkinter

###Board Class###
class Board(Canvas):
    def __init__(self,container):
        Canvas.__init__(self,container)
        self.setupGUI()


    def setupGUI(self):
        
        #Name in top left corner
        self.Name = Label(self, text = ("Lets play Chess!"), height =5, width = 20, font = ("Arial",10), background = "white")
        self.Name.grid(row=0,column=0)
        
        #creates a loop for rows
        for rows in range(1,9):
            #create row names
            self.rowname = Label(self,text=(rows), height = 5, width =5, background = "gray93")
            self.rowname.grid(row=rows,column=0, sticky = E)

            topLabels = ['A','B','C','D','E','F','G','H']
            #inner loop for columns
            for col in range(1,9):
                #create column names
                self.letter = Label(self,text=topLabels[col-1], height =2, width = 10, background="gray93")
                self.letter.grid(row = 0, column=col, sticky = S)
                
                #variable to make checkboard look
                offset = 0

                #if the row is 0,2,4,6,8
                if rows%2 == 0:
                    offset = 1

                #if the column is 1,3,5,7 and row is 0,2,4,6,8
                #make the box brow
                if (col + offset)%2 == 0:
                    self.box1 = Canvas(self, height = 90, width = 90, background = "Light yellow")
                    self.box1.grid(row=rows,column=col)
                else:
                    self.box1 = Canvas(self, height = 90, width = 90, background = "brown")
                    self.box1.grid(row=rows,column=col)
                

        self.pack(fill = BOTH, expand = 1)
        


###Main Code###
window = Tk()
window.title("Board")

#create an instance of board
b1 = Board(window)

#render the GUI in the mainloop
window.mainloop()
