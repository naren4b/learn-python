def format_service(name: str, port: int = 8080) -> str:
    return f'{name}:{port}'


if __name__ == '__main__':
    print(format_service('api'))
