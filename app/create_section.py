from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials


def create_section(presentation_id, page_id, title='Title'):
  """
  Create a section header slides with the specified title, by default at the end of the current presentation
  Load pre-authorized user credentials from the environment.
  """

  SCOPES = ["https://www.googleapis.com/auth/presentations"]
  creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  
  # pylint: disable=maybe-no-member
  try:
    service = build("slides", "v1", credentials=creds)
    requests = [
        {
          "createSlide": {
            "objectId": f'{page_id}',
            "slideLayoutReference": {
              "predefinedLayout": "SECTION_HEADER"
            },
            "placeholderIdMappings": [
              {
                "layoutPlaceholder": {
                  "type": "TITLE",
                  "index": 0
                },
                "objectId": f'{page_id}_title',
              },
            ],
          }
        },
      {
      "insertText": {
        "objectId": f'{page_id}_title',
        "text": f'{title}',
      }
      }
    ]

    # Execute the request.
    body = {"requests": requests}
    response = (
        service.presentations()
        .batchUpdate(presentationId=presentation_id, body=body)
        .execute()
    )
    create_slide_response = response.get("replies")[0].get("createSlide")
    print(f"Created slide with ID: {(create_slide_response.get('objectId'))} and title: {title}")

  except HttpError as error:
    print(f"An error occurred: {error}")
    print("Slides not created")
    return error

  return response


if __name__ == "__main__":
  id = '12rMAE3hFzkcvfsnMMOnpNMFc-YcX68YTtM8EiYY28-Y'
  create_section(id, "page1", 'Title1')
  create_section(id, "page2", 'Title2')