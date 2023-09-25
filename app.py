import traceback

from flask import Flask, Response, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint

from common.logger import logger
from common.review_collector import get_review_data
from common.settings import PUBG_APP_ID_STEAM, STEAM_REVIEWS_BASEURL

# Instantiating the flask server
app = Flask(__name__)


# Adding blueprint to showcase the schema of API
SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={"app_name": "Steam Game Reviews API"})
# Registering the above created blueprint in flask
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)


# Route to the homepage/rootpage
@app.route("/", methods=["GET"])
def index_page():
    return "Hi! This is a steam PUBG Game reviews fetcher"


# Route to list the reviews of the steam app
@app.route("/reviews", methods=["GET"])
def get_reviews() -> Response:
    try:
        # Extracting the given params into a different dict
        params = {key: value for key, value in request.args.items()}
        # This is a default param that needs to be passed
        # inorder to get the response in JSON format
        params.update({"json": 1})
        pubg_url = STEAM_REVIEWS_BASEURL + PUBG_APP_ID_STEAM
        response = get_review_data(url=pubg_url, params=params)
        response_data = []
        # To fetch the next set of documents using this cursor
        next_cursor = response.get("cursor")
        reviews_list = response.get("reviews")
        if reviews_list is None:
            error_message = "Failed to fetch reviews"
            logger.error(error_message)
            return jsonify({"error": error_message}), 400
        for review in reviews_list:
            author_id = review["author"]["steamid"]
            review_comment = review["review"]
            reviewed_at = review["timestamp_created"]
            response_data.append({"author_id": author_id, "review": review_comment, "timestamp_created": reviewed_at})
        return jsonify({"data": response_data, "next_cursor": next_cursor})
    except Exception as err:
        error_message = f"Error while processing the request: {str(err)}"
        logger.exception(error_message)
        # Adding a traceback to find the error
        logger.error(traceback.format_exc())
        return jsonify({"error": error_message}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0")
