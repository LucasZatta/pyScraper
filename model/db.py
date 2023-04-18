from flask import current_app
from pymongo import MongoClient

def get_db():
    client = MongoClient("mongodb://pyscraper-db-1:27017/")

    db = client["scraped"]
    return db