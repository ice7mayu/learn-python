def welcome(name=''):
    print(f"user name is {name}")
    return f'welcome, {name or "guest"}'


def goodbye(name=''):
    print("new feature")
    return f'goodbye, {name or "guest"}'
