#!/usr/bin/env bash

# Get parameters from the workflow
export SOURCE_PREFIX=${1}
export SOURCE_SUFFIX=${2}
export DESTINATION_BUCKET=${3}
export DESTINATION_PREFIX=${4}
export DESTINATION_SUFFIX=${5}
export BACKUP_EXISTING=${6}

cd /opt/s3-copy/
pip install -r ./requirements.txt
python s3-copy.py
