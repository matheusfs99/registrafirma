build:
	docker-compose up -d --build

run:
	docker-compose up -d

down:
	docker-compose down

test:
	docker-compose exec web pytest

createsuperuser:
	docker-compose exec web python manage.py createsuperuser

install:
	pip install -r requirements.txt

secret:
	docker-compose exec web python utils/secret_gen.py
