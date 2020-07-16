import requests as rq
from classes.exceptions import UnsafeAdress


class CurrentWeather:
    """
    :arg
    api_key
    city_name
    allow_http optional argument if False raise exception if user pass http adres
    instead of https
    api_link optional argument whose contain link to api endpoint
    """

    def __init__(self, api_key, city_name, allow_http=False,
                 api_link="""api.openweathermap.org/data/2.5/weather?q={}&appid={}"""):
        self.api_key = api_key
        self.city_name = city_name
        self.api_link = api_link
        self._check_url(allow_http)

    def _check_url(self, allow_http):
        if self.api_link[:8] != "https://":
            if self.api_link[:4] == "http":
                if self.api_link[:5] != "https" and allow_http is False:
                    raise UnsafeAdress("Use https instead of http")  # i should write custom_exception to now use http
            self.api_link = "https://" + self.api_link

    def make_request(self):
        data = rq.get(self.api_link.format(self.city_name, self.api_key))
        if data.ok:
            return data
        else:
            raise rq.HTTPError
