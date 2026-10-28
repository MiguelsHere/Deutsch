from mysql import connector


def database():
    try:
        con = connector.connect(user='root', password='', host='localhost', database='language_helper')
        return con
    except Exception as e:
        print(e)
        return None
