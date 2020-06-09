from util.yaml_loader import load_yaml
import json


def yam_test(**kwargs):
    """
    :param kwargs: kwargs
    :return: json
    """
    file_path = "/".join([arg for arg in kwargs["path"]])
    print(file_path)
    yam = load_yaml(file_path)   # yaml 파일 path 설정
    yam = json.loads(yam)['global'][kwargs["target"]]
    return yam


if __name__ == '__main__':
    yam = yam_test(path=["util", "yam", "db"], target="db_info")
    print(yam)