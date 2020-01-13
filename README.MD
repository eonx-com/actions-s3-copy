# Github Actions: Copy Files To S3

This action can be used to upload files to
an S3 bucket, optionally backing up 
existing files by adding a timestamp
suffix.

```yaml
name: Copy File To S3

on:
  push:
    branches:
      - master

jobs:
  copy-files:
    name: Copy Files To S3
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Branch
        uses: eonx-com/actions-checkout@v1.0

      - name: Upload infrastructure files to S3 bucket
        uses: eonx-com/actions-s3-copy@v1.0
        with:
          # AWS secrets
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          AWS_DEFAULT_REGION: ${{ secrets.AWS_REGION }}
          
          # Source filename prefix
          SOURCE_PREFIX: 'infrastructure'
          
          # Source filename suffix
          SOURCE_SUFFIX: '.yml'
          
          # Destination filename prefix
          DESTINATION_PREFIX: 'infrastructure/'
          
          # Destination filename suffix
          DESTINATION_SUFFIX: ''
          
          # Destination S3 bucket name
          DESTINATION_BUCKET: 'deployment.infrastructure.dev.company.com'
          
          # Append current system timestamp to end of the file in S3 bucket
          TIMESTAMP: 'false'
```
