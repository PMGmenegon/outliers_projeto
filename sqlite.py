import sqlite3

def run_sql(sql: str):
    with sqlite3.connect("news.db") as con:

        cur = con.cursor()

        res = cur.execute(sql)
        
        data = res.fetchall()
        
        con.commit()

    return data

def create_table():
    return run_sql(f'''
        CREATE TABLE IF NOT EXISTS news(
            id INTEGER PRIMARY KEY,
            date INT NOT NULL,
            body TEXT NOT NULL
        )
    ''')

def select_all():
    return run_sql(f'''
        SELECT *
        FROM news
    ''')

def select_news(**kwargs):
    key, value = list(kwargs.items())[0]
    return run_sql(f'''
        SELECT body
        FROM news
        WHERE {key} = {value}
        ORDER BY id
        LIMIT 7
    ''')

def insert_news(date, body):
    return run_sql(f'''
        INSERT INTO news(date, body)
        VALUES({date}, '{body}')
    ''')

def update_news(id, date, body):
    return run_sql(f'''
        UPDATE news
        SET date = {date}, body = '{body}'
        WHERE id = {id}
    ''')

def delete_news(id):
    return run_sql(f'''
        DELETE FROM news
        WHERE id = {id}
    ''')
