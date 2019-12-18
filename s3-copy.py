import boto3
import os
import sys

from botocore.exceptions import ClientError
from datetime import datetime
from glob import glob


class S3:
    __s3_client__ = None

    @staticmethod
    def __client__():
        """
        Return cached S3 client
        """
        if S3.__s3_client__ is None:
            S3.__s3_client__ = boto3.client('s3')
        return S3.__s3_client__

    @staticmethod
    def upload(source, destination):
        """
        Upload local files to S3 bucket
        """
        print('Uploading Files...')

        timestamp = ''
        if str(destination['timestamp']).lower() == 'true':
            timestamp = '.{timestamp}'.format(timestamp=datetime.utcnow().timestamp())

        base_path = os.environ['GITHUB_WORKSPACE']
        for source_filename in glob(base_path + '/*', recursive=True):
            filename = source_filename[len(base_path):]
            print('checking suffix: {s}'.format(s=source['suffix']))
            print(filename)
            if not source['suffix'] or filename.endswith(source['suffix']):

                print('checking prefix: {s}'.format(s=source['prefix']))
                print(filename)
                if not source['prefix'] or filename.startswith(source['prefix']):
                    destination_filename = '{prefix}{source_filename}{suffix}{timestamp}'.format(
                        prefix=destination['prefix'],
                        source_filename=filename_base,
                        suffix=destination['suffix'],
                        timestamp=timestamp
                    )

                    while '//' in destination_filename:
                        destination_filename = destination_filename.replace('//', '/')

                    # Display logging messages
                    print('\nUploading: {source_filename}'.format(source_filename=source_filename))
                    print('Destination Bucket: {bucket}'.format(bucket=destination['bucket']))
                    print('Destination Filename: {destination_filename}'.format(destination_filename=destination_filename))

                    # Upload the new file
                    S3.__client__().upload_file(
                        Bucket=destination['bucket'],
                        Filename=source_filename,
                        Key=destination_filename
                    )

        print('Upload Complete')


if __name__ == '__main__':
    S3.upload(
        source={
            'prefix': sys.argv[1],
            'suffix': sys.argv[2]
        },
        destination={
            'prefix': sys.argv[3],
            'suffix': sys.argv[4],
            'bucket': sys.argv[5],
            'timestamp': sys.argv[6]
        }
    )
