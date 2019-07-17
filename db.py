import MySQLdb

class db:
    def __init__(self,score,review):
        self.score = score
        self.review = review

    def db_conn(self):
        return MySQLdb.connect(
        user = "root",
        passwd = "",
        host = "localhost",
        db = "flask"
        )

    def db_table_create(self):
        conn = self.db_conn()
        cur = conn.cursor()

        sql = 'create table Sentence (score float, content varchar(10000))'
        cur.execute(sql)

        cur.close()
        conn.close()

    def db_table_insert(self,score,review):
        conn = self.db_conn()
        cur = conn.cursor()

        sql = 'insert into Sentence values (%s, %s)'
        cur.execute(sql,(self.score,self.review))
        conn.commit()

        cur.close()
        conn.close()