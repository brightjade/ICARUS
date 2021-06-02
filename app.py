from flask import Flask, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
import logging
import secrets
import json

from api.recommend import extract_topk_papers

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create handlers for logging to stream(console) and file
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('server.log')

stream_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')

stream_handler.setFormatter(stream_formatter)
file_handler.setFormatter(file_formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

# Initiate Flask
app = Flask(__name__, static_url_path='', static_folder='web/build')
app.secret_key = secrets.token_bytes(32)
CORS(app)     # turn this off in production.

@app.route('/ping')
def ping():
    logger.info("ping success")
    return {'success': "Success!"}


@app.route('/recommend_papers', methods=['POST'])
def recommend_papers():
    logger.info('Recommending Papers')
    K = request.json.get('K')
    user_input = request.json.get('userInput')
    query_coordinates, topk_papers = extract_topk_papers(user_input, K)
    concat_results = [query_coordinates] + topk_papers
    return json.dumps(concat_results)
    

if __name__ == '__main__':
    logger.info('Starting Flask API Server.')
    app.run(host="0.0.0.0", port=8080, debug=True)
