import os
import json


def secret_key_loader():
    main_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    with open(f'{main_path}/secrets.json') as f:
        data = f.read()
        data = json.loads(data)['SECRET_KEY']
        return data


if __name__ == "__main__":
    print(secret_key_loader())