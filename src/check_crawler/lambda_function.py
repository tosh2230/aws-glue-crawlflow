import os
import json
import logging
from datetime import date, datetime

import botocore
import boto3

# logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    class CrawlerThrottlingException(Exception): pass

    try:
        # Get Glue crawler name
        crawler_name = event['CrawlerName']

        glue_client = boto3.client('glue')
        response = glue_client.get_crawler(Name=crawler_name)
        logger.info('Response: %s', response)

        ret = {}
        ret['StatusCode'] = response['ResponseMetadata']['HTTPStatusCode']
        ret['CrawlerState'] = response['Crawler']['State']

        if 'LastCrawl' in response['Crawler'].keys():
            ret['LastCrawlStatus'] = response['Crawler']['LastCrawl']['Status']

        return ret

    except botocore.exceptions.ClientError as e:
        logger.exception(e, exc_info=False)

        if e.response.get('Error', {}).get('Code') == 'ThrottlingException':
            raise CrawlerThrottlingException(e)
        else:
            raise e

    except Exception as e:
        logger.exception(e, exc_info=False)
        raise e
