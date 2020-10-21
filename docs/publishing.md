# Publishing

Publishing is done with one command:

```shell

npm run publish

```

> Both the development and production sites will be published with `npm run publish`. Specify `--only hosting:dev` or `--only hosting:production` to target a specific site.

You will need to have Firebase's command line tool installed:

```shell

npm install -g firebase-tools

```

Afterwards, you can login to Firebase in the command line with:

```shell

firebase login

```

### Build process

The publishing build process contains three steps:

1. The app is containerized and uploaded to Container Registry.

You can build your container image using Cloud Build by running the following command from the directory containing the Dockerfile:

```shell

gcloud builds submit --tag gcr.io/${PROJECT_ID}/${APP_ID}

```

2. The container image is deployed to Cloud Run.

```shell

gcloud beta run deploy ${APP_ID} --image gcr.io/${PROJECT_ID}/${APP_ID} --region ${REGION} --allow-unauthenticated --service-account=${GCS_SA}

```

3. Hosting requests are directed to the containerized app.

This step provides access to this containerized app from a [Firebase Hosting](https://firebase.google.com/docs/hosting) URL, so that the app can generate dynamic content for the Firebase-hosted site.

```shell

firebase deploy --only hosting:production

```
