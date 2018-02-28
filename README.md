# microservice_flask
example_microservice_using_flask

WIP Notes:

IP:
192.168.99.100


docker commands

# machine create

$ docker-machine create -d virtualbox testdriven-dev
$ eval "$(docker-machine env testdriven-dev)"

# machine ip

$ docker-machine ip testdriven-dev

# view logs

$ docker-compose -f docker-compose-dev.yml logs

# build (for requirements updates)

$ docker-compose -f docker-compose-dev.yml up -d --build

# run startup script

$ docker-compose -f docker-compose-dev.yml up -d

# recreate dbs

$ docker-compose -f docker-compose-dev.yml run users-service python manage.py recreate_db


# seed db

$ docker-compose -f docker-compose-dev.yml run users-service python manage.py seed_db

# run tests

$ docker-compose -f docker-compose-dev.yml run users-service python manage.py test


# hit user end-point

(machine ip is mapped to localhost)

$ curl http://localhost:5001/users

http://192.168.99.100:5001/users




# create new AWS-EC2 host

$ docker-machine create --driver amazonec2 testdriven-prod

# connect docker client to remote docker container

$ docker-machine env testdriven-prod

# set as active host
$ eval $(docker-machine env testdriven-prod)



# at pg 46