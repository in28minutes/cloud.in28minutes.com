#!/bin/bash

set -e

source ./config.sh

echo "Starting datastore emulator on localhost environment"
gcloud beta emulators datastore start --host-port="$DATASTORE_EMULATOR_HOST"
