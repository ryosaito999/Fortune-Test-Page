from flask import Flask, render_template, request, url_for, flash, redirect
from flaskext.mysql import MySQL
import random
import fortune_cookie

app = Flask(__name__, instance_relative_config=True)
mysql = MySQL()

app.config.from_object('config')
app.config['MYSQL_DATABASE_DB'] = 'fortune_db'
mysql.init_app(app)

@app.route('/')
def index():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM FORTUNE_TABLE')
    fortune_list = cursor.fetchall()
    conn.close()
    return render_template('index.html', fortune_list=fortune_list)

@app.route('/submit_fortune', methods=['POST'])
def submit_fortune():

    insert_fortune_string = "INSERT INTO FORTUNE_TABLE (fortune_text) VALUES ('%s');" % (request.form['fortune_entry'].strip())
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(insert_fortune_string)
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':

    #Setup debug table for now- Remove when placing app in production
    conn = mysql.connect()
    cursor = conn.cursor()

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

    conn.commit()
    conn.close()
    app.run(debug=True)

