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
    def upload(source, destination, backup):
        """
        Upload local files to S3 bucket
        """
        print('Uploading Files...')

        base_path = os.environ['GITHUB_WORKSPACE']
        for source_filename in glob(base_path + '/*', recursive=True):
            if not source['suffix'] or str(source_filename).endswith(source['suffix']):
                if not source['prefix'] or str(os.path.basename(source_filename)).startswith(source['prefix']):
                    destination_filename = '{prefix}{source_filename}{suffix}'.format(
                        prefix=destination['prefix'],
                        source_filename=os.path.basename(source_filename),
                        suffix=destination['suffix']
                    )

                    while '//' in destination_filename:
                        destination_filename = destination_filename.replace('//', '/')

                    # Display logging messages
                    print('\nUploading: {source_filename}'.format(source_filename=source_filename))
                    print('Destination Bucket: {bucket}'.format(bucket=destination['bucket']))
                    print('Destination Filename: {destination_filename}'.format(destination_filename=destination_filename))

                    # If backup is enabled check if file exists
                    if backup['enabled'] is True:
                        try:
                            S3.__client__().head_object(Bucket=destination['bucket'], Key=destination_filename)
                            # If this does not generate an exception- the file already exists
                            original_file = {
                                'Bucket': destination['bucket'],
                                'Key': destination_filename
                            }

                            backup_filename = '{backup_prefix}{filename}{backup_suffix}.{timestamp}'.format(
                                backup_prefix=backup['prefix'],
                                backup_suffix=backup['suffix'],
                                filename=os.path.basename(destination_filename),
                                timestamp=datetime.utcnow().timestamp()
                            )

                            while '//' in backup_filename:
                                backup_filename = backup_filename.replace('//', '/')

                            # Copy to new filename
                            print('Backing Up Existing File...')
                            S3.__client__().copy_object(
                                CopySource=original_file,
                                Bucket=destination['bucket'],
                                Key=backup_filename
                            )
                            # Delete original file
                            S3.__client__().delete_object(
                                Bucket=destination['bucket'],
                                Key=destination_filename
                            )
                            print('Backup Complete: {backup_filename}'.format(backup_filename=backup_filename))
                        except ClientError:
                            pass

                    # Upload the new file
                    S3.__client__().upload_file(
                        Bucket=destination['bucket'],
                        Filename=source_filename,
                        Key=destination_filename
                    )

        print('Upload Complete')


if __name__ == '__main__':
    backup = str(sys.argv[6]).lower()
    S3.upload(
        source={
            'prefix': sys.argv[1],
            'suffix': sys.argv[2]
        },
        destination={
            'prefix': sys.argv[3],
            'suffix': sys.argv[4],
            'bucket': sys.argv[5]
        },
        backup={
            'enabled': backup == 'true' or backup == 1 or backup == 'yes',
            'prefix': sys.argv[7],
            'suffix': sys.argv[8]
        }
    )
