from __future__ import print_function

import json
import urllib
import boto3
import os

s3 = boto3.client('s3')


def pdflatex(*args):
    pass


def setup_tlsb():
    os.environ["PATH"] = os.environ["PATH"] + os.path.join(os.path.dirname(os.path.abspath(__file__)), '/tlsb-gui-installer/bin/x86_64-linux')
    print(os.environ["PATH"])


def lambda_handler(event, context):
    setup_tlsb()
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        print(response.__dict__)
        return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e

setup_tlsb()
