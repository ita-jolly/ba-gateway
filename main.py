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
    endpoints = [
        {
            "path": "/apidocs",
            "method": "GET",
            "description": "Endpoint documentation"
        },
        {
            "path": "/skader",
            "method": "GET",
            "description": "Get skader"
        },
        {
            "path": "/skader",
            "method": "POST",
            "description": "Create skade"
        },
        {
            "path": "/aftaler",
            "method": "GET",
            "description": "Get all aftaler"
        },
        {
            "path": "/aftaler",
            "method": "POST",
            "description": "Create a new aftale"
        },
        {
            "path": "/kunder",
            "method": "GET",
            "description": "Get kunder"
        },
        {
            "path": "/kunder/<string:cpr>",
            "method": "GET",
            "description": "Get kunde by CPR"
        },
        {
            "path": "/kunder",
            "method": "POST",
            "description": "Create kunde"
        },
        {
            "path": "/biler",
            "method": "GET",
            "description": "Get biler"
        },
        {
            "path": "/biler/udlejet",
            "method": "GET",
            "description": "Get udlejet biler"
        },
        {
            "path": "/biler/udlejet/total",
            "method": "GET",
            "description": "Get total udlejet biler"
        }
    ]
    return jsonify({
        "Service": "ba-biler Microservice",
        "Available endpoints": endpoints
    })


###########
# SKADER  #
###########

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



###########
# AFTALER #
###########

@app.route('/aftaler', methods=['GET'])
@swag_from('swagger/get_aftaler.yml')
def get_aftaler():
    response = requests.get(f"{AFTALER_SERVICE_URL}/aftaler")
    return make_response(response.json(), response.status_code)


@app.route('/aftaler', methods=['POST'])
@swag_from('swagger/create_aftale.yml')
def create_aftale():
    data = request.json
    response = requests.post(f"{AFTALER_SERVICE_URL}/aftaler", json=data)
    return make_response(response.json(), response.status_code)



#################################
########### KUNDER ##############
#################################

@app.route('/kunder', methods=['GET'])
@swag_from('swagger/get_kunder.yml')
def get_kunder():
    response = requests.get(f"{KUNDER_SERVICE_URL}/kunder")
    return make_response(response.json(), response.status_code)

@app.route('/kunder/<string:cpr>', methods=['GET'])
@swag_from('swagger/get_kunde.yml')
def get_kunde(cpr):
    response = requests.get(f"{KUNDER_SERVICE_URL}/kunder/{cpr}")
    return make_response(response.json(), response.status_code)


@app.route('/kunder', methods=['POST'])
@swag_from('swagger/create_kunde.yml')
def create_kunde():
    data = request.json
    response = requests.post(f"{KUNDER_SERVICE_URL}/kunder", json=data)
    return make_response(response.json(), response.status_code)


#################################
########### BILER ##############
#################################

@app.route('/biler', methods=['GET'])
@swag_from('swagger/get_biler.yml')
def get_biler():
    response = requests.get(f"{BILER_SERVICE_URL}/biler")
    return make_response(response.json(), response.status_code)


@app.route('/biler/udlejet', methods=['GET'])
@swag_from('swagger/get_udlejet.yml')
def get_udlejet():
    response = requests.get(f"{BILER_SERVICE_URL}/biler/udlejet")
    return make_response(response.json(), response.status_code)

@app.route('/biler/udlejet/total', methods=['GET'])
@swag_from('swagger/get_udlejet_total.yml')
def get_udlejet_total():
    response = requests.get(f"{BILER_SERVICE_URL}/biler/udlejet/total")
    return make_response(response.json(), response.status_code)




if __name__ == '__main__':
    app.run()
