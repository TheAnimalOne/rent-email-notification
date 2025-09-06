Simple project that sends an email to remind myself that my rent is due :sob:.

Mostly to play around in google cloud run.
Using Docker for the first time as well as the Google Cloud CLI. 
The plan is to create a docker image using the Dockerfile (with uv) that is then uploaded to the Artifact Repository with the Google Cloud CLI.
The image will then be used to create a Google Cloud Run Job, with an automated trigger.
