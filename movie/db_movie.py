import logging
import pymysql
import pymysql.cursors
from datetime import datetime
from util.db_connect import get_db_info
from movie.utils import remove_b_tag, get_movie_code

"""
self._connect=pymysql.connect(host=self.mysql.ip,port=self.mysql.port,
                             user=self.mysql.user，password=str(self.mysql.password),
                             db=self.mysql.database)
"""

# MYSQL Connection
db = get_db_info(path=["util", "yam", "db"], target="db_info", get_str=True)
print(db)
MOVIE_CONNECTION = pymysql.connect(host=db['host'], user=db['user'], password=str(db['password']),
                                   db=db['db_name'], charset='utf8mb4')

logger = logging.getLogger('movie')


def insert_movie_rmk(data):
    try:
        with MOVIE_CONNECTION.cursor() as cursor:
            sql = 'INSERT INTO movie (movie_cd, movie_title, movie_subtitle, movie_link, movie_image, movie_pubdate, ' \
                  'movie_director) VALUES (%s, %s, %s, %s, %s, %s, %s)' \
                  'ON DUPLICATE KEY UPDATE movie_cd=%s, movie_title=%s, movie_subtitle=%s'
            code = get_movie_code(data['link'])
            title = remove_b_tag(data['title'])
            cursor.execute(sql, (code, title, data['subtitle'], data['link'], data['image'],
                                 data['pubDate'], data['director'], code, title, data['subtitle']))
            MOVIE_CONNECTION.commit()
    except Exception as e:
        with open('./error/DB_ERROR_{}.txt'.format(datetime.today().strftime('%Y%m%d')), mode='a',
                  encoding='utf8') as f:
            f.write('[INSERT MOVIE] {} / {} \n --> {}\r\n'.format(data['title'], code, e))
        logger.warning('[EXCEPTION] {}'.format(e))