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
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          AWS_DEFAULT_REGION: ${{ secrets.AWS_REGION }}
          SOURCE_PREFIX: 'infrastructure'
          SOURCE_SUFFIX: '.yml'
          DESTINATION_PREFIX: 'infrastructure/'
          DESTINATION_SUFFIX: ''
          DESTINATION_BUCKET: 'deployment.infrastructure.dev.company.com'
          TIMESTAMP: 'false'
```
