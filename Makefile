build-local:
	poetry lock --no-update --no-interaction --no-ansi 
	poetry export --without-hashes --with dev --format requirements.txt --output requirements.txt
	docker-compose build --force-rm

run-local:
	make build-local
	docker-compose up --force-recreate -d app
	docker-compose logs -f app
