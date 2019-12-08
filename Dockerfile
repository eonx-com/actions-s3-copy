FROM python:3.7

COPY s3-copy.py /opt/s3-copy/s3-copy.py
COPY requirements.txt /opt/s3-copy/requirements.txt

COPY entrypoint.sh /bin
ENTRYPOINT ["/bin/entrypoint.sh"]