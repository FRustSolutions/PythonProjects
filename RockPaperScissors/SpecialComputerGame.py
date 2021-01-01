#python program for special Rock/Paper/Scissors game - Frank Rust   ID:2116008
#last edited 13/11/2019

from tkinter import *               #for GUI functions/widgets
import tkinter.messagebox           #for messagebox Popup notifications
import random                       #for computer choice

root=Tk()
root.title('SpecialComputerGame')

def start_game():                       #function to start game when pressing the start button
    global roundcounter                 #set as global variables which are created and reset inside the function
    roundcounter=0                      #these get reset when start_game() is called again for a new tournament
    global pwins
    pwins=0
    global cwins
    cwins=0
    global playframe                    #all the widgets for the current tournament get stored in this frame
    playframe=LabelFrame(root,borderwidth=5)        #it gets deleted when the current tournament ends
    playframe.grid(row=7,column=0,columnspan=7)
    

    class GameGUI:                      #this class holds all the main widgets and functions

        def __init__(self,master):      #initialising main buttons and labels

            self.labelPick=Label(root, text='Your Pick:').grid(row=2,sticky=W,padx=4)   #Label:Your Pick:

            #creating all the buttons for the possible choices and give the input as argument to get_palyer_choice()
            self.rockButton=Button(root, text='Rock',font='Helvetica 10 bold',command=lambda:self.get_player_choice('Rock'))   #lambda command to avoid automatic execution with input argument
            self.rockButton.grid(row=2,column=1,sticky=W,ipadx=20, pady=10, ipady=20)
            
            self.paperButton=Button(root, text='Paper',font='Helvetica 10 bold',command=lambda:self.get_player_choice('Paper'))
            self.paperButton.grid(row=2,column=2,sticky=W,ipadx=20,ipady=20)
            
            self.scissorsButton=Button(root, text='Scissors',font='Helvetica 10 bold',command=lambda:self.get_player_choice('Scissors'))
            self.scissorsButton.grid(row=2,column=3,sticky=W,ipadx=15,ipady=20)
            
            self.lizardButton=Button(root, text='Lizard',font='Helvetica 10 bold',command=lambda:self.get_player_choice('Lizard'))
            self.lizardButton.grid(row=2,column=4,sticky=W,ipadx=20,ipady=20)
            
            self.spockButton=Button(root, text='Spock',font='Helvetica 10 bold',command=lambda:self.get_player_choice('Spock'))
            self.spockButton.grid(row=2,column=5,sticky=W,ipadx=20,ipady=20)

            self.widthlabel=Label(playframe,text='Tournament Window',font='Helvetica 10 bold',width=90).grid(row=2,sticky=N,columnspan=7)   #this Label with a set width of 90 holds everything in place
                       
            playButton=Button(root, text='PLAY!',fg="red", font='Helvetica 10 bold',command=self.play_round).grid(row=5, column=1, columnspan=5, ipadx=100)

            self.rulesButton=Button(root,text='Torunament Rules',command=lambda:self.showRules())           #additional button with function that shows the game rules
            self.rulesButton.grid(row=10,column=6,sticky=E,padx=4)

            exitButton=Button(root, text='Exit Game',command=root.destroy).grid(row=11,column=6,sticky=E,padx=4)            #exitButton destroys the main root and thereby the whole GUI window


        #additional functionality: showing tournament rules with win-condition image 
        def showRules(self):
            def hide_rules():                       #to hide tournament rules
                labelrules.grid_forget()            #grid_forget to remove label from grid display
                labelpng.grid_forget()              #will also remove the picture
                hideButton.grid_forget()            #and the hide button itself

            #showing tournament rules in labels:  
            labelrules=Label(root, text="\nA tournament consits of 5 games. Whoever wins the most games wins the tournament. \nThese are the winning conditions: ")
            labelrules.grid(row=13, sticky=N,columnspan=8)
            rulespng=PhotoImage(file="GameRulesImage600px.png")             #opens .png-file with PhotoImage() and put it in variable labelpng
            labelpng=Label(root, image=rulespng)                            #and store labelpng in an actual Label
            labelpng.image = rulespng                                       #otherwise image is blank because of missing reference (source:http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.html)
            labelpng.grid(row=14,column=0,sticky=N,columnspan=7)
            hideButton=Button(root,text="Hide Rules", command=hide_rules)
            hideButton.grid(row=10,column=5,padx=4,sticky=E)
            

        #method to show the current player choice: this option can still be changed before pressing play:
        def get_player_choice(self,choice):     
            self.labelchoice=Label(playframe, text='  Your pick:').grid(row=3,sticky=N)
            
            self.currentchoice=choice                                               #stores the choice from input argument from the buttons ('Rock'/'Paper'/...)                                          
            self.labelchoice=Label(playframe,text='             ').grid(row=4)      #empty text to overwrite the old choice in the label            
            self.labelchoice=Label(playframe,text=choice).grid(row=4)               #current choice in label output

            #adding images for the current player choices(additional functionality):
            filetxt=str(choice)+'.png'                                              #adds the strings to open the according .png files
            imgchoice=PhotoImage(file=filetxt)                                      #storing image in imgchoice
            choicelabel=Label(playframe, image=imgchoice)                           #outputting image choice in the label
            choicelabel.image=imgchoice                                             #otherwise image is blank because of missing reference 
            choicelabel.grid(row=5,sticky=W,columnspan=2)


        #method to play the round when the final choice is made and play button is pressed: 
        def play_round(self):                   
            try:                                                                    #exception handling for error when no choice was made before pressing play
                global roundcounter                                                 #using the global variable for the counter and incrementing by 1 for each round played
                roundcounter=roundcounter+1
                   
                print('\nPlaying Round Number:',roundcounter)
                global pwins_count                                                  #these will be reset each time the play-button is pressed
                pwins_count=0
                global cwins_count
                cwins_count=0
                global result
                result=0
                
                print('You picked:',self.currentchoice)
                
                self.listchoice=['Rock','Paper','Scissors','Lizard','Spock']            #create a list for computer choice 
                j=random.randint(0,4)                                                   #computer choice via RNG 0 to 4 decides the index from list      
                global cchoice                                                          #method creates a global variable that is used in other classes
                cchoice=self.listchoice[j]                                              #store listobject with index j in cchoice
                print('Computer picked:',cchoice)          
                
                self.labetextcchoice=Label(playframe,text='Computers pick:').grid(row=3,sticky=N,column=6, columnspan=2)
                self.labelcchoice=Label(playframe,text="              ").grid(row=4,column=6)           #easy way to overwrite the old choice with empty text/spaces
                self.labelcchoice=Label(playframe,text=cchoice).grid(row=4,column=6)                    #overwriting empty label text with computer choice

                #adding images for the computer choices(additional functionality):
                filetxt=str(cchoice)+'.png'                                             #string as filename to open the according .png files
                imgchoice=PhotoImage(file=filetxt)                                      #storing image in imgchoice
                choicelabel=Label(playframe, image=imgchoice)                           #same principle as player image
                choicelabel.image=imgchoice
                choicelabel.grid(row=5,sticky=E, column=6,columnspan=2)

                #creating the classes that give the game results according to the player's choice
                if self.currentchoice=='Rock':                      #if statements to check for current player choice
                    a=Rock()                                        #creating an object of class Rock()
                elif self.currentchoice=='Paper':
                    a=Paper()
                elif self.currentchoice=='Scissors':
                    a=Scissors()
                elif self.currentchoice=='Lizard':
                    a=Lizard()
                elif self.currentchoice=='Spock':
                    a=Spock()
                    
            except AttributeError:                                  #Exception Handling: AttributeError if no choice was made before pressing play
                print('You need to pick first')
                tkinter.messagebox.showerror('Oops','Please pick before pressing Play!')
                roundcounter=0                                      #reset if you started first round without a choice


        #method to show the game results in the GUI that gets called from the choice classes (Rock(),Paper(),...) after calculating the results:    
        def show_results(result,pwins,cwins):                                       #takes input arguments from the choice classes (Rock(),Paper(),...)that are created underneath and that call this method
            print(result,'\nPlayer wins:',pwins,'Computer wins:',cwins)

            roundcounttext=('RoundNo.',roundcounter,'/5')
            roundlabel=Label(playframe,text=roundcounttext).grid(row=6,column=2,sticky=N,columnspan=3)                              #roundcounter Label

            resultlabel=Label(playframe,text='                                                                                            ').grid(row=7,column=2,sticky=N,columnspan=3)  #overwriting Label
            resultlabel=Label(playframe,text=result,font='Helvetica 10 bold').grid(row=7,column=2,sticky=N,columnspan=3)            #Label for result of last round

            scorelabel=Label(playframe,text='Current Score:').grid(row=8,columnspan=7)
            scoretext=('Player',pwins,':',cwins,'Computer')
            scorecountlabel=Label(playframe,text=scoretext,font='Helvetica 10 bold').grid(row=9,columnspan=7)                       #Scoreboard Label


            #to end/restart tournament after 5 rounds:
            if roundcounter ==5:
                if pwins>cwins:                                                                                                     #storing the tournament rersult in tournresult according to who won more rounds
                    tournresult='Congratulations! You won the tournament!'
                if pwins<cwins:
                    tournresult='You lost the tournament. Better luck next time!'
                elif pwins==cwins:
                    tournresult='The tournament ended in a draw'
                reslabel=Label(playframe,text=tournresult,font='Helvetica 12 bold').grid(row=10,columnspan=7)                       #tournament result Label
                MsgBox=tkinter.messagebox.askquestion(tournresult,'\nDo you want to play another tournament?')                      #messagebox with tournament result asking to play again
                if MsgBox=='yes':                                                                                                   #if click yes in messagebox the game restarts
                    tkinter.messagebox.showinfo('Restart','Starting a new tournament')                                  
                    playframe.destroy()                                                                                             #the frame holding the widgets for current tournament gets destroyed
                    start_game()                                                                                                    #game gets started again via start_game() function, which recreates the frame
                    
                else:
                    tkinter.messagebox.showinfo('Exit','The game is closing.')                                                      #if click no in messagebox the program exits
                    root.destroy()                                                                                                  #by destroying the main program root 
                

       
    #the following are the classes for the different player picks that calculate the game results:
                    
    class Rock(GameGUI):                                #class for player pick: Rock, takes GameGUI as parent class to share its variables+methods
                                                        
        def __init__(self):
            self.cwins=0                    
            self.pwins=0
          
            if cchoice=='Rock':                         #checks computer choices and stores the outcome of the game in result
                result='Tie! Both chose Rock'
            elif cchoice=='Paper':
                result='Computer wins: Paper covers Rock'
                self.cwins+=1                           #incrementing computer win
            elif cchoice=='Scissors':
                result='You win: Rock crushes Scissors'
                self.pwins+=1                           #incrementing player win
            elif cchoice=='Lizard':
                result='You win: Rock crushes Lizard'
                self.pwins+=1
            elif cchoice=='Spock':
                result='Computer wins: Spock vaporizes Rock'
                self.cwins+=1
            
            if self.pwins==1:                           #whoever won last round gets +1 on global win counters pwins,cwins
                global pwins
                pwins+=1
            elif self.cwins==1:
                global cwins
                cwins+=1

            GameGUI.show_results(result,pwins,cwins)        #calls the show_results() method in class GameGUI to show the results in the GUI; result and win counters as arguments
            

    class Paper(GameGUI):                   #class for player pick: Paper                         
                                                        
        def __init__(self):
            self.cwins=0                    
            self.pwins=0
            
            if cchoice=='Rock':
                result='You win: Paper covers Rock'
                self.pwins+=1
            elif cchoice=='Paper':
                result='Tie! Both chose Paper'
            elif cchoice=='Scissors':
                result='Computer wins: Scissors cuts Paper'
                self.cwins+=1
            elif cchoice=='Lizard':
                result='Computer wins: Lizard eats Paper'
                self.cwins+=1
            elif cchoice=='Spock':
                result='You win: Paper disproves Spock'
                self.pwins+=1

            if self.pwins==1:                  
                global pwins
                pwins+=1
            elif self.cwins==1:
                global cwins
                cwins+=1
                
            GameGUI.show_results(result,pwins,cwins)
            
            
    class Scissors(GameGUI):                    #class for player pick: Scissors              
                                                        
        def __init__(self):
            self.cwins=0                    
            self.pwins=0
            
            if cchoice=='Rock':
                result='Computer wins: Rock crushes Scissors'
                self.cwins+=1
            elif cchoice=='Paper':
                result='You win: Scissors cuts Paper'
                self.pwins+=1
            elif cchoice=='Scissors':
                result='Tie! Both chose Scissors'
            elif cchoice=='Lizard':
                result='You win: Scissors decapitates Lizrad'
                self.pwins+=1
            elif cchoice=='Spock':
                result='Computer wins: Spock smashes Scissors'
                self.cwins+=1

            if self.pwins==1:                   
                global pwins
                pwins+=1
            elif self.cwins==1:
                global cwins
                cwins+=1
                
            GameGUI.show_results(result,pwins,cwins)                 


    class Lizard(GameGUI):                  #class for player pick: Lizard                     
                                                        
        def __init__(self):
            self.cwins=0                    
            self.pwins=0
            
            if cchoice=='Rock':
                result='Computer wins: Rock crushes Lizard'
                self.cwins+=1
            elif cchoice=='Paper':
                result='You win: Lizard eats Paper'
                self.pwins+=1
            elif cchoice=='Scissors':
                result='Computer wins: Scissors secapitates lizard'
                self.cwins+=1
            elif cchoice=='Lizard':
                result='Tie! Both chose Lizard'
            elif cchoice=='Spock':
                result='You win: Lizard poisons Spock'
                self.pwins+=1

            if self.pwins==1:                   
                global pwins
                pwins+=1
            elif self.cwins==1:
                global cwins
                cwins+=1
                
            GameGUI.show_results(result,pwins,cwins)            
            

    class Spock(GameGUI):                                 
                                                            #class for player pick: Spock
        def __init__(self):
            self.cwins=0                    
            self.pwins=0
            
            if cchoice=='Rock':
                result='You win: Spock vaporizes Rock'
                self.pwins+=1
            elif cchoice=='Paper':
                result='Computer wins: Paper disproves Spock'
                self.cwins+=1
            elif cchoice=='Scissors':
                result='You win: Spock smashes Scissors'
                self.pwins+=1
            elif cchoice=='Lizard':
                result='Computer wins: Lizard poisons Spock'
                self.cwins+=1
            elif cchoice=='Spock':
                result='Tie! Both chose Spock'

            if self.pwins==1:                   
                global pwins
                pwins+=1
            elif self.cwins==1:
                global cwins
                cwins+=1
                
            GameGUI.show_results(result,pwins,cwins)
                                                        #########################created all the classes for the choices

        
    a=GameGUI(root)                 #object of class GameGUI created when pressing Start Game Button


#Widgets on Start Screen:
Label(root, text='Player name:').grid(row=0,sticky=W)
nameEntry=Entry(root)
nameEntry.grid(row=1,sticky=W,pady=10)
startbutton=Button(root,text='Start Game',font='Helvetica 12 bold',width=8,padx=20,command=lambda:welcome())            #start button with command welcome()
startbutton.grid(row=2,sticky=W)

def welcome():                                                                                                          #welcome function
    name=nameEntry.get()
    if name=='':                                                                                                        #messagewindow if no name was entered before pressing start game
        tkinter.messagebox.showerror('Oops','Please insert a valid name')
    else:                                                                                                               #if a name was entered before pressing start the game starts:
        nameEntry.config(state=DISABLED)                                                                                #disabling entry so name cant be changed afterwards                     
        welcometext=('Welcome',name)
        tkinter.messagebox.showinfo('Welcome',welcometext)                                                              #messagewindow welcoming the player with name
        print('Welcome',nameEntry.get())
        start_game()                                                                                                    #function to start the game!
        startbutton.grid_forget()                                                                                       #deleting the startbutton from the grid
        
root.mainloop()                              #to keep the program running in a loop
