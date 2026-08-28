def indie_data(todo):
    return {
        "id":str(todo["_id"]),
        "title":todo["title"],
        "desc":todo["desc"],
        "status":todo["is_done"]
    }


def all_tasks(todos):
    return [indie_data(todo) for todo in todos]
