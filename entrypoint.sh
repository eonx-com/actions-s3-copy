#!/usr/bin/env bash

# Get parameters from the workflow
SOURCE_PREFIX=${1}
SOURCE_SUFFIX=${2}
DESTINATION_PREFIX=${3}
DESTINATION_SUFFIX=${4}
DESTINATION_BUCKET=${5}
BACKUP_EXISTING=${6}
BACKUP_PREFIX=${7}
BACKUP_SUFFIX=${8}
TIMESTAMP=${9}

echo "Source Prefix: ${SOURCE_PREFIX}"
echo "Source Suffix: ${SOURCE_SUFFIX}"
echo "Destination Prefix: ${DESTINATION_PREFIX}"
echo "Destination Suffix: ${DESTINATION_SUFFIX}"
echo "Destination Bucket: ${DESTINATION_BUCKET}"
echo "Backup Existing Files: ${BACKUP_EXISTING}"
echo "Backup File Prefix: ${BACKUP_PREFIX}"
echo "Backup File Suffix: ${BACKUP_SUFFIX}"
echo "Timestamp: ${TIMESTAMP}"

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
  "${BACKUP_EXISTING}" \
  "${BACKUP_PREFIX}" \
  "${BACKUP_SUFFIX}" \
  "${TIMESTAMP}" \
