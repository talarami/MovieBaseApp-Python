import requests

URL = "https://moviesdatabase.p.rapidapi.com/titles/series/%7BseriesId%7D"

headers = {
	"X-RapidAPI-Key": "1762556fbcmsh9ec8fd6d574b37cp1c1d46jsn676ebe2791e6",
	"X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
}

response = requests.get(URL, headers=headers)

print(response.json())


# ok

import http.client

conn = http.client.HTTPSConnection("moviesdatabase.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "1762556fbcmsh9ec8fd6d574b37cp1c1d46jsn676ebe2791e6",
    'X-RapidAPI-Host': "moviesdatabase.p.rapidapi.com"
}



# ok

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

print("Welcome to Movie Base!")
name = input("What's your name?")
print("Hello " + name + ("! Nice to meet you! \nWhat would you like to do?"))


# asking user what he wants to do:

whatToDo = {
    "1": "find a movie to watch", 
    "2": "search for movie by title",
    "3": "see a list of movie genres", 
    "4": "see a list of upcoming movies"}

for c, desc in whatToDo.items():
    print(f"{c}. {desc}")

choice = input("Please choose a number: ")

user_input = " "


while choice not in whatToDo:
    choice = input(f"Choose one of: {', '.join(whatToDo)}: ")

print(f"You chose: {whatToDo[choice]}")


# asking user how many page results he wants to get (option 1, 2, 4):

option = input("How many search results per page do you want to get? Please choose a number from 1 to 10: ") 

limitNumber = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "10": "10"
}


user_input = " "

while option not in limitNumber:
    option = input(f"You need to choose a number from: {', '.join(limitNumber)}: ")

print(f"You chose: {limitNumber[option]} search results per page")

# asking user for movie title

movieTitle = input("Please enter movie title: ")
print(f"Entered movie title: " + movieTitle)

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

searchExactMovieTitle()

"""
if choice[user_input] == 1:
    print("wybrales jeden")
"""

"""
if choice == 1:
    print("wybrales jeden")
"""

"""
if whatToDo[choice] == 1:
    print("wybrales opcje jeden")
"""
    
"""
if user_input == 2 in whatToDo[choice]:
    print("wybrales opcje dwa")
"""
"""
if 2 == 2:
    print("dwa rowna sie dwa")
"""
"""
for choice in whatToDo[choice]:
    if choice == 1:
        print("you chose option one")
"""


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