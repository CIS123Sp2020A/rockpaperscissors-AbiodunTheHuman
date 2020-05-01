#Abiodun Scott
#a GUI that will simulate the game Rock Paper Scissors using radio buttons

#import tkinter
import tkinter
import tkinter.messagebox as box

#import random
import random

class MyGUI:
    def __init__(self):
        # Create the main window
        self.mainWindow = tkinter.Tk()
        #name the window
        self.mainWindow.title('Rock, Paper, Scissors!')
        self.mainWindow.geometry("300x100")
        

        #create a frame for the radio buttons
        self.radioFrame = tkinter.Frame(self.mainWindow)
        #create a frame for regular button widgets
        self.buttonFrame = tkinter.Frame(self.mainWindow)

        #Create an IntVar object to use with the radio buttons
        self.radioVar = tkinter.StringVar()
        self.radioVars = tkinter.StringVar()
        self.resultVar = tkinter.StringVar()

        #Create radio buttons labeled Rock Paper Scissors; rock paper scissors radio frame
        self.rb1 = tkinter.Radiobutton(self.radioFrame, text='Rock', variable=self.radioVar, value='Rock')
        self.rb2 = tkinter.Radiobutton(self.radioFrame, text='Paper', variable=self.radioVar, value='Paper')
        self.rb3 = tkinter.Radiobutton(self.radioFrame, text='Scissors', variable=self.radioVar, value='Scissors')

        # Pack the radio buttons
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        #Create play and quit buttons; okay and quit button frame
        self.okayButton = tkinter.Button(self.buttonFrame, text='Okay', command=self.displayInfo)
        self.quitButton = tkinter.Button(self.buttonFrame, text='Quit', command=self.mainWindow.destroy)

        # Pack the Buttons
        self.okayButton.pack(side='left')
        self.quitButton.pack(side='left')

        # Pack the frames
        self.radioFrame.pack()
        self.buttonFrame.pack()

        #start the GUI running and keep it running
        tkinter.mainloop()


    #Generate a computer move (like TicTacToe;Rock (0), Paper (1), Scissors (2)
    #this will be displayed with the selection (message box)
    def displayInfo(self):
        self.randomNum = random.randint(0,2)

        if self.randomNum == 0:
            self.radioVars.set('Rock')
        elif self.randomNum == 1:
            self.radioVars.set('Paper')
        else:
            self.radioVars.set('Scissors')


        #Implement a game play function
        box.showinfo('Selection',('Computer selected: ' + self.radioVars.get(),
                                  'You selected: ' + self.radioVar.get()))
        #if the player chooses Rock beats Scissors, the player wins (state the moves made and that the player wins)   
        if ((self.radioVars.get() == 'Scissors') and (self.radioVar.get() == 'Rock')):    
            self.resultVar.set('Rock crushes Scissors. You win!')

        #if the player chooses Paper beats Rock, the player wins (state the moves made and that the player wins)
        elif ((self.radioVars.get() == 'Rock') and (self.radioVar.get() == 'Paper')):
            self.resultVar.set('Paper covers Rock. You win!')

        #if the player chooses Scissors beats Paper, the player wins (state the moves made and that the player wins)    
        elif ((self.radioVars.get() == 'Paper') and (self.radioVar.get() == 'Scissors')):
            self.resultVar.set('Scissors beats Paper. You win!')

        #if the player chooses Rock and the computer chooses Paper, the player loses (state the moves made and that the player loses)  
        elif ((self.radioVars.get() == 'Paper') and (self.radioVar.get() == 'Rock')):
            self.resultVar.set('Paper covers Rock. You lose.')

        #if the player chooses Paper and the computer chooses Scissors, the player loses (state the moves made and that the player loses)       
        elif ((self.radioVars.get() == 'Scissors') and (self.radioVar.get() == 'Paper')):
            self.resultVar.set('Scissors beats Paper. You lose.')

        #if the player chooses Scissors and the computer chooses Rock, the player loses (state the moves made and that the player loses) 
        elif ((self.radioVars.get() == 'Rock') and (self.radioVar.get() == 'Scissors')):
            self.resultVar.set('Rock crushes Scissors. You lose.')

        
        #if player plays Rock and computer plays Rock, it's a draw
        elif ((self.radioVars.get() == 'Rock') and (self.radioVar.get() == 'Rock')):    
            self.resultVar.set("Rock ties with Rock. It's a draw!")

        #if player plays Paper and computer plays Paper, it's a draw
        elif ((self.radioVars.get() == 'Paper') and (self.radioVar.get() == 'Paper')):    
            self.resultVar.set("Paper ties with Paper. It's a draw!")

        #if player plays Scissors and computer plays Scissors, it's a draw
        else: #((self.radioVars.get() == 'Paper') and (self.radioVar.get() == 'Paper')):    
            self.resultVar.set("Scissors ties with Scissors. It's a draw!")
            
        

       #pop up box to display the results
        box.showinfo('Winner',(self.resultVar.get()))

#create an instance of the MyGUI class
demoGUI = MyGUI()
