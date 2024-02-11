import requests

class API_service:
    def __init__(self, needed_params: dict, url_api: str, route) -> dict:
        self.needed_params = needed_params
        self.url_api = url_api
        self.route = route

    def do_requests(self, search_param, added_params: dict):
        parameters = {**self.needed_params, **added_params}
        response = requests.get(self.url_api + self.route(search_param), 
                                            params=parameters)
        if response.status_code == 200:
            response = response.json()
            return response
        else: 
            return {'error': 'not found'}