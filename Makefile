install:
	pip install -r requirements.txt


jwt_secret_key: 
	python -c "import secrets;print(f'JWT_SECRET_KEY=\"{secrets.token_urlsafe(64)}\"')" >> .secrets.toml


set_env:
	cp .env.sample .env 
	cp .secrets.toml.sample .secrets.toml
	make jwt_secret_key
	make install
	

clean:
	find . -name "*.pyc" -print0 | xargs -0 rm -rf
	-rm -rf htmlcov
	-rm -rf .coverage
	-rm -rf build
	-rm -rf dist
	-rm -rf $(PROJECT).egg-info


lint:
	pip install -r requirements-dev.txt
	black .
	flake8 .


test:
	pytest -vv 


coverage:
	pytest --cov=api


run:
	flask run