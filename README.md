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