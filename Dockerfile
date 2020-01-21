FROM python:3
RUN apt-get update -y
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uwsgi", "--http", ":8000", "--wsgi-file", "barebone.py"]
