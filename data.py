import json


def write_song(data, file_name):
    data = json.dumps(data)
    data = json.loads(str(data))

    with open(file_name, 'a', encoding='utf-8') as file:
        json.dump(data, file, indent=4)