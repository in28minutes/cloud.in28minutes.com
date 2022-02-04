#!/bin/bash

set -e

source ./config.sh

echo "Starting cloud-run emulator on localhost environment"
gcloud beta code dev "$SRV_CONFIG_FILE" --source="$APP_SOURCE_PATH" --dockerfile="$DOCKERFILE" --local-port="$CLOUD_RUN_EMULATOR_APP_PORT" --application-default-credential
