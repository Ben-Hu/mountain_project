MountainProject
============================================
A Python API Client for the MountainProject data API

.. image :: https://circleci.com/gh/Ben-Hu/mountain_project.svg?style=svg
  :target: https://circleci.com/gh/Ben-Hu/mountain_project
  
.. image :: https://codecov.io/gh/Ben-Hu/mountain_project/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/Ben-Hu/mountain_project
  
.. image :: https://img.shields.io/lgtm/grade/python/g/Ben-Hu/mountain_project.svg?logo=lgtm&logoWidth=18
  :target: https://lgtm.com/projects/g/Ben-Hu/mountain_project/context:Python
  
.. image :: https://img.shields.io/badge/code%20style-black-000000.svg
  :target: https://github.com/psf/black
  
.. image :: https://img.shields.io/github/license/Ben-Hu/mountain_project
  :target: https://github.com/Ben-Hu/mountain_project/blob/master/LICENSE

.. image :: https://img.shields.io/github/v/tag/Ben-Hu/mountain_project
  :target: https://github.com/Ben-Hu/mountain_project/releases

.. image :: https://img.shields.io/pypi/v/mountain_project?color=blue
  :target: https://pypi.org/project/mountain-project


Getting Started
---------------
- Sign up for MountainProject @ `https://www.mountainproject.com`
- Get your access key for the MountainProject data API @ `https://www.mountainproject.com/data`


Install
-------
::

  pip install mountain_project


Examples
--------
.. code:: python

  from mountain_project import MountainProject

  m = MountainProject("access_key")
  user = m.get_user("test@test.com")
  ticks = m.get_ticks("test@test.com")
  todos = m.get_todos("test@test.com")
  routes_by_id = m.get_routes(["106034519", "111519266", "106028737"])
  routes_by_location = m.get_routes_for_lat_lon(49.6867, -123.1350)


.. toctree::
  :hidden:
  :maxdepth: 1

  mountain_project/modules