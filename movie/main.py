from movie.api_call import nvr_api_connect
from movie.utils import read_excel
from movie.db_movie import insert_movie_rmk

if __name__ == '__main__':

    keywords = read_excel("movieList.xlsx", convert=True)
    for keyword in keywords:
        data_list = nvr_api_connect(keyword=str(keyword))
        if data_list:
            for data in data_list:
                print(data)
                insert_movie_rmk(data)
    """
    data_list = nvr_api_connect(keyword="harry")
    if data_list:
        for data in data_list:
            print(data)
            insert_movie_rmk(data)
    """