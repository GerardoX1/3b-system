FROM python:3.11

RUN apt-get update 

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./start-web /start-web
RUN sed -i 's/\r$//g' /start-web
RUN chmod +x /start-web

COPY ./start-celeryworker /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./start-celerybeat /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat
RUN chmod +x /start-celerybeat

COPY ./start-flower /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower

WORKDIR /app
