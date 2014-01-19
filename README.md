django-mease-example
====================

Simple chat example using django-mease

![screenshot](https://raw.github.com/florianpaquet/django-mease-example/master/images/screenshot.png)

Installation
------------

Clone this repo and set up your virtualenv as usual. (Requires python3)

```
pip install -r requirements.txt
python manage.py syncdb
```

Usage
-----

Start websocket server in a first shell :

```
python manage.py start_websocket_server
```

Start django server in a second one :

```
python manage.py runserver
```

Navigate to `http://localhost:8000` in your browser.
