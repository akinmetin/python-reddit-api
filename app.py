
'''
This module includes the create_app() function that
returns the Flask API Server with predefined endpoints
'''
import os
from flask import Flask, jsonify, request
from utils import (
    url_validator,
    get_reddit_data,
    find_top_five_post_titles,
)


def create_app():
    '''
    Initializes Flask app and necessary class objects
    Defines API endpoints and allowed request types
    :return: Flask API server
    '''
    app = Flask(__name__)

    @app.route("/posts/top", methods=['GET'])
    def get_top_five_posts():
        '''
        Endpoint that returns the top 5 post titles
        according to the provided paramater 'url'
        '''

        # check URL validation
        if not url_validator(request.args.get("url")):
            response = jsonify({"error": "please check the URL"})
            return response, 400

        # prepare the URL for Reddit
        if request.args.get("url")[-1] == "/":
            url = request.args.get("url") + ".json"
        else:
            url = request.args.get("url") + "/.json"

        # get the JSON output from Reddit
        data = get_reddit_data(url)

        # filter top 5 posts based on scores
        top_posts = find_top_five_post_titles(data)

        # convert the result into JSON
        response = jsonify(top_posts)
        return response

    return app


if __name__ == '__main__':  # pragma: no cover
    app = create_app()

    if os.environ['DEBUG_MODE'] == '1':
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        app.run()
