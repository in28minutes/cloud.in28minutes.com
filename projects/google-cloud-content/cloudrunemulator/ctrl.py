from db import get_conn


def get_total():
    return len(get_all())


def get_all():
    cursor = get_conn().cursor()
    sql = 'SELECT id, item, status FROM todos'
    cursor.execute(sql)
    return cursor.fetchall()


def get_by_id(key):
    cursor = get_conn().cursor()
    sql = 'SELECT id, item, status FROM todos WHERE id=?'
    cursor.execute(sql, [key])
    return cursor.fetchone()


def save(item, status):
    db = get_conn()
    cursor = db.cursor()
    sql = 'INSERT into todos (item, status) VALUES (?, ?)'
    cursor.execute(sql, [item, status])
    db.commit()
    return True

# update and delete - To be implemented...
