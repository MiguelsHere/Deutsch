from mysql import connector

class Collection:

    con = None
    cursor = None

    def __init__(self):
        try:
            self.con = connector.connect(user='root', password='', host='localhost', database='language_helper')
            self.cursor = self.con.cursor(prepared=True)
        except Exception as e:
            print(e)

    def fetch_all_collections(self):
        try:
            stmt = "SELECT collection_id, collection_name, language, category FROM collection"

            self.cursor.execute(stmt)
            cont = self.cursor.fetchall()
        except Exception as e:
            print(e)
            return None
        return cont
    
    def create_collection(self, name, language, category) -> bool:
        try:
            stmt = ("INSERT INTO collection(collection_name,language,category)"
                    " VALUES (%s,%s,%s)")

            self.cursor.execute(stmt, (name, language, category))
            self.con.commit()
        except Exception as e:
            print(e)
            return False
        return True
    
    def delete_collection(self, collection_id: int) -> bool:
        try:
            stmt = "DELETE FROM collection WHERE collection_id = $s"

            self.cursor.execute(stmt, collection_id)
        except Exception as e:
            print(e)
            return False
        return True



    def add_vocab(self, word: str, translation: str, collection_id: int) -> bool:
        try:
            stmt = ("INSERT INTO word(word,translation)"
                    " VALUES (%s,%s) WHERE collection_id = %s")

            self.cursor.execute(stmt, (word, translation, collection_id))
        except Exception as e:
            print(e)
            return False
        return True

    def fetch_collection(self, collection_id: int):
        try:
            stmt = ("SELECT collection_name, collection_description, language, category FROM collection"
                    " WHERE collection_id = %s")

            cont = self.cursor.execute(stmt, collection_id)
        except Exception as e:
            print(e)
            return None
        return cont
