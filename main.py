# scrape top X movies from IMDB and write the data to MongoDB.
# X can be atmost 250 (as per IMDB)

from pymongo import MongoClient
from dotenv import load_dotenv
import scrape
import os

# load env variables:
load_dotenv()

# create mongodb connection:
db_uri = os.getenv('MONGO_CONN_STRING')
client = MongoClient(db_uri)
db = client['pmdb']

if len(list(db.movies.find())) > 0:
    db.movies.delete_many({})

movie_links = scrape.get_movie_links()


print('Scraping movie info:')
X = 10
count = 0
for link in movie_links:
    count += 1
    if count > X:
        break
    data = scrape.get_movie_data(link)
    db.movies.insert_one(data)
    print(str(count)+'.'+data['name'] + ' written to DB')
