django-mease-example
====================

Simple chat example using [django](https://github.com/django/django), [django-mease](https://github.com/florianpaquet/django-mease) and [AngularJS](https://github.com/angular/angular.js).

![screenshot](https://raw.github.com/florianpaquet/django-mease-example/master/images/screenshot.png)

Installation
------------

Clone this repo and set up your virtualenv as usual :

```
git clone https://github.com/florianpaquet/django-mease-example.git
cd django-mease-example
virtualenv virtenv
source virtenv/bin/activate
pip install -r requirements.txt
```

`django-mease` comes with Redis PUB/SUB backend by default. Install these dependencies to get it to work :

```
sudo apt-get install redis-server python-dev
pip install redis toredis-mease
```

Set up sqlite database :

```
python manage.py syncdb
```

Usage
-----

Start websocket server in a first terminal :

```
python manage.py run_websocket_server
```

Start django debug server in a second one :

```
python manage.py runserver
```

Navigate to `http://localhost:8000` in your browser.
