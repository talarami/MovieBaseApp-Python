import apicalls
import os


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
    #if answer == "y" return True, if not return False
    return answer == "y"

# showing user a list of genres
def showGenres():
    os.system("cls")
    print("You chose: show genres")
    genres = apicalls.getGenres()
    return printPage("List of genres", genres)

def returnToMenu():
    input("Press enter to return to menu...")
    displayMenu()

def getUpcomingMovies(numberOfResults):
    os.system("cls")
    print("You chose: upcoming movies")
    return apicalls.getUpcomingMovies(numberOfResults)

def getMoviesWithinGenre(chosenGenre, numberOfResults):
    os.system("cls")
    print(" ")
    return apicalls.getMoviesWithinGenre(chosenGenre)[slice(int(numberOfResults))]

def getMovieByTitle(title, exact, numberOfResults):
    os.system("cls")
    print(" ")
    return apicalls.getMovieByTitle(title, exact, numberOfResults)

# Application logic
def handleAnswer(answer):
    if answer ==  "1":
        # 1.get genres from API
        genres = apicalls.getGenres()
        # 2. choose genre
        genreIndex = chooseGenre(genres)
        genre = genres[int(genreIndex) - 1]
        print("You chose " + genre)
        # 3. how many results
        numberOfResults = howManyResults()
        print("You chose " + numberOfResults + "results.")
        # 4. call to api to get x results within this genre
        result = getMoviesWithinGenre(genre, numberOfResults)
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
        result = getMovieByTitle(title, exact, numberOfResults)
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
        movies = getUpcomingMovies(numberOfResults)
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




