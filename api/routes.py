from collections import namedtuple
from flask import Blueprint, request, jsonify
from service.scraped import get_url_info as get_url
import re

scrape_route = Blueprint('scrape', __name__)

@scrape_route.route("/scrape", methods=['GET'])
def get_url_info():
    pattern = re.compile(r"[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)")
    url = request.args.get('url')
    if url is not None:
        if re.fullmatch(pattern,url):
            return namedtuple('Response', ('response', 'status_code'))(get_url(url), 200)
        else:
            return namedtuple('Response', ('error_msg', 'status_code'))("invalid url match", 400)
    else:
        return namedtuple('Response', ('error_msg', 'status_code'))("invalid url match", 400)