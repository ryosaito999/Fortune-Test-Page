import MySQLdb
import fortune_cookie

db = MySQLdb.connect("fortunedb-1.caugrehho37h.us-west-2.rds.amazonaws.com","admin","sfamily2r","fortune_db" )
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS FORTUNE_TABLE")

create_table_string = """CREATE TABLE IF NOT EXISTS FORTUNE_TABLE (
    fortune_id int(5) NOT NULL AUTO_INCREMENT,
    fortune_text text DEFAULT NULL,
    PRIMARY KEY(fortune_id)
); """
cursor.execute(create_table_string)

for i in range(20):
    insert_fortune_string = """ INSERT INTO FORTUNE_TABLE (fortune_text)
    VALUES ('%s'); """ % (fortune_cookie.fortune().strip().replace('\'', '\\\''))
    cursor.execute(insert_fortune_string)

db.commit()
db.close()


