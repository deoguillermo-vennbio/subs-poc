build:
	poetry lock --no-update --no-interaction --no-ansi 
	poetry export --without-hashes --format requirements.txt --output requirements.txt
	docker-compose build --force-rm

run:
	make build-local
	docker-compose up --force-recreate -d app
	docker-compose logs -f app

redis-cli:
	docker-compose exec redis redis-cli
