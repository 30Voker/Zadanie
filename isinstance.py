def clean(value):
    if isinstance(value, dict):
        new_dict = {}

        for key, item in value.items():
            cleaned = clean(item)

            if cleaned is not None:
                new_dict[key] = cleaned

        return new_dict if new_dict else None

    if isinstance(value, list):
        new_list = []

        for item in value:
            cleaned = clean(item)

            if cleaned is not None:
                new_list.append(cleaned)

        return new_list if new_list else None

    if isinstance(value, str):
        return value if value != '' else None

    return value


a = [
    {'x': 15, 'y': '', 'z': []},
    {},
    {'game': 'Dota', 'vers': 2, 'tags': {}},
    {'hero': 'pudge, invoker'}
]

a = clean(a)

print(a)
