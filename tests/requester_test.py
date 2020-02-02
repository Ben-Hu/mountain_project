import pytest
from pytest import raises

import requests

from mountain_project.requester import RestRequester, RequestException


class MockResponse(object):
    def __init__(self, status_code, data):
        self.__status_code = status_code
        self.__data = data

    @property
    def status_code(self):
        return self.__status_code

    @property
    def text(self):
        return self.__data

    def json(self):
        return self.__data


class TestRestRequester(object):
    @pytest.fixture
    def requester(self):
        return RestRequester("access_key")

    @pytest.fixture
    def default_params(self):
        return {"key": "access_key"}

    def test_get_success(self, mocker, requester, default_params):
        mock_response = MockResponse(200, {"foo": "bar"})
        mocker.patch("requests.get", return_value=mock_response)

        params = {"a": "b"}
        expected_params = {**default_params, **params}

        requester.get("/foo/bar", params=params)

        requests.get.assert_called_with(
            "https://www.mountainproject.com/data/foo/bar", params=expected_params
        )

    @pytest.mark.parametrize(
        "mock_response, error_message",
        [(MockResponse(n, f"{n} message"), f"{n} message") for n in range(201, 599)],
    )
    def test_get_error(self, mocker, requester, mock_response, error_message):
        mocker.patch("requests.get", return_value=mock_response)

        with raises(RequestException, match=error_message):
            requester.get("/foo/bar")
