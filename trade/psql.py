import psycopg2 as pg

host = "20.247.113.53"
db = "forex"


def save_order(order, list):
    conn = None
    cur = None
    try:
        conn = pg.connect(host=host, dbname=db,
                          user="postgres", password=123, port=5432)
        cur = conn.cursor()
        # insert_script = 'INSERT INTO positions (id) VALUES (%s)'
        # insert_value = 2315
        cur.execute("insert into positions (id,symbol,type,current,tp1,tp2,tp3,sl) values (%s, %s, %s, %s, %s ,%s ,%s ,%s)",
                    (order, list[0], list[1], list[2], list[4], list[6], list[8], list[10]))
        # cur.execute("select * from positions")
        # val = cur.fetchall()
        # for rec in val:
        #     print(type(rec[3]))

        conn.commit()
    except Exception as error:
        print("psql err: ", error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()


def get_all():
    conn = None
    cur = None
    try:
        conn = pg.connect(host=host, dbname=db,
                          user="postgres", password=123, port=5432)
        cur = conn.cursor()
        cur.execute("select * from positions")
        val = cur.fetchall()
        conn.commit()
        return val
    except Exception as error:
        print("psql err: ", error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()


def get(order):
    conn = None
    cur = None
    try:
        conn = pg.connect(host=host, dbname=db,
                          user="postgres", password=123, port=5432)
        cur = conn.cursor()
        cur.execute("SELECT * FROM positions WHERE id = %s", [order])
        val = cur.fetchall()
        conn.commit()
        return val
    except Exception as error:
        print("psql err: ", error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

def create_trail(order):
    print