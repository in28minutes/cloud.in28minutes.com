#!/bin/bash

# Startup script for deploying python flask on cloudrun

# Build, and deploy.
sh build.sh
sh create_cloud_run.sh

echo "Done"
