import requests


class HttpRequest:
    @staticmethod
    def get(url, return_json=True):
        # restful
        # json
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json if return_json else r.text
