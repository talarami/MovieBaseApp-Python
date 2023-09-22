file1 = open("myfile.txt", "w")
line1 = ["Welcome to Movie Base! \n", "What's your name? \n"]
line2 = "Anna \n"
line3 = ["Hello Anna! Nice to meet you! \n", "What would you like to do? \n", "1. find a movie to watch \n",
"2. search for movie by title \n", "3. see a list of movie genres \n", "4. see a list of upcoming movies \n", "Please choose a number: \n"]
line4 = ["2 \n"]
line5 = ["Please enter movie title: \n"]
line6 = ["Titanic \n"]
line7 = ["Is that an exact movie title? (Y/N) \n"]
line8 = ["y \n"]
line9 = ["How many search results do you want to get? Please choose a number 1 to 10: \n"]
line10 =["5 \n"]
line11 = ["List of movies: \n", "1. Titanic 2023 \n", "2. Titanic 2018 \n", "3. Titanic 2016 \n", "4. Titanic 2012 \n", "5. Titanic 1997 \n", "Press enter to return to menu... \n"]


file1.writelines(line1), file1.writelines(line2), file1.writelines(line3), file1.writelines(line4), file1.writelines(line5), file1.writelines(line6), file1.writelines(line7), file1.writelines(line8), file1.writelines(line9), file1.writelines(line10), file1.writelines(line11)


file1.close()

file1 = open("myfile.txt", "r")
print(file1.read())
file1.close()


