PROJECT=amino-frontend-challenge
COMPOSE_ARGS=-f docker-compose.yml -p ${PROJECT}

build: clean
	docker-compose ${COMPOSE_ARGS} build

test:
	docker-compose ${COMPOSE_ARGS} run --rm app test

run:
	docker-compose ${COMPOSE_ARGS} up

shell:
	docker-compose ${COMPOSE_ARGS} run --rm app shell

clean:
	docker-compose ${COMPOSE_ARGS} stop
	docker-compose ${COMPOSE_ARGS} rm -f
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
