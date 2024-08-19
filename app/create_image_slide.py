from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
from upload_image import upload_blob
import os

def create_image_slide(presentation_id, page_id, url, title='Title'):
  """
  Inserts a new slides with the specified title and image.
  Designed for use with specifically-designed chart exports.
  Requires pre-loaded credentials in environment.
  """

  SCOPES = ["https://www.googleapis.com/auth/presentations"]
  creds = Credentials.from_authorized_user_file("token.json", SCOPES)

  try:
    service = build("slides", "v1", credentials=creds)
    # create slides and title elements
    requests = []
    requests.append(
        {
          "createSlide": {
            "objectId": f'{page_id}',
            "slideLayoutReference": {
              "predefinedLayout": "TITLE_ONLY"
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
        }
    )

    # update title
    requests.append(
      {
      "insertText": {
        "objectId": f'{page_id}_title',
        "text": f'{title}',
      }
      }
    )

    # insert the specified image
    image_id = "MyImage_11"
    emu4M = {"magnitude": 360, "unit": "PT"}
    requests.append(
        {
            "createImage": {
                "objectId": image_id,
                "url": url,
                "elementProperties": {
                    "pageObjectId": page_id,
                    "size": {"height": emu4M, "width": emu4M},
                    "transform": {
                        "scaleX": 1,
                        "scaleY": 1,
                        "translateX": 25,
                        "translateY": 45,
                        "unit": "PT",
                    },
                },
            }
        }
    )

    body = {"requests": requests}
    response = (
        service.presentations()
        .batchUpdate(presentationId=presentation_id, body=body)
        .execute()
    )

    print(f"Created slide with page_id {page_id}, title {title} and image {url}")

    return response
  except HttpError as error:
    print(f"An error occurred: {error}")
    print("Images not created")
    return error


if __name__ == "__main__":
  
  id = '12rMAE3hFzkcvfsnMMOnpNMFc-YcX68YTtM8EiYY28-Y'
  bucket_name = os.environ['BUCKET_NAME']
  url = upload_blob(bucket_name, 'chart.png', 'chart.png')
  create_image_slide(id, "image_page", url=url, title='Testing image inserts', )