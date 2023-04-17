from flask import Blueprint, request
from service.scraped import get_url_info as get_url

scrape_route = Blueprint('scrape', __name__)

@scrape_route.route("/scrape", methods=['GET'])
def get_url_info():
    url = request.args.get('url')
    if url is not None:
        return get_url(url)
    else:
        return "Error na url"