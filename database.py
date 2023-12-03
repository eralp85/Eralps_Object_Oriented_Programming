class DataBase:

    def __init__(self, a: int = 99, b: int = 26, databaseer: str = 'Eralp'):
        self.a = a
        self.b = b
        self.databaseer = databaseer

    def database(self, database_name):
        self.databaseer = database_name
        return self.databaseer

    def sevval(self, eralp: str = "Karicim"):
        self.eralp = eralp
        return self.eralp


sevval22 = DataBase(10, 20, 'Sevval23')
print(sevval22.sevval())


def sevval():
    print("Karimin adi Sevval Pamuklar Unver")


class Query:
    def __init__(self, query: str):
        self.query = query

    def query_item(self):
        return "Query item is: " + self.query
