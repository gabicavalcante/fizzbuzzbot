# Flask - Fizz Buzz Bot

![Build Status](https://github.com/gabicavalcante/fizzbuzzbot/workflows/CI/badge.svg)
[![Code Coverage](https://codecov.io/gh/gabicavalcante/fizzbuzzbot/branch/master/graphs/badge.svg)](https://codecov.io/gh/gabicavalcante/fizzbuzz)

### create and active virtualenv

```
# virtualenv
$ virtualenv -p python3 env
$ source env/bin/activate
# pyenv
$ pyenv virtualenv 3.7.4 fizzbuzz
$ pyenv activate fizzbuzz
```

### install requirements

```
$ cd fizzbuzz
$ pip install -r requirements-dev.txt
```

_note_: `requirements-dev.txt` has all requirements packages to test, coverage and lint. If you don't want this packages, just run `pip install -r requirements.txt`.

### create and configure .env file

```
$ cp .env.sample .env
```

add the env vars:

```
FLASK_APP=fizzbuzz.app:create_app
SECRET_KEY="71b40786-c246-47c9-b3b1-cabe6917e0f6"
FLASK_ENV=development
```

### create and configure .secrets.toml

```
$ cp .secrets.toml.sample .secrets.toml
```

```
[default]
CSRF_SESSION_KEY = "s3cr37"
JWT_SECRET_KEY = ""
TELEGRAM_BOT_TOKEN = ""
TELEGRAM_BOT_USERNAME = "@"
BOT_HOST = ""
```

### migrate

```
$ flask db init
$ flask db migrate
$ flask db upgrade
```

### run

```
$  flask run
```

### docker-compose

You can run the app using the docker-compose file.

```
$  docker-compose up --build
```

### tests

To run tests with coverage:

```
$  pytest --cov=fizzbuzz
```


### references

- flask migrate https://flask-migrate.readthedocs.io/en/latest/
- precommit https://ljvmiranda921.github.io/notebook/2018/06/21/precommits-using-black-and-flake8/
