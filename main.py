import os
import requests
from flask import Flask, request, jsonify, make_response
from flasgger import Swagger, swag_from
from dotenv import load_dotenv
from swagger.config import swagger_config

load_dotenv()

app = Flask(__name__)
swagger = Swagger(app, config=swagger_config)

BILER_SERVICE_URL = os.getenv('BILER_SERVICE_URL')
AFTALER_SERVICE_URL = os.getenv('AFTALER_SERVICE_URL')
KUNDER_SERVICE_URL = os.getenv('KUNDER_SERVICE_URL')
SKADER_SERVICE_URL = os.getenv('SKADER_SERVICE_URL')


@app.route('/')
def index():
  return "Welcome to API"

@app.route('/skader', methods=['GET'])
@swag_from('swagger/get_skader.yml')
def get_skader():
    response = requests.get(f"{SKADER_SERVICE_URL}/skader")

    return make_response(response.json(), response.status_code)


@app.route('/skader', methods=['POST'])
@swag_from('swagger/post_skader.yml')
def create_skade():
   data = request.json

   response = requests.post(f"{SKADER_SERVICE_URL}/skader", json=data)

   return make_response(response.json(), response.status_code)


if __name__ == '__main__':
    app.run()
