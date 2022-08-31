#Importing Data
import os
from random import randint
    
desktop = os.path.join(os.path.expanduser("~"), "Desktop/Projects/ChoosingWhatToWatch") #creating a sort cut

#reading tv show file
if os.path.exists("Desktop/Projects/ChoosingWhatToWatch/tvShows.txt") == False:
    tvPath = open("tvShows.txt","x") #creating file if file doesn't exist
else:
    tvPath = os.path.join(desktop, "tvShows.txt") #importing data for TV shows

t = open(tvPath,"r") #important lesson - open doesn't mean read**
tvRead = t.read() 

#reading for Movie file
if os.path.exists("Desktop/Projects/ChoosingWhatToWatch/tvShows.txt/movies.txt") == False:
    moviePath = open("movies.txt","x")
else:
    moviePath = os.path.join(desktop, "movies.txt") #importing data for move

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
    print("5)\tSaved Movie and TV shows")
    print("6)\tExit Program")

def choice():
    #takes in choice and validates it to see if in range
    while True:
        menu()
        choice = int(input("selection: "))
        if choice >= 0 and choice <= 6:
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
        m.write(","+ addingList)
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

def printLists(choice):
    #prints out all the TV shows and Movies Saved
    if choice == 5:
        print("TV Shows\n--")
        for index in tvList:
            print(index)
        print("-------------")
        print("Movies\n--")
        for index in movieList:
            print(index)

def main():
    #main method
    pick = choice()
    while pick != 6:
        randomChoice = randomNum(pick)
        addtoList(pick)
        printLists(pick)
        printChoice(pick,randomChoice)
        pick = choice()
    print("Thank You for using my program :D")
    print("Created by Joseph McEnroe")
    
main()

