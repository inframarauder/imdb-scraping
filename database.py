from pymongo import MongoClient
from dotenv import load_dotenv
import scrape
import os


# load env variables:
load_dotenv()

# function to save to DB


def save_to_db():

    db_uri = os.getenv('MONGO_CONN_STRING')
    db = create_connection(db_uri)  # connect to mongodb
    cleanup_db(db)  # initial cleanup

    # get scraped links to follow for each movie
    movie_links = scrape.get_movie_links()

    # get scraped data and write to DB
    print('Extracting movie info...')
    X = 10  # change to desired value
    count = 0
    for link in movie_links:
        count += 1
        if count > X:
            break
        data = scrape.get_movie_data(link)
        data['rating'] = 0
        data['reviews'] = []
        db.movies.insert_one(data)
        print(str(count)+'.'+data['name'] + ' written to DB')

    print('Complete!')


def create_connection(db_uri):
    try:
        client = MongoClient(db_uri)
        db = client['pmdb']
        print("Database Connected!")
    except Exception as e:
        print('Error in MongoDB connection!')
        print(e)
        exit()
    finally:
        return db or None


def cleanup_db(db):
    try:
        if len(list(db.movies.find())) > 0:
            db.movies.delete_many({})
            print('Cleanup Successful!')
    except Exception as e:
        print("Error in DB cleanup!")
        print(e)
        exit()
