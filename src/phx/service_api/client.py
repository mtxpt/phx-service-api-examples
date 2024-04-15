import time
import requests
import phx.service_api.utility as utility
import phx.service_api.response as response


class Client:
    _base_path = '/phoenix/api/v1'
    _get_positions_path = _base_path + '/positions'
    _get_assets_path = _base_path + '/assets'
    _post_asset_transfer_path = _base_path + '/assets/transfer'
    _get_orders_path = _base_path + '/orders'
    _get_orders_history_path = _base_path + '/orders_history'
    _get_trades_history_path = _base_path + '/trades_history'
    _margin_type_path = _base_path + '/margin'
    _margin_leverage_path = _base_path + '/margin/leverage'
    _margin_isolated_path = _base_path + '/margin/isolated_margin'

    def __init__(self, api_key, secret_key, url):
        self.api_key = api_key
        self.secret_key = secret_key
        self.url = url

    def _make_request(self, request_method, api_path, query_params=None, body_params=None):
        if query_params is not None:
            query_params['timestamp'] = str(int(time.time() * 1000))

            signature = utility.get_signature(self.secret_key, api_path, query_params)
            query_params['signature'] = signature
        else:
            body_params['timestamp'] = str(int(time.time() * 1000))

            signature = utility.get_signature(self.secret_key, api_path, body_params)
            body_params['signature'] = signature

        request_id = utility.get_random_string(8)

        res = request_method(self.url + api_path, params=query_params, json=body_params, headers={
            'X-Request-ID': request_id,
            'X-MatrixPort-Access-Key': self.api_key
        }, verify=True)
        return response.Response(res.json())

    def get_positions(self, wallet_type, instrument_id=None):
        query_params = {
            'wallet_type': wallet_type,
        }

        if instrument_id is not None:
            query_params['instrument_id'] = instrument_id

        return self._make_request(requests.get, self._get_positions_path, query_params)

    def get_assets(self, wallet_type):
        query_params = {
            'wallet_type': wallet_type
        }

        return self._make_request(requests.get, self._get_assets_path, query_params)

    def get_open_orders(self, wallet_type, instrument_id=None):
        query_params = {
            'wallet_type': wallet_type,
        }

        if instrument_id is not None:
            query_params['instrument_id'] = instrument_id

        return self._make_request(requests.get, self._get_orders_path, query_params)

    def get_orders_history(self, wallet_type, instrument_id=None, start_time: int = None, end_time: int = None):
        query_params = {
            'wallet_type': wallet_type,
        }

        if instrument_id is not None:
            query_params['instrument_id'] = instrument_id
        if start_time is not None:
            query_params['start_time'] = start_time
        if end_time is not None:
            query_params['end_time'] = end_time

        return self._make_request(requests.get, self._get_orders_history_path, query_params)

    def get_trades_history(self, wallet_type, instrument_id=None, start_time: int = None, end_time: int = None):
        query_params = {
            'wallet_type': wallet_type,
        }

        if instrument_id is not None:
            query_params['instrument_id'] = instrument_id
        if start_time is not None:
            query_params['start_time'] = start_time
        if end_time is not None:
            query_params['end_time'] = end_time

        return self._make_request(requests.get, self._get_trades_history_path, query_params)

    def get_margin_type(self, wallet_type, instrument_id=None):
        query_params = {
            'wallet_type': wallet_type,
        }

        if instrument_id is not None:
            query_params['instrument_id'] = instrument_id

        return self._make_request(requests.get, self._margin_type_path, query_params)

    def set_margin_type(self, wallet_type, margin_type, instrument_id):
        body_params = {
            'wallet_type': wallet_type,
            'type': margin_type,
            'instrument_id': instrument_id
        }
        return self._make_request(requests.post, self._margin_type_path, body_params=body_params)

    def get_margin_leverage(self, wallet_type, instrument_id):
        query_params = {
            'wallet_type': wallet_type,
            'instrument_id': instrument_id
        }

        return self._make_request(requests.get, self._margin_leverage_path, query_params)

    def set_margin_leverage(self, wallet_type, leverage, instrument_id):
        body_params = {
            'wallet_type': wallet_type,
            'leverage': leverage,
            'instrument_id': instrument_id
        }

        return self._make_request(requests.post, self._margin_leverage_path, body_params=body_params)

    def set_isolated_margin(self, instrument_id, side, amount, wallet_type):
        body_params = {
            'wallet_type': wallet_type,
            'side': side,
            'amount': amount,
            'instrument_id': instrument_id
        }

        return self._make_request(requests.post, self._margin_isolated_path, body_params=body_params)

    def transfer_assets(self, from_wallet, to_wallet, asset, amount, from_instrument_id=None, to_instrument_id=None):
        body_params = {
            'from_wallet': from_wallet,
            'to_wallet': to_wallet,
            'asset': asset,
            'amount': amount,
        }

        if from_instrument_id is not None:
            body_params['from_instrument_id'] = from_instrument_id
        if to_instrument_id is not None:
            body_params['to_symbol'] = to_instrument_id

        return self._make_request(requests.post, self._post_asset_transfer_path, body_params=body_params)
