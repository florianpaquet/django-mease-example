django-mease-example
====================

Simple chat example using [django-mease](https://github.com/florianpaquet/django-mease)

![screenshot](https://raw.github.com/florianpaquet/django-mease-example/master/images/screenshot.png)

Installation
------------

Clone this repo and set up your virtualenv as usual. (Requires python3)

```
pip install -r requirements.txt
python manage.py syncdb
```

`django-mease` comes with Redis PUB/SUB backend by default. Install these dependencies to get it to work :

```
sudo apt-get install redis-server python-dev
pip install redis toredis-mease
```

Usage
-----

Start websocket server in a first shell :

```
python manage.py run_websocket_server
```

Start django debug server in a second one :

```
python manage.py runserver
```

Navigate to `http://localhost:8000` in your browser.
