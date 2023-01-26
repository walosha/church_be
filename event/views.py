import os
from .models import Event
from rest_framework import generics,response,status
from .serializers import EventSerializer,CalenderSerializer
from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import  datetime 
import pytz,uuid




SCOPES = ["https://www.googleapis.com/auth/calendar"]
service_account_email = os.getenv('GOOGLE_SERVICE_ACCOUNT')
credentials = service_account.Credentials.from_service_account_file('church-375900-fbd978c352ca.json')
scoped_credentials = credentials.with_scopes(SCOPES)
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

    service = build("calendar", "v3", credentials=scoped_credentials)
    return service

class CalenderCreateAPIView (generics.CreateAPIView):
    serializer_class = CalenderSerializer

  
    def post(self, request, *args, **kwargs):
        request = request.data
        if self.request:
            return self.form_valid(request)
        else:
            return self.form_invalid(request)


    def form_valid(self, form):

        eventTitle = form.get("eventTitle")
        start_date_data = form.get("startDateTime")
        end_date_data = form.get("endDateTime")

        if start_date_data > end_date_data:
            return response.Response({"mesage": 'Please enter the correct period.'})
        service = build_service(self.request)
        print(datetime.now(pytz.timezone('US/Central')).isoformat())
        event = {
                    "summary": eventTitle,
                    "start": {"dateTime": datetime.now(pytz.timezone('US/Central')).isoformat()},
                    "end": {"dateTime": datetime.now(pytz.timezone('US/Central')).isoformat()},
                    # "attendees": [{"email": "walosha@gmail.com"}],
                    "conferenceData": {"createRequest": {"requestId": f"{uuid.uuid4().hex}"}},
                    "description": eventTitle,                                 
                    "reminders": {"useDefault": True}
                }
       
        result = service.events().insert(calendarId=calendarId, body=event).execute()
        print(result)
        return response.responses({"data":result.get('organizer'),"status":status.HTTP_201_CREATED})

    # def get_success_url(self):

    #     messages.add_message(self.request, messages.INFO, 'Form submission success!!')

    #     return reverse('cal:home')

    # def get_context_data(self, **kwargs):
    #     context = super(HomeView, self).get_context_data(**kwargs)
    #     form = BookingForm()
    #     booking_event = []
    #     service = build_service(self.request)
    #     events = (
    #         service.events().list(
    #             calendarId=calendarId,
    #         ).execute()
    #     )

    #     for event in events['items']:

    #         event_title = event['summary']

    #         # Deleted the last 6 characters (deleted UTC time)
    #         start_date_time = event["start"]["dateTime"]
    #         start_date_time = start_date_time[:-6]

    #         # Deleted the last 6 characters (deleted UTC time)
    #         end_date_time = event['end']["dateTime"]
    #         end_date_time = end_date_time[:-6]

    #         booking_event.append([event_title, start_date_time, end_date_time])

    #     context = {
    #         "form":form,
    #         "booking_event" : booking_event,
    #     }

    #     return context