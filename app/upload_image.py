from google.cloud import storage
import os

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    # returns the URL of the created object

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )

    return f'https://storage.googleapis.com/{bucket_name}/{destination_blob_name}'

if __name__ == "__main__":

    project = os.environ['GCLOUD_PROJECT']
    bucket_name = os.environ['BUCKET_NAME']
    source_file_name = 'chart.png'
    destination_blob_name = 'chart.png'

    upload_blob(bucket_name, source_file_name, destination_blob_name)