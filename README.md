# django-barebone

A barebone Django project that only imports the most basic stuff in order to get Django up and running.

## Why?

This is perfect for building small apps that is supposed to do something very simple at first and then slowly grow into a full fledged app.

> This project is a barebone example of how Django can be used to create very small and efficient apps. From a code structure point of view, it is suboptimal. Please make sure to check the template for a normal Django project in order to see how things should be separated into conveniently named files.

## Get started

1. Create a virtual enviroment and activate it

```
python3 -m venv barebone-env
source barebone-env/bin/activate
```

2. Install Django

```
pip install django
```

3. Run the development server

```
python barebone.py runserver
```

---

## Build and run it with Docker

#### Build it via the local `Dockerfile`

```
docker build -t djangoapp .
```

#### And then run it on port 8000

```
docker run -d -p 8000:8000 djangoapp
```

Go to http://localhost:8000 to see that the app works

#### Jump into the running Docker container

You can run `docker ps` in order to see all the running containers

```
docker ps
```

And the output should be something similar to the one below

```
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
0f61b4378dc3        django              "uwsgi --http :8000 …"   28 minutes ago      Up 28 minutes       0.0.0.0:8000->8000/tcp   awesome_perlman
```

And after that if You want to jump into an interactive shell You can run the command below

```
docker exec -it awesome_perlman /bin/bash
```

You can also run a single command like below, in our example we want to see all the files in our root folder

```
docker exec -it awesome_perlman ls
```

And the output is

```
Dockerfile  README.md  __pycache__  barebone.py  now.json  requirements.txt
```

---

## Run it on Zeit Now

Run it in `development` mode

```
now dev
```

Push a version to `now`

```
now
```

Push a version to `production`

```
now --prod
```
