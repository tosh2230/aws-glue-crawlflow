import os
import json
import logging
from datetime import date, datetime

import boto3
import botocore

# logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    class CrawlerThrottlingException(Exception): pass
    class CrawlerRunningException(Exception): pass

    try:
        # Get Glue crawler name
        crawler_name = event['CrawlerName']
        logger.info('CrawlerName: %s', crawler_name)

        glue_client = boto3.client('glue')
        response = glue_client.start_crawler(Name=crawler_name)
        logger.info('Response: %s', json.dumps(response))

        return {
            "StatusCode": response['ResponseMetadata']['HTTPStatusCode']
        }

    except botocore.exceptions.ClientError as e:
        logger.exception(e, exc_info=False)

        if e.response.get('Error', {}).get('Code') == 'ThrottlingException':
            raise CrawlerThrottlingException(e)
        elif e.response.get('Error', {}).get('Code') == 'CrawlerRunningException':
            raise CrawlerRunningException(e)
        else:
            raise e

    except Exception as e:
        logger.exception(e, exc_info=False)
        raise e