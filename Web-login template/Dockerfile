FROM python:latest

LABEL mainteiner="alexmyku"

RUN pip install update \
    pip install flask

WORKDIR /webapp
RUN mkdir /templates
RUN mkdir /webapp/static
COPY app.py /webapp/
COPY templates /webapp/templates
COPY static /webapp/static
EXPOSE 80
CMD [ "python","app.py" ]
#Dockerfile by Al3x-Myku
