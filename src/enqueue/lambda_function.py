import os
import json
import logging

import boto3

# logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# get env
QUEUE_URL = os.environ.get('QUEUE_URL')

# boto3 session
session = boto3.Session()
sqs = session.client('sqs')

def lambda_handler(event, context):
    """
    SQSに対してイベント情報をキューイングする

    Parameters
    ----------
    event : json
        トリガーイベント情報
    context : json
        実行環境情報
    
    Returns
    ----------
    response : json
        キューイング実行結果
    """
    try:
        logger.info('Send message to SQS')
        response = sqs.send_message(
            QueueUrl = QUEUE_URL,
            MessageBody = json.dumps(event)
        )

        return response

    except Exception as e:
        logger.exception(e, exc_info=False)
        raise e