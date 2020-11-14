FROM python:3 as base

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

COPY . /code/

###########START NEW IMAGE : DEBUGGER ###################
FROM base as debug
RUN pip install ptvsd

WORKDIR /code/
CMD python -m ptvsd --host 0.0.0.0 --port 5678 --wait --multiprocess -m manage.py runserver 0.0.0.0:8000

###########START NEW IMAGE: PRODUCTION ###################
FROM base as prod

CMD manage.py runserver 0.0.0.0:8000