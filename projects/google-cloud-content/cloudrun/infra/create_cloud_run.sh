#!/bin/bash

echo "Deploying python application to cloud run"
gcloud beta run deploy $SERVICE_NAME \
  --project=$PROJECT_ID \
  --image=$IMAGE_NAME \
  --region=$REGION \
  --min-instances=1 \
  --max-instances=1 \
  --platform=managed \
  --allow-unauthenticated
