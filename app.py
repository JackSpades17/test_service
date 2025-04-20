from sys import argv
from flask import Flask, render_template
import psycopg2
import subprocess

app = Flask(__name__)
_, pgrsurl = argv

def get_hostname():
    return subprocess.run('hostname',capture_output=True, text=True).stdout

@app.route('/')
def hello_world():
    node = get_hostname()
    return render_template('index.html', node = node)

@app.route('/healthcheck')
def healthcheck():
    return 'OK'

@app.route('/get_url_pg')
def get_url_pg():
    return pgrsurl

# def connect_to_db():
#     conn = psycopg2.connect (
#         #database = "postgres",
#         #user = "test_user",
#         #password = "1111",
#         host = "192.168.49.2",
#         port = "5432"
#     )   
#     return conn

@app.route('/info')
def get_price():
    #with psycopg2.connect('postgresql://admin:1111@postgres-clusterip-test-service:5432/test_zone') as conn:
    with psycopg2.connect(pgrsurl) as conn:
        cur = conn.cursor()
        cur.execute('''select * from info_girl;''')
        sets = cur.fetchone()
    print(sets)

    return f'<h1>Age:{sets[0]}</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=1717)