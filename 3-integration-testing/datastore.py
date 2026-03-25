database = {}


def store_value(key, value):
    #raise NotImplementedError("Implement store_value using TDD")
    database[key] = value

def get_value(key):
    #raise NotImplementedError("Implement get_value using TDD")
    if key in database:
        return database[key]
    else:
        return None


def delete_value(key):
    #raise NotImplementedError("Implement delete_value using TDD")
    if key in database:
        del database[key]


def list_keys():
    #raise NotImplementedError("Implement list_keys using TDD")
    return database.keys()
