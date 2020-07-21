import requests as rq
from classes.exceptions import UnsafeAdress
from typing import AnyStr


class CurrentWeather:
    """
    Parameters
    api_key:  api key to service whose provide weather information

    city_name: name of the city whose water data will be provided
    state_code: optional argument work only if city is in usa, (city with the same names can be in few states)
    country: optional argument (city with the same name can be in few countries)
    allow_http: optional argument allow or disallow not safe http connections
    api_link: link to api endpoint format api.openweathermap.org/data/2.5/weather?q={0},{1},{2}&appid={3}
                                          .format(city_name,state_code,country,api_key)
    """

    def __init__(
        self,
        api_key: AnyStr,
        city_name: AnyStr,
        state_code=None,
        country=None,
        allow_http=False,
        api_link="""https://api.openweathermap.org/data/2.5/weather?q={0},{1},{2}&appid={3}""",
    ):
        self.api_key = api_key
        self.city_name = city_name
        self.country = country
        self.state_code = state_code  # Only for USA
        self.api_link = api_link.format(city_name, state_code, country, api_key)
        self._check_url(allow_http)

    def _check_url(self, allow_http):
        """allow_http: if false and api_link start with http:// raise exception UnsafeAdress"""
        if self.api_link[:8] != "https://":
            if self.api_link[:4] == "http":
                if self.api_link[:5] != "https" and allow_http is False:
                    raise UnsafeAdress(
                        "Use https instead of http"
                    )  # i should write custom_exception to now use http
                if self.api_link[:5] != "https" and allow_http is True:
                    return self.api_link
            self.api_link = "https://" + self.api_link

    def make_request(self):
        """Return request response if connection succeed else raise exception"""
        data = rq.get(self.api_link.format(self.city_name, self.api_key))
        if data.ok:
            return data
        else:
            raise rq.HTTPError
