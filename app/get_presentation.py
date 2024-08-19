import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/presentations.readonly"]

creds = Credentials.from_authorized_user_file("token.json", SCOPES)

def get_presentation_info(presentation_id):
  """Shows basic usage of the Slides API.
  Prints the number of slides and elements in a sample presentation.
  """
  try:
    service = build("slides", "v1", credentials=creds)

    # Call the Slides API
    presentation = (
        service.presentations().get(presentationId=presentation_id).execute()
    )

    slides = presentation.get("slides")

    print(
      f'Presentation {presentation.get("presentationId")}, titled {presentation.get("title")} '
      f"contains {len(slides)} slides:"
    )

    for i, slide in enumerate(slides):
      print(
          f"- Slide #{i + 1} contains"
          f" {len(slide.get('pageElements'))} elements."
          f" The elements are {slide.get('pageType')}"
      )

  except HttpError as err:
    print(err)
  
  try:
    with open('presentation.json', 'w') as fp:
      json.dump(presentation, fp)
    print('Created presentation.json will all details')
  except:
    print('Unable to create presentation.json')

if __name__ == "__main__":

  presentation_id = os.environ['PRESENTATION_ID']
  get_presentation_info(presentation_id)