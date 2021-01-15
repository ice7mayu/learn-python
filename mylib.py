def welcome(name=''):
    print(f"user name is {name}")
    return f'hi, {name or "guest"}'


def goodbye(name=''):
    return f'goodbye, {name or "guest"}'
