import os
import sys
import requests
import json
from util.yaml_loader import read_yaml


def make_query(url, where_dic):
    """
    To make query string that use like url parameter
    :param url: String
    :param where_dic: Dictionary
    :return: String
    """
    path = url + '&'.join([k + '=' + v for k, v in where_dic.items()])
    print(path)  # Need to remove
    return path


def nvr_api_connect(keyword="A"):
    """
    To connect api (especially Naver Open API)
    :param keyword: String
    :return: json
    """

    file_path = "/".join([arg for arg in ["util", "yam", "api"]])
    connect_info = read_yaml(file_path, "naver_movie_api")

    api_header = {
        "X-Naver-Client-Id": connect_info["client_id"],
        "X-Naver-Client-secret": connect_info["client_secret"]
    }

    api_url = make_query(connect_info["api_url"], {"query": keyword})
    
    response = requests.get(api_url, headers=api_header)
    # print(response.text)
    result = json.loads(response.text)

    """ 고쳐야함!
    if result["total"] > 100:
        if result["start"] == 1:
            None
        elif result["start"] > 1:
            None
    elif result["total"] and result["start"]:
        None
    else:
        None
    """

    if result["items"]:
        return result["items"]
    else:
        return None