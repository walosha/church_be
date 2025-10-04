import os
import json
from .models import Event
from rest_framework import generics, response, status
from .serializers import EventSerializer, CalenderSerializer
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.errors import HttpError
from datetime import datetime
import pytz
import uuid

SCOPES = ["https://www.googleapis.com/auth/calendar"]

# Load credentials from environment variable


def get_google_credentials():
    google_creds_json = os.getenv('GOOGLE_SERVICE_ACCOUNT')
    if google_creds_json:
        creds_dict = json.loads(google_creds_json)
        credentials = service_account.Credentials.from_service_account_info(
            creds_dict)
        return credentials.with_scopes(SCOPES)
    return None


calendarId = os.getenv('CALENDER_ID')


class EventListCreateAPIView (generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            serializer.save()


class EventRetrieveAPIView (generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDestroyAPIView (generics.DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventUpdateAPIView (generics.UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


def build_service(request):
    credentials = get_google_credentials()
    if not credentials:
        raise Exception("Google credentials not configured")
    service = build("calendar", "v3", credentials=credentials)
    return service


class CalenderCreateAPIView (generics.CreateAPIView):
    serializer_class = CalenderSerializer

    def post(self, request, *args, **kwargs):
        request = request.data
        if self.request:
            return self.form_valid(request)
        else:
            return self.form_valid(request)

    def form_valid(self, request):

        eventTitle = request.get("eventTitle")
        start_date_data = request.get("startDateTime")
        end_date_data = request.get("endDateTime")

        if start_date_data > end_date_data:
            return response.Response({"mesage": 'Please enter the correct period.'})
        service = build_service(self.request)
        event = {
            "calendarId": calendarId,
            # "conferenceDataVersion": 1,
            "end": {
                'dateTime': datetime.now(pytz.timezone('US/Central')).isoformat(),
                'timeZone': 'US/Central'
            },
            "start": {
                'dateTime': '2023-01-31T17:00:00-07:00',
                'timeZone': 'US/Central'
            },
            "conferenceData": {
                "entryPoints": [{"entryPointType": "video", }],
                "createRequest": {
                    "conferenceSolutionKey": {
                        "type": "hangoutsMeet"
                    },
                    "requestId": f"{uuid.uuid4().hex}"
                }
            },
            "summary": eventTitle
        }

        # Implement worldwide delegation on admin account

        # result = service.events().insert(conferenceDataVersion=1,calendarId=calendarId, body=event).execute()
        print("-------------------------------------------------")

        result = service.events().insert(body=event).execute()
        print("--------------------RESULT--------------------------")
        return response.responses({"data": result.get('organizer'), "status": status.HTTP_201_CREATED})

    def get_context_data(self, request):
        """Shows basic usage of the Google Calendar API.
        Prints the start and name of the next 10 events on the user's calendar.
        """

        try:

            service = build_service(self.request)

            events_result = service.events().list(calendarId=calendarId, timeMin='2022-01-25T17:00:00-07:00',
                                                  maxResults=10, singleEvents=True,
                                                  orderBy='startTime').execute()
            events = events_result.get('items', [])

            if not events:
                print('No upcoming events found.')
                return

            # Prints the start and name of the next 10 events
            for event in events:
                start = event['start'].get(
                    'dateTime', event['start'].get('date'))
                print("---", start, event['summary'], "---")
            return response.responses(data=event, status=status.HTTP_201_CREATED)

        except HttpError as error:
            print('An error occurred: %s' % error)
