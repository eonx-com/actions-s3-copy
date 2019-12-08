#!/usr/bin/env bash

# Get parameters from the workflow
SOURCE_PREFIX=${1}
SOURCE_SUFFIX=${2}
DESTINATION_PREFIX=${3}
DESTINATION_SUFFIX=${4}
DESTINATION_BUCKET=${5}
BACKUP_EXISTING=${6}

echo "Source Prefix: ${1}"
echo "Source Suffix: ${2}"
echo "Destination Prefix: ${3}"
echo "Destination Suffix: ${4}"
echo "Destination Bucket: ${5}"
echo "Backup: ${6}"

# Setup Python
cd /opt/s3-copy/
pip install -r ./requirements.txt

# Start copying files
python s3-copy.py \
  "${SOURCE_PREFIX}" \
  "${SOURCE_SUFFIX}" \
  "${DESTINATION_PREFIX}" \
  "${DESTINATION_SUFFIX}" \
  "${DESTINATION_BUCKET}" \
  "${BACKUP_EXISTING}"
