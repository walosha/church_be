
# Church Management App

This is a Church Management App that provides a variety of features for managing a church's activities, members, events, and content. The app includes an attendance system, blog, podcast, polls and surveys, pledges, offering and donation, prayer requests, contacts, and scheduling meetings, among other things.

Installation
- To install and run this app, follow the steps below:

- Clone this repository using git clone https://github.com/walosha/church_be.git.
- Run docker-compose --build && docker compose up to build and start the Docker containers.
- Activate the virtual environment using source ./venv/bin/activate.
- Install the required packages using pip install -r requirements.txt.
- Run python manage.py makemigrations to create the database migrations.
- Run python manage.py migrate to apply the database migrations.
- Run the app in development mode using python manage.py runserver --settings=core.settings.local, or in production mode using python manage.py runserver --settings=core.settings.prod.
- Access Swagger documentation on api/doc/#/.
Y- ou can also run the following commands:

```text
docker-compose exec web python /code/church/manage.py migrate: Migrate the database.
docker-compose exec web python /code/church/manage.py collectstatic or python manage.py collectstatic --settings=core.settings.local: Collect static files.
python manage.py check --settings=core.settings.prod (church directory): Check for deploy issues.
python manage.py check --deploy --settings=church.settings.prod: Check for deploy issues.
openssl req -x509 -newkey rsa:2048 -sha256 -days 3650 -nodes -keyout ssl/church.key -out ssl/church.crt -subj '/CN=_.church.com' -addext 'subjectAltName=DNS:_.church.com': Generate SSL cert.
docker-compose exec nginx nginx -s reload: Reload NGINX.
```
## Features
This Church Management App has several features, including:

- User management (roles/permissions) / Members directory / Groups
- Events (meetings, events and programs) for activities Callender
- Attendance system for events
- Blog (post & comments)
- Podcast (Video and audio for sermons)
- Polls and Surveys
- Pledges, offering and donation
- Prayer request, Contact
- Schedule meetings
- Email
- Live streaming
- e-bible

Thank you for using our Church Management App!
