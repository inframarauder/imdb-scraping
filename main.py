import scrape
import json

movie_links = scrape.get_movie_links()
movie_data_list = []

print('Scraping movie info:')
for link in movie_links:
    data = scrape.get_movie_data(link)
    movie_data_list.append(data)
    print(data['name'])

print(json.dumps(movie_data_list))
