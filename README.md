# CPTER
Tool to help analyse cpt data

```
127.0.0.1:80/docs
```

## Fast api commands
```
$ uvicorn app.main:app --reload
```
## Docker

Final docker image is important. Difference between:
- Python
- Pyhton-lite
- Python-fastapi
Check https://testdriven.io/blog/fastapi-docker-traefik/

```
$ docker build . -t cpter

$ docker run --name cpter -p 80:80 -d cpter

$ docker restart cpter

$ docker logs cpter
```

## Docker-compose
```
$ docker-compose build

$ docker-compose up
```
```
$ docker-compose up -d --build cpter
```
## Postgresql
```
# Get in container w/ psql
$ docker exec -it cpter_db_1 psql --username=fastapi_traefik --dbname=fastapi_traefik
OR
$ docker-compose exec db psql --username=fastapi_traefik --dbname=fastapi_traefik
```
```
# Show DB's
$ \l

# Connect to db
$ \c name

# List tables in db
$ \dt
```

## Alembic
```
# Get in the container w/ bash
$ docker exec -it cpter_backend_1 bash
```
```
# Generate migration
$ alembic revision --autogenerate -m "Initial table generation & setup"

# Execute migration
$ alembic upgrade head

# Set DB state up-to-date
$ alembic stamp head
```

## Known issues
- authx package has issues with different python and other package versions
- keep track of env vars & pythonpath
- 