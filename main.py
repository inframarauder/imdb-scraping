import scrape

movie_links = scrape.get_movie_links()

for link in movie_links:
    data = scrape.get_movie_data(link)
    print(data)
