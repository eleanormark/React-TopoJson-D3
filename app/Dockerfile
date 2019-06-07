FROM python:3.7-alpine

RUN apk add --update make sqlite

ENV APP /data/app

RUN mkdir -p $APP
RUN mkdir -p $APP/www

WORKDIR $APP

COPY data $APP/data

COPY requirements.txt $APP
RUN pip install --no-cache-dir -r requirements.txt

COPY init_db.py $APP
COPY www/models.py $APP/www

RUN python init_db.py data/physicians.csv.gz

COPY . $APP

ENTRYPOINT ["make"]
