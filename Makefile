ENV=local
include ./secrets/$(ENV)/.env

APP_NAME=greenlab

use_secrets:
	cp ./secrets/$(ENV)/.env ./.

down:
	docker compose down

build: use_secrets
	docker compose build

up: build
	docker compose up -d
	docker exec -it backend python create_categories.py
	docker exec -it backend python create_questions.py

unit_tests: up
	docker compose exec -T backend pytest -s --cov-report term-missing --cov=. ./tests/unit/

some_unit_tests: up
	docker compose exec -T backend pytest -s --cov-report term-missing --cov=. ./tests/unit/$(TEST_PATH)

integration_tests: up
	docker compose exec -T backend pytest -s --cov-report term-missing --cov=. ./tests/integration/

some_integration_tests: up
	docker compose exec -T backend pytest -s ./tests/integration/$(TEST_PATH)

tests: up
	docker-compose exec -T backend pytest -s --cov-report term-missing --cov=. ./tests/

lint:
	flake8 ./