# Church management app

`

- Clone this repository
- docker compose --build && docker compose up
- source ./venv/bin/activate
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver --settings=core.settings.local ( Development )
- python manage.py runserver --settings=core.settings.prod ( Production )

`
@@ Access swagger documentation on : api/doc/#/

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
