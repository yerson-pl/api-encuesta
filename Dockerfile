FROM python:3
WORKDIR /home/concytec/PycharmProjects/django/api-encuesta
ADD requirements.txt /home/concytec/PycharmProjects/django/api-encuesta
RUN pip install -r requirements.txt
ADD . /home/concytec/PycharmProjects/django/api-encuesta

