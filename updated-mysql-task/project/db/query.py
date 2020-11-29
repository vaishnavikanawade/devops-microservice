import db.db_connection as connection


def query_adduser(id, name, age, department, subject):
    try:
        mysql = connection.connect_db()
        cur = mysql.cursor()
        query = "INSERT INTO user(id, name, age, department, subject) VALUES(%s, %s, %s, %s,%s)"
        values = (id, name, age, department, subject)
        cur.execute(query, values)
        mysql.commit()
        mysql.disconnect()
        return 200
    except Exception as e:
        return 500

def query_deleteuser(id):
    try:
        mysql = connection.connect_db()
        cur = mysql.cursor()
        query = "DELETE FROM user where id = %s"
        cur.execute(query, (id,))
        mysql.commit()
        mysql.disconnect()
        return 200
    except Exception as e:
        return 500

def query_showuser():
    try:
        mysql = connection.connect_db()
        cur = mysql.cursor()
        cur.execute("SELECT * FROM user")
        userDetails = cur.fetchall()
        return userDetails
    except Exception as e:
        return 500