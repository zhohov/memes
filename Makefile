COMPOSE_FILE = docker-compose.dev.yaml

.PHONY: build
build:
	docker-compose -f ${COMPOSE_FILE} up --build

.PHONY: up
up:
	docker-compose -f ${COMPOSE_FILE} up -d

.PHONY: down
down:
	docker-compose -f ${COMPOSE_FILE} down

.PHONY: exec
exec:
	docker exec -it $(var) bash