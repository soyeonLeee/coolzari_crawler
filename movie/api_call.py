import os
import sys
import requests
from util.yaml_loader import read_yaml


def nvr_api_connect(path=None, target=None):
    """
    To connect api (especially Naver Open API)
    :param path: List
    :param target: String
    :return: json
    """
    file_path = "/".join([arg for arg in path])
    connect_info = read_yaml(file_path, target)

    api_header = {
        "X-Naver-Client-Id": connect_info["client_id"],
        "X-Naver-Client-secret": connect_info["client_secret"]
    }

    response = requests.get(connect_info["api_url"] + "?query=기생충", headers=api_header)
    print(response.text)
    print(response.url)



if __name__ == '__main__':
    nvr_api_connect(path=["util", "yam", "api"], target="naver_movie_api")