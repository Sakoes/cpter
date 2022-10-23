# CPTER
Tool to help analyse cpt data

## Fast api commands
```
$ uvicorn app.main:app --reload
```
## Docker
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