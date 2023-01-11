import requests
class RequestUtil(object):
    URL_ENDPOINT = "http://174.138.35.154"
    PORT = 8000

    def make_post_request(self, ENDPOINT_ROUTE:str, data=None, json=None, token=None):
        headers = None
        if token:
            headers = {"token": token}
        res = requests.post(url=f"{self.URL_ENDPOINT}:{self.PORT}/{ENDPOINT_ROUTE}", data=data,
                            json=json, headers=headers)
        return res.json()

    def make_get_request(self, ENDPOINT_ROUTE: str, token: str):
        res = requests.get(url=f"{self.URL_ENDPOINT}:{self.PORT}/{ENDPOINT_ROUTE}/{token}")
        return res.json()

