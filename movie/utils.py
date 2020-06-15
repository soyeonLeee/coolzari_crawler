import os
import pandas as pd
import urllib.parse as urlparse
from urllib.parse import parse_qs


# SET YOUR OWN DIRECTORY
BASE_DIR = 'C:\\Users\\foxgi\\OneDrive\\project\\coolzari_crawler\\data'


def read_excel(excel_file, convert=False):
    """
    To read excel file using numpy and pandas
    :param excel_file: String
    :param convert: boolean
    :return: List
    """
    excel_dir = os.path.join(BASE_DIR, excel_file)
    df = pd.read_excel(excel_dir)

    if convert:
        return df_to_list(df)
    return df


def df_to_list(df):
    """
    To convert Dataframe to list (but only first column)
    :param df: pd.Dataframe
    :return: List
    """
    # df_list = df.values.tolist() [[''], [''], [''] ... ,['']]
    df_list = df.iloc[:, 0].tolist()  # ['', '', ... ,'']
    return df_list


def remove_b_tag(title):
    """
    Remove some tags from title
    :param title: String
    :return: String
    """
    replace_str = title.replace('<b>', '').replace('</b>', '')
    return replace_str


def get_movie_code(url_str):
    """
    Get movie code from url string
    :param url_str: String
    :return: String
    """
    parsed = urlparse.urlparse(url_str)
    return ''.join(urlparse.parse_qs(parsed.query)['code'])


if __name__ == '__main__':
    print(get_movie_code("https://movie.naver.com/movie/bi/mi/basic.nhn?code=189012"))