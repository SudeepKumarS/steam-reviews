import traceback

import requests

from common.logger import logger


# Fetching the review data using the requests module
def get_review_data(url: str, params: dict) -> dict:
    """
    To retreive the data from the given url
    """
    try:
        # Updating the cursor value in the params
        response = requests.get(url=url, params=params).json()
        return response
    except Exception as err:
        logger.error(f"Error due to: {err}")
        logger.error(traceback.format_exc())
        raise err
