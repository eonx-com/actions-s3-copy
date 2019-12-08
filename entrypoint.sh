#!/usr/bin/env bash

# Get AWS credentials from workflow parameters
export AWS_ACCESS_KEY_ID=${1}
export AWS_SECRET_ACCESS_KEY=${2}
export AWS_DEFAULT_REGION=${3}

# Get other parameters from the workflow
export SOURCE_PREFIX=${4}
export SOURCE_SUFFIX=${5}
export DESTINATION_BUCKET=${6}
export DESTINATION_PREFIX=${7}
export DESTINATION_SUFFIX=${8}
export BACKUP_EXISTING=${9}

pip install -r ./requirements.txt
python s3-copy.py
