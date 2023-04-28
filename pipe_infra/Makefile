.PHONY: run build up down clean

run:
	@python table_creation.py
	@python table_creation.py
	@python table_creation.py

# Build the Docker image
build:
	docker-compose build

# Start the containers
up:
	docker-compose up -d

# Stop the containers
down:
	docker-compose down

# Clean up Docker containers, networks, and images
clean:
	docker system prune -a --volumes --force

# Rebuild and run the containers
rebuild: down clean build up

################################################################################
# Test the application

format:
	docker exec -it ${CONTAINER_NAME} python -m black -S .

isort:
	docker exec -it ${CONTAINER_NAME} python -m isort .

lint:
	docker exec -it ${CONTAINER_NAME} python -m flake8 .

type:
	docker exec -it ${CONTAINER_NAME} python -m mypy --ignore-missing-imports .

start_integration: isort format type lint
