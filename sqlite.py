import sqlite3

def run_sql(sql: str, values = ()):
    with sqlite3.connect("news.db") as con:

        cur = con.cursor()

        res = cur.execute(sql, values)
        
        data = res.fetchall()
        
        con.commit()

    return data

def create_table():
    return run_sql(f'''
        CREATE TABLE IF NOT EXISTS news(
            link TEXT PRIMARY KEY,
            date INT NOT NULL,
            title TEXT NOT NULL,
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
        SELECT *
        FROM news
        WHERE {key} = ?     
        ORDER BY date
    ''',
    (value,))

def insert_news(link, date, title, body):
    return run_sql(f'''
        INSERT OR IGNORE INTO news(link, date, title, body)
        VALUES(?, ?, ?, ?)
    ''',
    (link, date, title, body))

def update_news(link, date, title, body):
    return run_sql(f'''
        UPDATE news
        SET date = ?, title = ?, body = ?
        WHERE link = ?
    ''',
    (date, title, body, link))

def delete_news(**kwargs):
    key, value = list(kwargs.items())[0]
    return run_sql(f'''
        DELETE FROM news
        WHERE {key} = ?
    ''',
    (value,))
