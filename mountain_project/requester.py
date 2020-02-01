from abc import ABC, abstractmethod
from typing import Any

import requests


class Requester(ABC):
    @abstractmethod
    def __init__(self, access_key: str) -> None:
        pass

    @abstractmethod
    def get(self, path: str, params: dict = {}) -> Any:
        pass


class RestRequester(Requester):
    def __init__(self, access_key: str) -> None:
        self.__domain: str = "https://www.mountainproject.com/data"
        self.__access_key: str = access_key

    def get(self, path: str, params: dict = {}) -> Any:
        url = f"{self.__domain}{path}"
        base_params = {"key": self.__access_key}
        request_params = {**base_params, **params}
        response = requests.get(url, params=request_params)
        if response.status_code == 200:
            return response.json()
        else:
            raise RequestException(response.status_code, response.text)


class RequestException(Exception):
    def __init__(self, status_code: int, data: str):
        self.__status_code = status_code
        self.__data = data

    def __str__(self):
        return f"{self.__status_code}: {self.__data}"
