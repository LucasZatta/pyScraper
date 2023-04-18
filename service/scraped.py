import datetime
import json
from bson import json_util
import dateutil.parser

import pymongo
from model.db import get_db
from utils.scrape import scrape_url

def get_url_info(url):
    date = datetime.datetime.now() 
    
    db = get_db()

    scraped_data_collection = db["scraped"]

    doc = scraped_data_collection.find_one({"url":url})
    


    if doc is not None and (date - dateutil.parser.isoparse(doc['created_at'])).total_seconds()/3600 < 1:
        doc = json.loads(json_util.dumps(doc))
        del doc["_id"]
        del doc['created_at']
        return doc
         
    else:
        scraped_data = scrape_url(url)
        scraped_data['created_at']=date.isoformat()
        formated_data = json.loads(json_util.dumps(scraped_data))
        scraped_data_collection.insert_one(formated_data)
        del scraped_data['created_at']
        return scraped_data    
        