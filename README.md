# Steam Application Reviews Fetcher
An API service that collects reviews for an application in the stream platform and list them.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Starting the Server](#starting-the-server)
  - [Accessing the API](#accessing-the-api)
- [Responses](#responses)
  - [Success Response](#success-response)
  - [Error Response](#error-response)
- [Swagger UI](#swagger-ui)
- [Approach](#approach)
- [Challenges](#challenges)

## Overview

This Flask-based project is designed to fetch and display reviews for the PUBG game on Steam. It provides a simple API for retrieving reviews in JSON format. The project is equipped with logging and Swagger UI for easy API documentation.

## Project Structure

The project structure is as follows:

- `app.py`: The main Flask application file.
- `common/settings.py`: Configuration settings, including the base URL and app ID for PUBG on Steam.
- `common/review_collector.py`: A module for fetching review data.
- `common/logger.py`: Logging configuration file and store them into a log file. 
- `common/logs/`: The directory where log files are stored.
- `static/swagger.json`: Swagger JSON file for API documentation.
- `templates/`: Templates for Swagger UI.

## Getting Started

### Prerequisites

Before running the project, make sure you have the following installed:

- Python 3.10
- Any IDE
- Git

### Installation

1. Clone this repository to your local machine.

```bash
git clone https://github.com/SudeepKumarS/steam-reviews.git
cd steam-reviews
```

2. Create a virtual environment (optional but recommended).

```bash
python -m venv venv
```

3. Activate the virtual environment.

   - On Windows:

   ```bash
   venv\Scripts\activate
   ```

   - On macOS and Linux:

   ```bash
   source venv/bin/activate
   ```

4. Install the project dependencies.

```bash
pip install -r requirements.txt
```

## Usage

### Starting the Server

To start the Flask server, run the following command:

```bash
python app.py
```

The server will start and listen on `http://0.0.0.0:5000`.

### Accessing the API

You can access the API using a web browser or a tool like `curl`. Here are the available endpoints:

- Home Page: `http://localhost:5000/`
- Get Reviews: `http://localhost:5000/reviews`

## Responses

### Success Response

```json
{
  "data": [
    {
      "author_id": "steam_user_id",
      "review": "review_comment",
      "timestamp_created": "reviewed_at"
    },
    {
      "author_id": "steam_user_id",
      "review": "review_comment",
      "timestamp_created": "reviewed_at"
    },
    // More review objects...
  ],
  "next_cursor": "cursor_value"
}
```

- `data`: An array of review objects.
- `author_id`: The Steam user's ID who wrote the review.
- `review`: The review comment.
- `timestamp_created`: The timestamp when the review was created.
- `next_cursor`: A cursor value for fetching the next set of reviews.

### Error Response

```json
{
  "error": "error_message"
}
```

- `error`: An error message describing the issue.

## Swagger UI

To explore the API documentation interactively, you can visit the Swagger UI page at `http://localhost:5000/swagger`. This page provides a user-friendly interface for understanding and testing the available endpoints.

## Approach
The approach for this is a pretty straight forward approach. I used the officail steam API to fetch the reviews for the PUBG Game. 
Here is the [link](https://partner.steamgames.com/doc/store/getreviews) to the official API documentation. The official documentation mentioned about all the request parameters and response details. So, I built the Flask API in appropriately to fetch the data and filtered the response data into a simple data and returned only the required data, `review`, `author_id` and `timestamp_created` in the response data along with the next cursor value to fetch the next set of review objects.

The Application implementation is as follows:
1. **Project Initialization:**
   - The project is initialized by creating a Flask application (`app.py`).
   - It also sets up logging to record server activities and errors.

2. **Configuration:**
   - Configuration settings, such as the base URL and app ID for PUBG on Steam are loaded from `.env` file and are consumed in `common/settings.py`.
   
3. **API Implementation:**
   - Two main API endpoints are implemented:
     - `/` (Home Page): A simple route to provide a greeting message.
     - `/reviews` (Get Reviews): An endpoint to fetch and return reviews for PUBG on Steam.
    - To fetch the initial set of review objects, the user can fetch the data using the url `http://localhost:5000/reviews`, returns 20 review objects by default.
    - To fetch the next set of objects, use the `next_cursor` value in the next response like `http://localhost:5000/reviews?cursor=<next_cursor>`. For initial request, the cursor value can be set to `*` like `http://localhost:5000/reviews?cursor=*`
   
4. **Swagger Documentation:**
   - Swagger UI is integrated into the project for easy API documentation and testing.
   - The Swagger UI page is made available at `/swagger`.

5. **Error Handling:**
   - Error handling is implemented to gracefully handle exceptions and provide meaningful error responses.

6. **Logging:**
   - Logging is set up to record server activities and errors in log files within the `common/logs/` directory.

7. **Dependencies:**
   - Required dependencies are specified in `requirements.txt` for easy installation.

8. **Usage Instructions:**
   - A README file is created to provide usage instructions, including prerequisites, installation steps, and details about API endpoints and responses.

9. **Server Launch:**
   - The Flask server is launched with `app.run()`.

## Challenges
The main challenge that I faced while developing the project is integrating Swagger UI.

1. **Swagger Integration:**
   - Integrating Swagger UI to document the API endpoints and make it user-friendly requires understanding Swagger's configuration. I want to give a clear schema about the request and response for the endpoints who are using our endpoints.

2. **API Integration:**
   - The first thing that I thought was Scrapping the data from their website but thankfully, they have provided an API to fetch the reviews based on the application.

3. **Documentation:**
   - Creating clear and comprehensive documentation in the README file is important for users of the API. Explaing the setup and installation process is more important.