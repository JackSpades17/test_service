from flask import Flask
import psycopg2
import argv

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, Nastya is a LOVA GIRL!!!</h1>'

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
    with psycopg2.connect(host = "127.0.0.1", port = "5432", user="admin", database="test_zone") as conn:
        cur = conn.cursor()
        cur.execute('''select * from info_girl;''')
        sets = cur.fetchone()
    print(sets)

    return f'<h1>Age:{sets[0]}</h1>'

# @app.route('/update')
# def update_price():
#     cur.execute('''select * from count_update order by count desc;''')
#     sets = cur.fetchone()
#     new_item = int(sets[0]) + 1
#     cur.execute(f'''insert into count_update values('{new_item}');''')
#     con.commit()
#     cur.execute('''select * from count_update order by count desc;''')
#     sets = cur.fetchone()
#     return f'<h1>Congratulations!Обновлено! BIG is {sets[0]}!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=1717)