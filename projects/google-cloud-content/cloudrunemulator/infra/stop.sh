#!/bin/bash

# TO STOP THE EMULATOR PRESS Control+C
# AFTER THE EMULATOR RUN THE BELOW COMMAND TO REMOVE THE ENV. VARIABLES
echo "Cleaning up cloud-run emulator environment variables from localhost environment"
unset SRV_CONFIG_FILE
unset APP_SOURCE_PATH
unset DOCKERFILE
unset CLOUD_RUN_EMULATOR_APP_PORT
