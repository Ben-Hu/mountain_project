import pytest
from pytest_mock import mocker


from mountain_project import MountainProject
from mountain_project.requester import Requester


@pytest.fixture
def client():
    return MountainProject("access_key")


def test_get_user(mocker, client):
    mocker.patch(
        "mountain_project.requester.Requester.get", return_value={"foo": "bar"}
    )

    assert client.get_user(email="foo@bar.com") == {"foo": "bar"}
    Requester.get.assert_called_with(
        "/get-user", params={"email": "foo@bar.com", "userId": None}
    )

    assert client.get_user(user_id="123") == {"foo": "bar"}
    Requester.get.assert_called_with(
        "/get-user", params={"email": None, "userId": "123"}
    )


def test_get_ticks(mocker, client):
    mocker.patch(
        "mountain_project.requester.Requester.get", return_value={"foo": "bar"}
    )

    assert client.get_ticks(email="foo@bar.com") == {"foo": "bar"}
    Requester.get.assert_called_with(
        "/get-ticks", params={"email": "foo@bar.com", "userId": None}
    )

    assert client.get_ticks(user_id="123") == {"foo": "bar"}
    Requester.get.assert_called_with(
        "/get-ticks", params={"email": None, "userId": "123"}
    )


def test_get_todos(mocker, client):
    mocker.patch(
        "mountain_project.requester.Requester.get", return_value={"foo": "bar"}
    )

    assert client.get_todos(email="foo@bar.com") == {"foo": "bar"}
    Requester.get.assert_called_with(
        "/get-to-dos", params={"email": "foo@bar.com", "userId": None}
    )

    assert client.get_todos(user_id="123") == {"foo": "bar"}
    Requester.get.assert_called_with(
        "/get-to-dos", params={"email": None, "userId": "123"}
    )


def test_get_routes(mocker, client):
    mocker.patch(
        "mountain_project.requester.Requester.get", return_value={"foo": "bar"}
    )

    assert client.get_routes(["a", "b", "c"]) == {"foo": "bar"}
    Requester.get.assert_called_with("/get-routes", params={"routeIds": "a,b,c"})


def test_get_routes_for_lat_lon(mocker, client):
    mocker.patch(
        "mountain_project.requester.Requester.get", return_value={"foo": "bar"}
    )

    assert client.get_routes_for_lat_lon(0.0, 1.0) == {"foo": "bar"}
    Requester.get.assert_called_with(
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
    Requester.get.assert_called_with(
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
