#!/usr/bin/env bash

# Get parameters from the workflow
SOURCE_PREFIX=${1}
SOURCE_SUFFIX=${2}
DESTINATION_BUCKET=${3}
DESTINATION_PREFIX=${4}
DESTINATION_SUFFIX=${5}
BACKUP_EXISTING=${6}

# Setup Python
cd /opt/s3-copy/
pip install -r ./requirements.txt

# Start copying files
python s3-copy.py \
  ${SOURCE_PREFIX} \
  ${SOURCE_SUFFIX} \
  ${DESTINATION_BUCKET} \
  ${DESTINATION_PREFIX} \
  ${DESTINATION_SUFFIX} \
  ${BACKUP_EXISTING}
