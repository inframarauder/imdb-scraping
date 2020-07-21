import scrape
import json

movie_links = scrape.get_movie_links()
movie_data_list = []

print('Scraping movie info:')
count = 0
for link in movie_links:
    count += 1
    data = scrape.get_movie_data(link)
    movie_data_list.append(data)
    print(str(count)+'.'+data['name'])

print(json.dumps(movie_data_list))
