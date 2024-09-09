from cryptocompare_api import get_price
import json

def main():
    print(json.dumps(get_price().json(), indent=4))

if __name__ == '__main__':
    main()