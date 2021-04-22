FROM python:3.8.3-alpine
MAINTAINER Mateusz Głowiński

ENV PYTHONUNBUFFERED 1

ARG USER=app
ARG GROUP=app

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN mkdir /app
COPY ./ /app
WORKDIR /app
RUN pip install -r requirements.txt

RUN addgroup -S $GROUP && adduser -S $USER -G $GROUP
USER app

ENTRYPOINT ["./entrypoint.sh"]