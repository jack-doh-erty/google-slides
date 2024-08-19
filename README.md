# Google Slides

Some functions to examine a presentation, create header slides and insert a slide with an image and title.

## Setup

- Run `generate_creds.py` to be redirected to google login and generate `credentials.json`
- Set `$PRESENTATION_ID` to your ID, based on the google slides url format: `https://docs.google.com/presentation/d/{presentation_id}`
- Run `source env.sh` to setup local envars for the bucket and gcloud project
- Set up [gcloud application default credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc#local-dev) using gcloud cli

Use the `venv` specific to this project and `pip -r requirements.txt` to install all dependencies.

The GCS bucket you use must have public access enabled by granting `allUsers` read access. Recommend setting a 1 day deletion for all uploaded objects under `Lifecycle` configuration.