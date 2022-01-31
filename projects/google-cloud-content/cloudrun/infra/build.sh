#!/bin/bash

cd ..

echo "Creating docker image"
docker build . -f Dockerfile -t $IMAGE_NAME
echo "Pushing docker image to google cloud container registry"
docker push $IMAGE_NAME
