from typing import Any, Dict, List
from .requester import Requester


class MountainProject(object):
    def __init__(self, access_key: str) -> None:
        self.__requester = Requester(access_key)

    def get_user(self, email: str = None, user_id: str = None) -> Dict[str, Any]:
        arg_error = "requires exactly one of email or user_id"
        assert not (email is None and user_id is None), arg_error
        assert not (email is not None and user_id is not None), arg_error

        params = {"email": email, "userId": user_id}
        return self.__requester.get("/get-user", params=params)

    def get_ticks(self, email: str = None, user_id: str = None) -> Dict[str, Any]:
        arg_error = "requires exactly one of email or user_id"
        assert not (email is None and user_id is None), arg_error
        assert not (email is not None and user_id is not None), arg_error

        params = {"email": email, "userId": user_id}
        return self.__requester.get("/get-ticks", params=params)

    def get_todos(self, email: str = None, user_id: str = None) -> Dict[str, Any]:
        arg_error = "requires exactly one of email or user_id"
        assert not (email is None and user_id is None), arg_error
        assert not (email is not None and user_id is not None), arg_error

        params = {"email": email, "userId": user_id}
        return self.__requester.get("/get-to-dos", params=params)

    def get_routes(self, route_ids: List[str]) -> Dict[str, Any]:
        cs_route_ids = ",".join(route_ids)
        params = {"routeIds": cs_route_ids}
        return self.__requester.get("/get-routes", params=params)

    def get_routes_for_lat_lon(
        self,
        lat: float,
        lon: float,
        max_distance: float = None,
        max_results: int = None,
        min_difficulty: str = None,
        max_difficulty: str = None,
    ):
        params = {
            "lat": lat,
            "lon": lon,
            "maxDistance": max_distance,
            "maxResults": max_results,
            "minDiff": min_difficulty,
            "maxDiff": max_difficulty,
        }
        return self.__requester.get("/get-routes-for-lat-lon", params=params)
