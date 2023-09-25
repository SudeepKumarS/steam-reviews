# Documentation for stream getreviews API --> https://partner.steamgames.com/doc/store/getreviews
import os

from dotenv import load_dotenv

# Loading all the essential environment varaibles from .env file
load_dotenv(override=True)

STEAM_REVIEWS_BASEURL = os.getenv("STEAM_REVIEWS_BASEURL")
PUBG_APP_ID_STEAM = os.getenv("PUBG_APP_ID_STEAM")

try:
    if not any([STEAM_REVIEWS_BASEURL, PUBG_APP_ID_STEAM]):
        raise Exception("Some required envirables variables are not found")
except Exception as err:
    print(err)
