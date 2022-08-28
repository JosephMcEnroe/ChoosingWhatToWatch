#Importing Data
import os
    
desktop = os.path.join(os.path.expanduser("~"), "Desktop/Projects/ChoosingWhatToWatch") #importing file
tvPath = os.path.join(desktop, "tvShow.txt") #importing txt for TV shows
moviePath = os.path.join(desktop, "movies.txt")

#reading tv show file
t = open(tvPath,"r") #important lesson - open doesn't mean read**
tvRead = t.read()

#reading for Movie file
m = open(moviePath, "r")
movieRead = m.read()

#turning files into list
tvList = list(tvRead.split(","))
movieList = list(movieRead.split(","))
print(movieList)