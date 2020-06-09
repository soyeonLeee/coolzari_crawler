import os, json, yaml
from io import IOBase


def open_file(file):
    path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
    file_path = os.path.join(path, "{}.yml".format(file))
    return open(file_path, encoding='utf-8')


def load_yaml(config):
    """
    Only load yaml file. To Read, use read_yaml function
    :param config:
    :return:
    """
    if isinstance(config, dict):
        config = json.dumps(config)
    elif isinstance(config, IOBase):
        config = "".join(config.readlines())
    config = yaml.load(open_file(config), Loader=yaml.FullLoader)

    return json.dumps(config)


def read_yaml(file_path, target):
    """
    To read yaml file and get string from yaml file
    :param file_path: String
    :param target: String
    :return:
    """
    yam = load_yaml(file_path)  # yaml 파일 path 설정
    yam = json.loads(yam)['global'][target]
    return yam
