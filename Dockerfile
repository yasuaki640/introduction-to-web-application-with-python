FROM python:3.10.2-bullseye

COPY ./src /var/www/app

WORKDIR /var/www/app
