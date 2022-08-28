#Importing Data
import os
    
desktop = os.path.join(os.path.expanduser("~"), "Desktop/Projects/ChoosingWhatToWatch") #importing file
tvPath = os.path.join(desktop, "tvShow.txt") #importing data for TV shows
moviePath = os.path.join(desktop, "movies.txt") #importing data for move

#reading tv show file
t = open(tvPath,"r") #important lesson - open doesn't mean read**
tvRead = t.read()

#reading for Movie file
m = open(moviePath, "r")
movieRead = m.read()

#turning files into list
tvList = list(tvRead.split(","))
movieList = list(movieRead.split(","))

def menu():
    #prints out menu
    print("\t\tMenu")
    print("1)\tChoose a Random TV Show")
    print("2)\tChoose a Random Movie")

def choice():
    #takes in choice and validates it to see if in range
    choice = input(menu())
    choice = int(choice)
    if choice <= 0 or choice >= 3:
        while(choice <= 0 or choice >= 3):
            choice = input(menu())
            choice = int(choice)
choice()
