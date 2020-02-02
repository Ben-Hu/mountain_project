from mountain_project import MountainProject

import pytest
from unittest.mock import Mock


@pytest.fixture
def mock_requester():
    mock_requester = Mock()
    mock_requester.get.return_value = {"foo": "bar"}
    return mock_requester


@pytest.fixture
def client(mock_requester):
    return MountainProject("access_key", mock_requester)


def test_get_user(mocker, client, mock_requester):
    assert client.get_user(email="foo@bar.com") == {"foo": "bar"}
    mock_requester.get.assert_called_with(
        "/get-user", params={"email": "foo@bar.com", "userId": None}
    )

    assert client.get_user(user_id="123") == {"foo": "bar"}
    mock_requester.get.assert_called_with(
        "/get-user", params={"email": None, "userId": "123"}
    )


def test_get_ticks(mocker, client, mock_requester):
    assert client.get_ticks(email="foo@bar.com") == {"foo": "bar"}
    mock_requester.get.assert_called_with(
        "/get-ticks", params={"email": "foo@bar.com", "userId": None}
    )

    assert client.get_ticks(user_id="123") == {"foo": "bar"}
    mock_requester.get.assert_called_with(
        "/get-ticks", params={"email": None, "userId": "123"}
    )


def test_get_todos(mocker, client, mock_requester):
    assert client.get_todos(email="foo@bar.com") == {"foo": "bar"}
    mock_requester.get.assert_called_with(
        "/get-to-dos", params={"email": "foo@bar.com", "userId": None}
    )

    assert client.get_todos(user_id="123") == {"foo": "bar"}
    mock_requester.get.assert_called_with(
        "/get-to-dos", params={"email": None, "userId": "123"}
    )


def test_get_routes(mocker, client, mock_requester):
    assert client.get_routes(["a", "b", "c"]) == {"foo": "bar"}
    mock_requester.get.assert_called_with("/get-routes", params={"routeIds": "a,b,c"})


def test_get_routes_for_lat_lon(mocker, client, mock_requester):
    assert client.get_routes_for_lat_lon(0.0, 1.0) == {"foo": "bar"}
    mock_requester.get.assert_called_with(
        "/get-routes-for-lat-lon",
        params={
            "lat": 0.0,
            "lon": 1.0,
            "maxDistance": None,
            "maxResults": None,
            "minDiff": None,
            "maxDiff": None,
        },
    )

    assert client.get_routes_for_lat_lon(
        0.0,
        1.0,
        max_distance=100,
        max_results=200,
        min_difficulty="V3",
        max_difficulty="V5",
    ) == {"foo": "bar"}
    mock_requester.get.assert_called_with(
        "/get-routes-for-lat-lon",
        params={
            "lat": 0.0,
            "lon": 1.0,
            "maxDistance": 100,
            "maxResults": 200,
            "minDiff": "V3",
            "maxDiff": "V5",
        },
    )
