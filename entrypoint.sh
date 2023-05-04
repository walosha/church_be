


docker-compose exec web python /code/church/manage.py migrate
docker-compose exec web python /code/church/manage.py collectstatic