from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def main(motive, full_name, name, start_datetime, end_datetime):
    """Creates an event in the user's calendar.
    Does not save the credentials.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    # if os.path.exists('token.pickle'):
    #     with open('token.pickle', 'rb') as token:
    #         creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        #with open('token.pickle', 'wb') as token:
        #    pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    event = {
          'summary': motive,
          'location': 'Sala de vidrio',
          'creator': {
            'displayName': full_name
          },
          'organizer': {
            'displayName': name
          },
          'start': {
            'dateTime': start_datetime,
            'timeZone': 'America/Bogota',
          },
          'end': {
            'dateTime': end_datetime,
            'timeZone': 'America/Bogota',
          },
          'visibility': 'public',
        }
    event = service.events().insert(calendarId='6q974sd40tgfue316ucgiunjb8@group.calendar.google.com',
                                    body=event).execute()
    return event

if __name__ == '__main__':
    main()
