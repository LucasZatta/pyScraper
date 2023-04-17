# import pymongo  # package for working with MongoDB
# client = pymongo.MongoClient("mongodb://localhost:27017/")
# db = client["customersdb"]
# customers = db["test"]

# print(customers.name)

from flask import Flask
from api.routes import scrape_route

app = Flask(__name__)
app.register_blueprint(scrape_route)


if __name__ == "__main__":
    app.run(port=3300)

