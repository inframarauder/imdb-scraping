from pymongo import MongoClient
import scrape

# create mongodb connection:
client = MongoClient(
    'mongodb+srv://dbadmin:I7hWIWrLDrq18JqZ@pmdb-cluster.txef4.mongodb.net/')
db = client['pmdb']

if len(list(db.movies.find())) > 0:
    db.movies.delete_many({})

movie_links = scrape.get_movie_links()


print('Scraping movie info:')
count = 0
for link in movie_links:
    if count > 2:
        break
    count += 1
    data = scrape.get_movie_data(link)
    db.movies.insert_one(data)
    print(str(count)+'.'+data['name'])
