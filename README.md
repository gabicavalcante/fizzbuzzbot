# Flask - Fizz Buzz Bot

![Build Status](https://github.com/gabicavalcante/fizzbuzzbot/workflows/CI/badge.svg)
[![Code Coverage](https://codecov.io/gh/gabicavalcante/fizzbuzzbot/branch/master/graphs/badge.svg)](https://codecov.io/gh/gabicavalcante/fizzbuzzbot)
[![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=gabicavalcante_fizzbuzzbot&metric=alert_status)](https://sonarcloud.io/dashboard?id=gabicavalcante_fizzbuzzbot)

This is a simple python bot to response messages using FizzBuzz logic. For multiples of three, the bot response "Fizz", for the multiples of five, it response "Buzz". For numbers which are multiples of both three and five, it response "FizzBizz". For any other number, it response the number sent. For any thing else, it reponse `Hey, '{text}' is not a valid input :(`.

### about the project

This project is a Flask API to response telegram messages. All messages are save in MySQL database, and you can see the data using the admin interface (`/admin`). To access this interface, you need create a user. You can do that running `flask add-user -u username -p password` (change `username` and `password` for your credential). That user that you created, can be used to request a token, to access the REST API to get all messages datas (`/chats/all` and `/chats/<int:id>` are the endpoints).

You can find a docker-compose file that can be used to run the flask api and mysql db.

### python code formartter

- [`black`](https://github.com/psf/black)
- [`flake8`](http://flake8.pycqa.org/en/latest/)
- [`pre-commit`](https://pre-commit.com/): the file `.pre-commit-config.yml` is a file to configure git hooks for identify simple issues before submit a commit. Run `pre-commit install` to set up the git hook scripts. After that, `pre-commit` will run automatically on `git commit`.

### libs

- telegram wrapper: [`python-telegram-bot`](https://github.com/python-telegram-bot/python-telegram-bot)
- config: [`dynaconf`](https://dynaconf.readthedocs.io/en/latest/)
- admin: [`flask_admin`](https://flask-admin.readthedocs.io/en/latest/)
- auth: [`flask_simplelogin`](https://github.com/flask-extensions/flask_simplelogin)
- commands: [`click`](https://flask.palletsprojects.com/en/1.0.x/cli/)
- tests: [`pytest`](https://docs.pytest.org/en/latest/)
- token: [`flask_jwt_extended`](https://flask-jwt-extended.readthedocs.io/en/stable/)
- log: [`logging`](https://flask.palletsprojects.com/en/1.0.x/logging/)
- db: [`flask_sqlalchemy`](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) and [`flask_migrate`](https://flask-migrate.readthedocs.io/en/latest/)
- appearance: [`flask_bootstrap`](https://pythonhosted.org/Flask-Bootstrap/)

### coverage report

- [codecov](https://codecov.io/gh/gabicavalcante/fizzbuzzbot)

### continuous code quality

- [sonar](https://sonarcloud.io/dashboard?id=gabicavalcante_fizzbuzzbot)

### create a bot

First of all, you need to create a telegram bot. So, if you don't know how, I'll explain, but you look this [telegram doc](https://core.telegram.org/bots) for details.
You just need talk to BotFather (it's a telegram bot, you can open a chat with him) and follow a few simple steps. After that, you've created a bot and received your authorization token.

## setup

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
CSRF_SESSION_KEY = ""
JWT_SECRET_KEY = ""
TELEGRAM_BOT_TOKEN = ""
BOT_HOST = "https://"
```

### configure the .settings.toml

Open the .settings.toml file and check all variables. See if you want change any thing. I set the `SQLALCHEMY_DATABASE_URI` to connect with the mysql credentials that I defined in docker-compose file. If you change one of these files, remenber to change other.

## run

### docker-compose

You can run the app using the docker-compose file.

```
$  docker-compose up --build
```

To test, run `ngrok` to expose your local server:

```
$ ./ngrok http 5000
ngrok by @inconshreveable

Session Status                online
Session Expires               7 hours, 59 minutes
Version                       2.3.35
Region                        United States (us)
Web Interface                 http://127.0.0.1:4040
Forwarding                    http://732498a9.ngrok.io -> http://localhost:5000
Forwarding                    https://732498a9.ngrok.io -> http://localhost:5000
```

Now, set the `BOT_HOST` var in `.secrets.toml` file, with the ngrok url (https).

```
[default]
CSRF_SESSION_KEY = "..."
JWT_SECRET_KEY = "..."
TELEGRAM_BOT_TOKEN = "..."
BOT_HOST = "https://732498a9.ngrok.io"
```

Access `127.0.0.1:5000/setwebhook` to start the webhook, and now you can use your bot. o/
You can see all message accessing `127.0.0.1:5000/admin`, the docker-compose created a user with username `admin` and password `admin`.

### flask run

#### virtualenv

```
# virtualenv
$ virtualenv -p python3 env
$ source env/bin/activate
# pyenv
$ pyenv virtualenv 3.7.4 fizzbuzz
$ pyenv activate fizzbuzz
```

#### install requirements

```
$ cd fizzbuzz
$ pip install -r requirements-dev.txt
```

_note_: `requirements-dev.txt` has all requirements packages to test, coverage and lint. If you don't want this packages, just run `pip install -r requirements.txt`.

#### migrate

```
$ flask db init
$ flask db migrate
$ flask db upgrade
```

#### run

```
$  flask run
```

## tests

Start the test db:

```
$  docker-compose up dbtest
```

To run tests with coverage

```
$  pytest --cov=fizzbuzz
```

### references

- flask migrate https://flask-migrate.readthedocs.io/en/latest/
- precommit https://ljvmiranda921.github.io/notebook/2018/06/21/precommits-using-black-and-flake8/
