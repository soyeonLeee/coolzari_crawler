from util.yaml_loader import load_yaml
import json


def get_db_info(get_str=False, **kwargs):
    file_path = "/".join([arg for arg in kwargs["path"]])
    yam = load_yaml(file_path)  # yaml 파일 path 설정
    yam = json.loads(yam)['global'][kwargs["target"]]

    if get_str:
        return yam
    else:
        return db_connection(yam)


def db_connection(yam):
    if yam["type"] == "mariadb":
        db_uri = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8mb4".format(
            yam['user'],
            yam['password'],
            yam['host'],
            yam['port'],
            yam['db_name']
        )
        return db_uri


if __name__ == '__main__':
    db_info = get_db_info(path=["util", "yam", "db"], target="db_info", get_str=True)
    print(db_info)
    print(get_db_info(path=["util", "yam", "db"], target="db_info"))