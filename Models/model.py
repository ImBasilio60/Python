from mysql.connector import connect


class Model(object):
    con = None
    cur = None

    def open(self):
        __class__.con = connect(
            host='localhost',
            user='root',
            password='',
            database='tourisme',
        )

        __class__.cur = __class__.con.cursor(dictionary=True)


    def close(self):
        if None != __class__.cur:


