# Seat-Reservation-System

## Connect to Database

install mysql client on your machine if you haven't done yet

```
$ sudo apt-get install default-mysql-client
```


### Connect to Remote Testing MySQL Server
```
$ mysql -h 140.116.249.231 -u root -D master
```
### Run MySQL Instance on Localhost and Connect
```
$ ./db/setup.sh
$ docker-compose up -d
$ mysql -h 127.0.0.1 -u root -D master
```

---

## Run Backend Server
```
pipenv install
pipenv run uvicorn main:app --reload
```
