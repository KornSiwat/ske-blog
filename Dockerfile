# pull official base image
FROM python:3.8.2-alpine

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup -S app && adduser -S app -G app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/media
WORKDIR $APP_HOME

# install dependencies
COPY ./requirements.txt .
RUN apk update && apk add libpq
# dependencies for python modules
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache libressl-dev musl-dev libffi-dev
# install cryptography without rust *this is important*
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1
RUN pip install --no-cache-dir -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh $APP_HOME

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

# permission for entrypoint.sh
RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["/home/app/web/entrypoint.sh"]