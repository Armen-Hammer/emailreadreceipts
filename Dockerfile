# 1
FROM python:3.9

COPY . /app
WORKDIR /app

#2
RUN pip install Flask gunicorn

RUN pip install twilio


#4
ENV PORT 8080

#5
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app