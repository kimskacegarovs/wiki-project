FROM python:3.9.9-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /wiki
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8086", "--settings=wiki.settings.prod" ]
