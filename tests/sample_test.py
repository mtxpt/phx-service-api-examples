from phx.service_api.client import Client
import json

base_url = 'https://api.mp-phoenix-prime.com'


def get_api_key():
    with open('secret.json') as json_file: 
        key = (json.load(json_file))["api_key"]
    return key


def get_secret_key():
    with open('secret.json') as json_file: 
        key = (json.load(json_file))["secret_key"]
    return key


def get_m_assets(wallet_type="UM_FUTURES"):
    client = Client(api_key=get_api_key(), secret_key=get_secret_key(), url=base_url)

    obj = client.get_assets(
        wallet_type=wallet_type)
    return obj.get_response(exclude_metadata=False)


def check_assets(coin):
    obj = get_m_assets()
    data = json.loads(obj['metadata'])
    list_of_assets = data['assets']
    return [asset for asset in list_of_assets if asset["asset"] == coin][0]


def check_positions(symbol):
    obj = get_m_assets()
    data = json.loads(obj['metadata'])
    list_of_positions = data['positions']
    return [loc_symbol for loc_symbol in list_of_positions if loc_symbol["symbol"] == symbol][0]


if __name__ == "__main__":
    print(check_assets("BTC"))
    print(check_positions("ETHUSDT"))
