
class Collection:

    cursor = None

    def __init__(self, con):
        self.cursor = con.cursor(prepared=True)

    def create_collection(self, name, description, language, category) -> bool:
        try:
            stmt = ("INSERT INTO collection(collection_name,collection_description,language,category)"
                    " VALUES (%s,%s,%s,%s)")

            self.cursor.execute(stmt, (name, description, language, category))
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

    def fetch_all_collections(self):
        try:
            stmt = "SELECT collection_name, collection_description, language, category FROM collection"

            cont = self.cursor.execute(stmt)
        except Exception as e:
            print(e)
            return None
        return cont

    def delete_collection(self, collection_id: int) -> bool:
        try:
            stmt = "DELETE FROM collection WHERE collection_id = $s"

            self.cursor.execute(stmt, collection_id)
        except Exception as e:
            print(e)
            return False
        return True
