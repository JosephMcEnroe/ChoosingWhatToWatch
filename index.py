#Importing Data
import os
from random import randint
    
desktop = os.path.join(os.path.expanduser("~"), "Desktop/Projects/ChoosingWhatToWatch") #creating a sort cut
tvPath = os.path.join(desktop, "tvShow.txt") #importing data for TV shows
moviePath = os.path.join(desktop, "movies.txt") #importing data for move

#reading tv show file
t = open(tvPath,"r+") #important lesson - open doesn't mean read**
tvRead = t.read() 

#reading for Movie file
m = open(moviePath, "r+")
movieRead = m.read()

#turning files into list
tvList = list(tvRead.split(","))
movieList = list(movieRead.split(","))

def menu():
    #prints out menu
    print("\t\tMenu")
    print("1)\tChoose a Random TV Show")
    print("2)\tChoose a Random Movie")
    print("3)\tAdd a TV Show to Watch")
    print("4)\tAdd a Movie to Watch")

def choice():
    #takes in choice and validates it to see if in range
    while True:
        menu()
        choice = int(input("selection: "))
        if choice >= 0 and choice <= 3:
            return choice
def randomNum(choice):
    #picks a random number based on the list's range
    import random 
    if choice == 1:
        return(randint(0,len(tvList)-1))
    elif choice == 2:
        return(randint(0,len(movieList)-1))
    else: 
        return None

def addtoList(choice):
    #adds to data file
    if choice == 3:
        addingList = input("What do you want to add to list(split TV shows using ','):")
        t.write("," + addingList)
    if choice == 4:
        addingList = input("What do you want to add to list(split movies using ','):")
        m.write(addingList)
    else:
        return None
    
    #updating program
    tvRead = t.read() 
    movieRead = m.read()

    #updating list
    tvList = list(tvRead.split(","))
    movieList = list(movieRead.split(","))
    print(tvList)
    print(movieList)
    
def printChoice(choice,rand):
    #prints out choice for the night
    if choice == 1:
        print(tvList[rand])
    elif choice == 2:
        print(movieList[rand])




pick = choice()
randomChoice = randomNum(pick)
addtoList(pick)
printChoice(pick,randomChoice)

