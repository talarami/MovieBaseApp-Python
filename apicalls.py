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

'''
# get a movie within genre + number of results
conn.request("GET", "/titles?genre=Drama&info=base_info&limit=3", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

# get movie by title + exact title + number of results
conn.request("GET", "/titles/search/title/Lost?exact=true&titleType=movie&limit=3", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

# get movie by title + not exact title + number of results
conn.request("GET", "/titles/search/title/Lost?titleType=movie&limit=3", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
'''
