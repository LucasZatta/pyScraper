from flask import Flask
from api.routes import scrape_route

app = Flask(__name__)
app.register_blueprint(scrape_route)


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')

