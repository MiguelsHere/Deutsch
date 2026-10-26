class Collection:

    def create_collection(name) -> bool:
        try:
            with open(f"Collections/{name}.csv","x",encoding="utf-8") as f:
                pass
        except Exception as e:
            print(e)
            return False

        return True

    def add_vocab(name:str ,word_translation:dict) -> bool:
        try:
            with open(f"Collections/{name}.csv","a",encoding="utf-8") as f:
                for word, trans in word_translation.items():
                    f.write(f"{word};{trans}\n")
                    
        except Exception as e:
            print(e)
            return False
        
        return True
    
    def fetch_collection(name:str) -> dict:
        try:
            with open(f"Collections/{name}.csv","r",encoding="utf-8") as f:
                lines = f.read().split("\n")
                dici = {}
                for x in lines:
                    if x:
                        cont = x.split(";")
                        dici[cont[0]] = cont[1]
        except Exception as e:
            print(e)
            return {}
        
        return dici 

    def delete_collection(name:str) -> bool:
        pass
    