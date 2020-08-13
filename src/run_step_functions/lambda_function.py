import os
import json
import logging

import boto3

# logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# get env
STATEMACHINE_ARN = os.environ.get('STATEMACHINE_ARN')

# boto3 session
session = boto3.Session()
sf = boto3.client('stepfunctions')

def lambda_handler(event, context):
    """
    SQSキューにて指定されたステートマシンを起動する

    Parameters
    ----------
    event : json
        トリガーイベント情報
    context : json
        実行環境情報
    
    Returns
    ----------
    response : json
        ステートマシン起動リクエスト結果
    """
    try:
        logger.info('Get event from SQS')
        input = json.loads(event['Records'][0]['body'])

        logger.info('Start state machine')
        response = sf.start_execution(
            **{
                'input': json.dumps(input),
                'stateMachineArn': STATEMACHINE_ARN
            }
        )
        logger.info('executionArn: %s', response['executionArn'])

        return {
            "StatusCode": response['ResponseMetadata']['HTTPStatusCode'],
            "ExecutionArn": response['executionArn']
        }

    except Exception as e:
        logger.exception(e, exc_info=False)
        raise e