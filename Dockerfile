FROM python:3.7-alpine

# set work directory
WORKDIR /app

# install psycopg2
RUN apk update \
    && apk add --virtual build-essential gcc python3-dev musl-dev

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

RUN chmod +x start.sh

CMD ["sh", "./start.sh"]
