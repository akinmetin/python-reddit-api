'''
This module includes required functions for Flask API
'''
import logging
import requests

logging.basicConfig(format='%(asctime)s - [%(levelname)s] %(funcName)s - %(message)s',
                    level='DEBUG')
LOGGER = logging.getLogger(__name__)


def url_validator(url: str) -> bool:
    '''
    low level URL verification function
    takes string type URL as input
    could be improved with regex
    returns boolean result of verification
    '''
    if "https://www.reddit.com" not in url:
        return False
    return True


def get_reddit_data(url: str) -> dict:
    '''
    takes string type URL as input
    sends GET request to provided URL
    returns json type retrieved data
    '''
    # request header to disable default API rate limit
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/92.0.4515.115 Safari/537.36'
            }

    # sending get request and saving the response as response object
    req = requests.get(url=url, headers=headers)

    # extracting data in json format
    data = req.json()
    return data


def find_top_five_post_titles(data: dict) -> list:
    '''
    takes dictonary type input
    returns the top 5 post name and score value pairs
    '''
    filtered_json = {}

    # add only title and score value pairs into a clean dict
    for elem in data["data"]["children"]:
        filtered_json[elem["data"]["title"]] = elem["data"]["score"]

    # sort filtered title and score pairs in descending order
    result = dict(sorted(filtered_json.items(), key=lambda item: item[1],
                         reverse=True))

    # log the top 5 title and score pairs
    LOGGER.info("Processed top 5 post title and score pairs: "
                + str(list(result.items())[:5])[1:-1])

    # return the top 5 titles
    return list(result.keys())[:5]
