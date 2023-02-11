# Church management app

`

- Clone this repository
- docker-compose --build && docker compose up
- source ./venv/bin/activate
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver --settings=core.settings.local ( Development )
- python manage.py runserver --settings=core.settings.prod ( Production )

`
@@ Access swagger documentation on : api/doc/#/

`
docker-compose exec web python /code/church/manage.py migrate
docker-compose exec web python /code/church/manage.py collectstatic
or
python manage.py collectstatic --settings=core.settings.local
python manage.py check --settings=core.settings.prod (church directory)

python manage.py check --deploy --settings=church.settings.prod ( check for deploy issues)

// Generate SSL Cert

openssl req -x509 -newkey rsa:2048 -sha256 -days 3650 -nodes \
-keyout ssl/church.key -out ssl/church.crt \
-subj '/CN=_.church.com' \
-addext 'subjectAltName=DNS:_.church.com'

//reload NGNIX
docker-compose exec nginx nginx -s reload

`

## Features (Content Mgt System)

- User management (roles/permissions) / Members directory / Groups
- Events (meetings, events and programs) for activities Callender
- Attendance system for events
- Blog (post & comments )
- Podcast (Video and audio for sermons)
- Polls and Surveys
- pleadges, offering and donation
- Prayer Request ,Contact
- schedule meetings
- Email
- Live streeming
- e-bible
