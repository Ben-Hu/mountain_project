import pytest
from pytest import raises
from pytest_mock import mocker

import requests

from mountain_project.requester import Requester, RequestException


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


@pytest.fixture
def requester():
    return Requester("access_key")


@pytest.fixture
def default_params():
    return {"key": "access_key"}


def test_get_success(mocker, requester, default_params):
    mock_response = MockResponse(200, {"foo": "bar"})
    mocker.patch("requests.get", return_value=mock_response)

    params = {"a": "b"}
    expected_params = {**default_params, **params}

    requester.get("/foo/bar", params=params)

    requests.get.assert_called_with(
        "https://www.mountainproject.com/data/foo/bar", params=expected_params
    )


def test_get_error(mocker, requester, default_params):
    mock_response = MockResponse(503, "503 Bad Gateway")
    mocker.patch("requests.get", return_value=mock_response)

    with raises(RequestException, match="503: 503 Bad Gateway"):
        requester.get("/foo/bar")
