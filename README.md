[![CircleCI](https://circleci.com/gh/Ben-Hu/mountain_project.svg?style=svg)](https://circleci.com/gh/Ben-Hu/mountain_project) [![codecov](https://codecov.io/gh/Ben-Hu/mountain_project/branch/master/graph/badge.svg)](https://codecov.io/gh/Ben-Hu/mountain_project) [![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/Ben-Hu/mountain_project.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Ben-Hu/mountain_project/context:python) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) ![License](https://img.shields.io/github/license/Ben-Hu/mountain_project) ![Tag](https://img.shields.io/github/v/tag/Ben-Hu/mountain_project)

# MountainProject
Python MountainProject API Client

## Getting Started
- Sign up for MountainProject @ `https://www.mountainproject.com`
- Get your access key for the MountainProject data API @ `https://www.mountainproject.com/data`

```python
from mountain_project import MountainProject

m = MountainProject("access_key")
user = m.get_user("test@test.com")
ticks = m.get_ticks("test@test.com")
todos = m.get_todos("test@test.com")
routes_by_id = m.get_routes(["106034519", "111519266", "106028737"])
routes_by_location = m.get_routes_for_lat_lon(49.6867, -123.1350)
```