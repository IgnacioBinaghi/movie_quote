from urllib.request import urlopen
from bs4 import BeautifulSoup
from RandomFilm import *


while True:
    availability = input('Hello... To start off, if you would like to see our available movies? (y)es or any other key for no: ')
    if availability == "y":
        u = getFilms()
        count = 0
        for i in range(len(u)):
            count += 1
            print(u[i],",", end="")
            if count == 5:
                print()
                count = 0
    elif availability == "n":
        print("Got it...")
    print()
    choice_0 = input('please choose a movie or type "random" for a random movie: ')
    if choice_0 == "random":
        choice = getRandomFilm()
        print("Your movie is "+choice)
    else:
        u = getFilms()
        choice_1 = choice_0.title()
        if choice_1 in u:
            choice = choice_1
            print("Your movie is "+choice)
        else:
            print("Movie isn't in our list... we'll assign you a random movie")
            choice = getRandomFilm()
            print("Your movie is "+choice)
    choice = choice.replace(",","")
    choice = choice.replace(":","")
    movie_choice = getUrl(choice)
    scriptUrl = 'https://imsdb.com/scripts/' + movie_choice + '.html'
    c = getScript(scriptUrl)
    print("\n")
    print("Soon you will enter any word and I will let you know whether or not it is in the script")
    print('')
    while True:
        script = c.split(" ")
        case_sensitivity = input("Would you like it to be case sensitive? (y)es or (n)o: ")
        if case_sensitivity == "y" or case_sensitivity == "Y":
            word_choice = input("Enter word or enter 'stop' to exit... it can be more than one and will be searched for individually: ")
            if word_choice == "stop" or word_choice == "Stop":
                break
            else:
                try:
                    word_choice_list = word_choice.split(" ")
                    word_counter = 0
                    for i in script:
                        if i in word_choice_list:
                            word_counter += 1
                            word_placement = script.index(i)
                    break
                except:
                    print("You must put a space between your words")
        elif case_sensitivity == "n" or case_sensitivity == "N":
            word_choice = input("Enter word or enter 'stop' to exit... it can be more than one and will be searched for individually: ")
            if word_choice == "stop" or word_choice == "Stop":
                break
            else:
                try:
                    capitalized_words = []
                    fully_capitalized_words = []
                    lowercase_words = []
                    word_placement = []
                    word_choice_list = word_choice.split(" ")
                    word_counter = 0


                    for u in word_choice_list:
                        lowercase_words.append(u.lower())
                    for i in script:
                        if i in lowercase_words:
                            word_counter += 1
                            word_placement.append(script.index(i))

                    for u in word_choice_list:
                        capitalized_words.append(u.capitalize())
                    for i in script:
                        if i in capitalized_words:
                            word_counter += 1
                            word_placement.append(script.index(i))

                    for u in word_choice_list:
                        fully_capitalized_words.append(u.upper())
                    for i in script:
                        if i in fully_capitalized_words:
                            word_counter += 1
                            word_placement.append(script.index(i))
                    break
                except:
                    print("You must put a space between your words")
    print()
    print("Your chosen word/words are used: "+str(word_counter)+" times")
    print()
    continue_q = input("Would you like to continue? (y)es or (n)o: ")
    if continue_q == "n":
        print()
        print("Goodbye!")
        break
    elif continue_q == "y":
        print("Okay... here we go again")
        print()
