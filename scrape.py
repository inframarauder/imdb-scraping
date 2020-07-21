from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_movie_links():

    html = urlopen('https://www.imdb.com/chart/top/').read()
    soup = BeautifulSoup(html, 'html.parser')

    rows = soup.find_all(attrs={'class': 'lister-list'})[0].find_all('tr')
    movie_links = []
    for row in rows:
        title_column = row.find(attrs={'class': 'titleColumn'})
        movie = title_column.find('a').get('href', None)
        movie_links.append(movie)

    return movie_links


def get_movie_data(link):
    url = 'https://www.imdb.com'+link
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    data = {}

    data['name'] = soup.find(attrs={'class': 'title_wrapper'}).find(
        'h1').text.split('\xa0')[0]
    data['genres'] = ','.join(list(map(lambda a: a.text, soup.find(
        attrs={'class': 'title_wrapper'}).select('[href*=genres]'))))
    data['year'] = soup.find(attrs={'class': 'title_wrapper'}).find(
        'h1').text.split('\xa0')[1][1:5]
    data['directors'] = ','.join(list(map(lambda a: a.text, soup.find_all(attrs={'class': "credit_summary_item"})[
        0].find_all('a'))))
    data['starring'] = ','.join(list(map(lambda a: a.text, soup.find_all(attrs={'class': 'credit_summary_item'})[
        2].select('[href*=nm]'))))
    data['runtime'] = soup.find(
        attrs={'class': 'title_wrapper'}).find('time').text.strip()
    data['poster'] = soup.find(attrs={'class': 'poster'}).find('img')['src']
    data['plot'] = soup.find(attrs={'class': 'summary_text'}).text.strip()

    return data
