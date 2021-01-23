import requests
from urllib.parse import urlencode
import json
from pprint import pprint

def url_query(url, query_params):
    query_string = urlencode(query_params)
    url = f"{url}?{query_string}"
    return url

def get_json_from_url(url, my_data={}):
    my_data = bytes(json.dumps(my_data), encoding="utf-8")
    my_headers = { "Content-Type" : "application/json" }
    with requests.request(method="get", url=url, data=my_data, headers=my_headers) as response:
        return response.json()

def post_url(url, my_data):
    my_data = bytes(json.dumps(my_data), encoding="utf-8")
    my_headers = { "Content-Type" : "application/json" }
    print(url)
    with requests.request(method="post", url=url, data=my_data, headers=my_headers) as response:
        print(response.content)
    return response

def return_dictionary_from_args(*args, **kwargs):
    dict_ = {
        **kwargs
    }
    return dict_