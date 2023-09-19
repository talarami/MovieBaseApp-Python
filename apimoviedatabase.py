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


def printPage(question, answers):
    print(question)
    for index, elem in enumerate(answers):
        print(str(index+1) + ". " + elem)

def askQuestion(question, numberOfAnswers):
    choice = input(question)

    while int(choice) < 1 or int(choice) > numberOfAnswers:
        choice = input(f"Choose one of the numbers between 1 and " + str(numberOfAnswers) + ": ") 
    return choice  

# asking user for movie title
def askForMovieTitle():
    os.system("cls")
    title = input("Please enter movie title: ")
    return title

# asking user how many page results he wants to get (option 1, 2, 4):
def howManyResults():
    os.system("cls")
    return askQuestion("How many search results do you want to get? Please choose a number 1 to 10:", 10)
 
# showing user a list of genres and letting user choose a genre
def chooseGenre(genres):
    os.system("cls")
    printPage("List of genres:", genres)
    return askQuestion("Choose genre:", len(genres))

# asking user if its exact movie title
def whetherItsExactTitle():
    os.system("cls")
    answer = ""
    while answer.lower() != "y" and answer.lower() != "n":
        answer = input("Is that an exact movie title? (Y/N)")
    return answer

# showing user a list of genres
def showGenres():
    os.system("cls")
    print("You chose: show genres")
    genres = getGenres()
    return printPage("List of genres", genres)

def returnToMenu():
    input("Press enter to return to menu...")
    displayMenu()

# API calls

def getGenres():
    genres = ["drama", "horror", "comedy"]
    # conn.request("GET", "/titles/utils/genres", headers=headers)
    # res = conn.getresponse()
    # data = res.read()
    # print(data.decode("utf-8"))
    return genres

def getUpcomingMovies(numberOfResults):
    os.system("cls")
    print("You chose: upcoming movies")
    listOfMovies = ["Terminator", "Titanic", "ABC", "Lost", "Fargo"]
    return listOfMovies[:numberOfResults]

def getMoviesWithinGenre(genre, numberOfResults):
    listOfMovies = ["Terminator", "Titanic", "ABC", "Lost", "Fargo"]
    return listOfMovies[:numberOfResults]

def getMovieByTitle(title, exact, numberOfResults):
    listOfMovies = ["Terminator", "Titanic", "ABC", "Lost", "Fargo"]
    return listOfMovies[:numberOfResults]

# Application logic
def handleAnswer(answer):
    if answer ==  "1":
        # 1.get genres from API
        genres = getGenres()
        # 2. choose genre
        genreIndex = chooseGenre(genres)
        genre = genres[int(genreIndex) - 1]
        print("You chose " + genre)
        # 3. how many results
        numberOfResults = howManyResults()
        print("You chose " + numberOfResults + "results.")
        # 4. call to api to get x results within this genre
        result = getMoviesWithinGenre(genre, int(numberOfResults))
        # 5. display results
        printPage("List of movies:", result)
        # 6. return to menu
        returnToMenu()
        return
    elif answer == "2":
        # 1. ask for title
        title = askForMovieTitle()
        print("You chose " + title)
        # 2. ask whether its exact title Y/N
        exact = whetherItsExactTitle()
        # 3. how many results
        numberOfResults = howManyResults()
        # 4. call api for movie data
        result = getMovieByTitle(title, exact, int(numberOfResults))
        # 5. display results
        printPage("List of movies:", result)
        # 6. return to menu
        returnToMenu()
        return
    elif answer == "3":
        # 1. show genres
        showGenres()
        # 2. return to menu
        returnToMenu()
        return
    elif answer == "4":
        # 1. how many results
        numberOfResults = howManyResults()
        # 2. get movies from api
        movies = getUpcomingMovies(int(numberOfResults))
        # 3. show upcoming movies
        printPage("A list of upcoming movies:", movies)
        # 4. return to menu
        returnToMenu()
        return
    else:
        return

def displayMenu():
    os.system("cls")
    title = "Hello " + name + "! Nice to meet you! \nWhat would you like to do?"
    options = ["find a movie to watch", "search for movie by title", "see a list of movie genres", "see a list of upcoming movies"]

    printPage(title, options)
    chosenAnswer = askQuestion("Please choose a number: ", len(options))
    os.system("cls")
    print(f"You chose: {options[int(chosenAnswer)-1]}")
    handleAnswer(chosenAnswer)

displayMenu()

