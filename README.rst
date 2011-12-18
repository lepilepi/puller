============
Puller
============
It automatically pulls from a git repository every time when a push occurres in a github repo.

Note: please, do not use on production site! It is for development only.

Requirements
------------

* python 2.6
* web.py

Configure receiver
------------------
First create a `config.py` file in the same directory with `puller_service.py`.(Rename `config.template.py`)

Required options:

* `REF`: This ref will be watched only, if the push is for other branch, nothing will happen
* `PATH`: The location of the `.git` folder
* `REMOTE`: The code will be pulled from this remote.
* `BRANCH`: This branch will be pulled, and merged locally.
* `WSGI_PATH`: The path ot the wsgi file, if the project runs with wsgi. This file will be touched to restart.

To start the service:

`python puller_service 0.0.0.0:8000`

Set up git
----------
In repository admin go to the service hooks (/admin/hooks).
Select `Post-Receive URLs`, and type your url, where puller_service runs, for example: `http://your.domain.com:8000/`

enjoy