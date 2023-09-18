import requests
import http.client
import apikey
import constants
import os

headers = {
	"X-RapidAPI-Key": apikey.APIKEY,
	"X-RapidAPI-Host": constants.BASEURL
}
conn = http.client.HTTPSConnection(constants.BASEURL)

# 1) see upcoming movies/tv series:

# conn.request("GET", "/titles/x/upcoming", headers=headers) 


# 2) searching for movies/tv series by keyword:

# conn.request("GET", "/titles/search/keyword/children", headers=headers) 


# 3) searching for movies by title, it DOES NOT have to be exactly word "Lost" as a title, for example: "Lost Dogs", "Lost Vegas" etc:

# conn.request("GET", "/titles/search/title/Lost", headers=headers)


# 4) searching for movies by title, IT HAS to be exactly word "Lost" as a title:

# conn.request("GET", "/titles/search/title/Lost?exact=true", headers=headers) 


# 5) searching for movies by title + limit of titles per page + base info:

# conn.request("GET", "/titles?titleType=Lost&info=base_info&limit=1", headers=headers)



# 6) shows genres:

# conn.request("GET", "/titles/utils/genres", headers=headers)


# 7) shows movie/tv series titles based on chosen genre + limit of titles per page:

# conn.request("GET", "/titles?genre=Horror&limit=5", headers=headers)


# 8) shows movie/tv series titles based on chosen genre + limit of titles per page + basic info:

# conn.request("GET", "/titles?genre=Horror&info=base_info&limit=5", headers=headers)


# PROJECT
os.system('cls')
print("Welcome to Movie Base!")
name = input("What's your name?\n")
os.system('cls')
#print("Hello " + name + ("! Nice to meet you! \nWhat would you like to do?"))

title1 = "Hello " + name + "! Nice to meet you! \nWhat would you like to do?"
options1 = ["find a movie to watch", "search for movie by title", "see a list of movie genres", "see a list of upcoming movies"]
title2 = "How many search results do you want to get? Please choose a number from 1 to 10:"

def printPage(question, answers):
    print(question)
    for index, elem in enumerate(answers):
        print(str(index+1) + ". " + elem)

def askQuestion(question, numberOfAnswers):
    choice = input(question)

    while int(choice) < 1 or int(choice) > numberOfAnswers:
        choice = input(f"Choose one of the numbers between 1 and " + str(numberOfAnswers) + ": ") 

    return choice  

printPage(title1, options1)

# asking user what he wants to do:
chosenAnswer = askQuestion("Please choose a number: ", len(options1))
os.system('cls')
print(f"You chose: {options1[int(chosenAnswer)-1]}")

# asking user for movie title
def askForMovieTitle():
    movieTitle = input("Please enter movie title: ")
    print(f"Entered movie title: " + movieTitle)

# asking user how many page results he wants to get (option 1, 2, 4):
def howManyResults():
    finalChoice = askQuestion(title2, 10)
    print(f"You chose: {finalChoice} search results")

def chooseGenre():
    print("You chose: choose genre")

def displayResults():
    print("display results")

def whetherItsExactTitle():
    print("You chose: whether it exact title")
    
def showGenres():
    print("You chose: show genres")

def returnToMenu():
    print("You chose: return to menu")

def upcomingMovies():
    print("You chose: upcoming movies")

def handleAnswer(answer):
    if answer ==  "1":
        chooseGenre()
        howManyResults()
        displayResults()
        returnToMenu()
        # 1. choose genre
        # 2. how many results
        # 3. display results
        return
    elif answer == "2":
        askForMovieTitle()
        whetherItsExactTitle()
        howManyResults()
        displayResults()
        returnToMenu()
        # 1. ask for title - askForMovieTitle()
        # 2. ask whether its exact title Y/N
        # 3. how many results
        # 4. display results
        return
    elif answer == "3":
        showGenres()
        returnToMenu()
        # 1. show genres
        # 2. on click return to question 1
        return
    elif answer == "4":
        howManyResults()
        upcomingMovies()
        returnToMenu()
        # 1. how many results
        # 2. show upcoming movies
        return
    else:
        print("choose a different number")
        return

handleAnswer(chosenAnswer)





# asking user if the movie title he entered has to be the exact name of a title or not:

def searchExactMovieTitle():
    exactMovieTitle = input("Can the search results include movie titles that contain other words in addition to the word you entered? Please enter y for yes or n for no.")
    if exactMovieTitle == "y":
        print("You chose: yes")
    if exactMovieTitle == "n":
        print("You chose: no")
    if exactMovieTitle not in ["y", "n"]:
        input("Please type y or n")
    return searchExactMovieTitle








# wyświetla się odpowiedź z api:
# conn.request("GET", "/titles/utils/genres", headers=headers)
# res = conn.getresponse()
# data = res.read()
# print(data.decode("utf-8"))

# response = requests.get(url = URL, params = conn.request("GET", "/titles/utils/genres", headers=headers))
# print(response.json())

"""
conn.request("GET", "/titles/utils/genres", headers=headers)
def choices():
    if whatToDo[choice] == 2:
        print(data.decode("utf-8"))

print(data.decode("utf-8"))

"""
"""
def optionsss(optionone, optiontwo, optionthree):
    optionone = 0
    optiontwo = conn.request("GET", "/titles/utils/genres", headers=headers)
    optionthree = 0
    print(optiontwo)

"""

"""
if whatToDo[choice] == 2:
    optiontwo = conn.request("GET", "/titles/utils/genres", headers=headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
"""

"""
res = conn.getresponse()
data = res.read()
conn.request("GET", "/titles/utils/genres", headers=headers)

if user_input == 2:
    print(data.decode("utf-8"))
"""