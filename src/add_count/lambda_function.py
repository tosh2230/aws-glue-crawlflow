import json
import logging

# logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        # Increment Count
        check_count = int(event['CheckCount'])
        check_count += 1
        logger.info('CheckCount: %s', str(check_count))

        return check_count

    except Exception as e:
        logger.exception(e, exc_info=False)
        raise e