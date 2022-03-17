# Seat-Reservation-System

## Initailize Database on Localhost
```
$ ./db/setup.sh
$ docker-compose up -d
```

## Run Backend Server
```
pipenv install
pipenv run uvicorn main:app --reload
```
