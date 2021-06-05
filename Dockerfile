FROM shawara/django-alpine:base
ENV PYTHONUNBUFFERED 1

ENV APP_PATH /opt/Code
WORKDIR $APP_PATH

#installing django
COPY docker-entrypoint.sh requirements.txt /
RUN pip install -r /requirements.txt \
    && rm /requirements.txt \
    && chmod +x /docker-entrypoint.sh \
