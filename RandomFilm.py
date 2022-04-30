import random
from urllib.request import urlopen
from bs4 import BeautifulSoup


def getScript(movie_script_link):
    url = movie_script_link
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("ISO-8859-1")
    soup = BeautifulSoup(html, features="html.parser")
    for data in soup(['b']):
        data.decompose()
    return ' '.join(soup.stripped_strings)


def getUrl(choice):
    movie_name_for_url = ""
    movie_name_list = choice.split(" ")
    if len(movie_name_list) == 1:
        return movie_name_list[0]
    else:
        for i in movie_name_list:
            if i == movie_name_list[len(movie_name_list)-1]:
                movie_name_for_url += i
                return movie_name_for_url
            else:
                movie_name_for_url += i + "-"

def getFilms():
    url = 'https://imsdb.com/all-scripts.html'
    page = urlopen(url)
    list_of_films = []
    html_bytes = page.read()
    html = html_bytes.decode("ISO-8859-1")
    soup = BeautifulSoup(html, features="html.parser")
    titles = soup.find_all('a')
    for tag in titles:
        u = tag.text.strip()
        list_of_films.append(u)
    del list_of_films[:61]
    del list_of_films[1211:]
    return list_of_films

def getRandomFilm():
    u = getFilms()
    random_int = random.randint(0, len(u))
    return u[random_int]
