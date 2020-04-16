import tkinter
import tkinter.messagebox as box

class MyGUI:
    def __init__(self):
        # Create the main window.
        self.mainWindow = tkinter.Tk()
        self.mainWindow.geometry("200x200")

        # Create two frames. One for the Radiobuttons
        # and another for the regular Button widgets.
        self.radioFrame = tkinter.Frame(self.mainWindow)
        # self.middle_frame = tkinter.Frame(self.main_window)
        self.buttonFrame = tkinter.Frame(self.mainWindow)

        # Create an IntVar object to use with
        # the Radiobuttons.
        self.radioVar = tkinter.StringVar()

        # Set the intVar object to 1.
        self.radioVar.set(1)

        # Create the Radiobutton widgets in the top_frame.
        self.rb1 = tkinter.Radiobutton(self.radioFrame, text='Option 1', variable=self.radioVar, value='Option 1')
        self.rb2 = tkinter.Radiobutton(self.radioFrame, text='Option 2', variable=self.radioVar, value='Option 2')

        # Pack the Radiobuttons.
        self.rb1.pack()
        self.rb2.pack()

        # Set up buttons
        self.okButton = tkinter.Button(self.buttonFrame, text='OK', command=self.showOption)
        self.quitButton = tkinter.Button(self.buttonFrame, text='Quit', command=self.mainWindow.destroy)

        # Pack the Buttons.
        self.okButton.pack(side='left')
        self.quitButton.pack(side='left')

        # Pack the frames.
        self.radioFrame.pack()
        self.buttonFrame.pack()

        # Start the mainloop.
        tkinter.mainloop()

    def showOption(self):
        box.showinfo('Selection', 'You selected ' + self.radioVar.get())

demoGUI = MyGUI()
