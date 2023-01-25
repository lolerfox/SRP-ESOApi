import json


def file_descriptor(name, file_type, action, var=None):
    if action == 'r':
        with open(name, action, encoding='utf-8') as f:
            if file_type == 'json':
                data = json.load(f)
            elif file_type == 'txt':
                data = f.read()

            return data
    elif action == 'w':
        with open(name, action, encoding='utf-8') as f:
            if file_type == 'json':
                json.dump(var, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    pass
