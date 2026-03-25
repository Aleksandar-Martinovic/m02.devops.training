import datastore

def process_and_store(key, raw_value):
    #raise NotImplementedError("Implement process_and_store using TDD")
    stored_value = raw_value.strip().upper()
    datastore.store_value(key, stored_value)
    return stored_value


def retrieve_processed(key):
    #raise NotImplementedError("Implement retrieve_processed using TDD")
    return datastore.get_value(key).lower() if datastore.get_value(key) is not None else None


def update_value(key, raw_value):
    #raise NotImplementedError("Implement update_value using TDD")
    if datastore.get_value(key) is not None:
        process_and_store(key, raw_value)
    else:
        raise KeyError(f"Key '{key}' does not exist.")


def delete_value(key):
    #raise NotImplementedError("Implement delete_value using TDD")
    if datastore.get_value(key) is not None:
        datastore.delete_value(key)
        return True
    else:
        return False


def list_all_keys():
    #raise NotImplementedError("Implement list_all_keys using TDD")
    return datastore.list_keys()
