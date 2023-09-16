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


# 5) searching for movies by title + limit of titles per page:

# conn.request("GET", "/titles/search/title/Lost?exact=true&limit=1", headers=headers) 


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

whatToDo = {
    "1": "find a movie to watch", 
    "2": "see a list of movie genres", 
    "3": "see a list of upcoming movies"}

for c, desc in whatToDo.items():
    print(f"{c}. {desc}")

choice = input("Please choose a number: ")

while choice not in whatToDo:
    choice = input(f"Choose one of: {', '.join(whatToDo)}: ")

print(f"You chose: {whatToDo[choice]}")

user_input = " "
input_message = "Choose an option: \n"



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