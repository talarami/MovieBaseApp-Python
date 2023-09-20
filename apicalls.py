import requests
import apikey
import constants

headers = {
	"X-RapidAPI-Key": apikey.APIKEY,
    "Content-type": "application/json"
} 

def getGenres():
    response = requests.get(constants.BASEURL + "/titles/utils/genres", headers=headers)
    dict = response.json()
    list = dict.get("results")
    #Remove 'None' type which is on position 0
    del list[0]
    return list

def getUpcomingMovies(numberOfResults):
    response = requests.get(constants.BASEURL + "/titles/x/upcoming?limit=" + numberOfResults, headers=headers)
    dict = response.json()
    list = dict.get("results")
    results = []
    for result in list:
        title = result["titleText"]["text"]
        releaseDate = result["releaseDate"]
        day = releaseDate["day"]
        month = releaseDate["month"]
        year = releaseDate["year"]
        results.append(title + " " + str(day) + "/" + str(month) + "/" + str(year))
    return results

def getMoviesWithinGenre(chosenGenre):
    response = requests.get(constants.BASEURL + "/titles?genre=" + chosenGenre + "&info=base_info&limit=10", headers=headers)
    dict = response.json()
    list = dict.get("results")
    results = []
    for result in list:
        title = result["titleText"]["text"]
        releaseYear = result["releaseYear"]["year"]
        results.append(title + " " + str(releaseYear))
    return results


def getMovieByTitle(title, exact, numberOfResults):
    exactPart = ""  
    if exact == True:
        exactPart = "exact=true&"
    response = requests.get(constants.BASEURL + "/titles/search/title/" + title + "?" + exactPart + "titleType=movie&info=base_info&limit=" + numberOfResults, headers=headers)
    dict = response.json()
    list = dict.get("results")
    results = []
    for result in list:
        print(result)
        title = result["titleText"]["text"]
        releaseYear = result["releaseYear"]["year"]
        results.append(title + " " + str(releaseYear))
    return results