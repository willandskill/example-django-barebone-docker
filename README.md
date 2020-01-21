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

Build it via the local `Dockerfile`

```
docker built -t djangoapp .
```

And then run it on port 8000

```
docker run -d -p 8000:8000 djangoapp
```

Go to http://localhost:8000 to see that the app works

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