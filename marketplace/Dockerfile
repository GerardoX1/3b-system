FROM python:3.11

RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get install -y gcc \
    && apt-get install -y python3-dev \
    && apt-get install -y libpq-dev \
    && apt-get install -y gettext \
    && apt-get install -y git \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./start-web /start-web
RUN sed -i 's/\r$//g' /start-web
RUN chmod +x /start-web

WORKDIR /app
