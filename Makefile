RUN = docker exec -it notify_web_app_1
superuser:
	$(RUN) python manage.py createsuperuser
cov:
	$(RUN) coverage html

test:
	$(RUN) coverage run manage.py test -v 2

start:
	docker-compose up --build

stop:
	docker-compose down