import requests
from urllib.parse import urlencode
import json
from pprint import pprint

""" Mini library to deal with http requests.
"""

def get_json_from_url(url, my_data={}):
    """ Gets the json response of getting the url

    """
    my_data = bytes(json.dumps(my_data), encoding="utf-8")
    my_headers = { "Content-Type" : "application/json" }
    with requests.request(method="get", url=url, data=my_data, headers=my_headers) as response:
        return response.json()

def post_url(url, my_data):
    my_data = bytes(json.dumps(my_data), encoding="utf-8")
    my_headers = { "Content-Type" : "application/json" }
    with requests.request(method="post", url=url, data=my_data, headers=my_headers) as response:
        return response

def return_dictionary_from_args(*args, **kwargs):
    """Returns a dictionary with all the parameters
    Returns:
        dict
    """
    dict_ = {
        **kwargs
    }
    return dict_