import logging
import json
import hmac
import hashlib
import re
import datetime
import boto3
import base64

from botocore.exceptions import ClientError
from urllib.parse import unquote

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

events = boto3.client("events")

def process(content):
    entries = [
        {
            "Source": "My source",
            "DetailType": "Description",
            "Detail": content,
            "EventBusName": "default",
        }
    ]
    event_response = events.put_events(Entries=entries)

def lambda_handler(event, context):
    process(event["body"])