from Config.Database import database
from Models.Collection import *


class CollectionController:

    con = None
    collection = None

    def __init__(self):
        self.con = database()
        if self.con is not None:
            self.collection = Collection(self.con)

    def create_collection(self, name, description, language, category) -> bool:
        return self.collection.create_collection(name, description, language, category)

