# ba-gateway

## Overview

This README provides the necessary information to set up, configure, and use the microservice. It includes details about environmental variables, API endpoints, and dependencies.

The service can be accesed here: https://ba-gateway-e5bxdghpa2ayf3fk.northeurope-01.azurewebsites.net/apidocs

---
## Relevant Links
Below is a list of  relevant links:
### Github repos
* [ba-kunder microservice](https://github.com/ita-jolly/ba-kunder)
* [ba-biler microservice](https://github.com/ita-jolly/ba-biler)
* [ba-skader  microservice](https://github.com/ita-jolly/ba-skader)
* [ba-aftaler microservice](https://github.com/ita-jolly/ba-aftaler)

### Azure App URLs
* [ba-gateway microservice](https://ba-gateway-e5bxdghpa2ayf3fk.northeurope-01.azurewebsites.net/)
* [ba-kunder microservice](https://ba-kunder-auc6hdhuejg4hnfr.northeurope-01.azurewebsites.net/)
* [ba-biler microservice](https://ba-biler-hagae6gdgacvafaf.northeurope-01.azurewebsites.net/)
* [ba-aftaler microservice](https://ba-aftaler-asathva5fdfscgb5.northeurope-01.azurewebsites.net/)
* [ba-skader microservice](https://ba-skader-euanhqfffdage0as.northeurope-01.azurewebsites.net/)

### DockerHub Repositories
* [ba-gateway microservice](https://hub.docker.com/r/daidalost/ba-gateway)
* [ba-kunder microservice](https://hub.docker.com/r/daidalost/ba-kunder)
* [ba-biler microservice](https://hub.docker.com/r/sushigirrl/ba-biler)
* [ba-skader microservice](https://hub.docker.com/r/diadalost/ba-skader)
* [ba-aftaler microservice](https://hub.docker.com/r/sushigirrl/ba-aftaler)

---

## Environment Variables
| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `BILER_SERVICE_URL` | Yes | - | Path to the Biler microservice URL |
|`AFTALER_SERVICE_URL`|Yes|-|Path to the Aftaler microservice URL|
|`KUNDER_SERVICE_URL`|Yes|-|Path to the Kunder microservice URL|
|`SKADER_SERVICE_URL`|Yes|-|Path to the Skader microservice URL|

---

## API Endpoints

Below is a list of the API endpoints exposed by this microservice. Each endpoint includes the HTTP method, a brief description, possible status codes, and the returned data.

### Endpoints

| Path             | Method | Description                          | Status Codes   | Response                                                                                     |
|------------------|--------|--------------------------------------|----------------|---------------------------------------------------------------------------------------------|
| `/skader`        | GET   | Retrieve a list of all damages | 200, 404       | Array of objects each containing `skade_id`, `skade_type`, `skade_pris`, `nummerplade`, `syn_type` and `indberetnings_dato` or error message explaining failure.|
| `/skader`        | POST    | Create a new damage         | 201, 400       | Object with `skade_id`, `skade_type`, `skade_pris`, `nummerplade`, `syn_type` and `indberetnings_dato` or error message explaining failure.|
| `/aftaler`     | GET        | Retrieves a list of all aftaler stored in the database. | 200, 404  | Array of objects each containing `aftale_id`, `cpr`, `nummerplade`, `aftale_type`, `start_dato` and `slut_dato` or error message explaining failure. |
| `/aftaler`     | POST       | Creates a new aftale in the database after validating data with external microservices. | 201, 400, 404, 409, 500  | Object containing `aftale_id`, `cpr`, `nummerplade`, `aftale_type`, `start_dato` and `slut_dato` or error message explaining failure. |
| `/kunder`        | POST   | Create a new customer                | 201, 400       | Object with `cpr`, `navn`, `tlf`, `email`, and `adresse` or error message explaining failure.|
| `/kunder/<cpr>`  | GET    | Retrieve a specific customer by CPR  | 200, 400, 404  | Object with `cpr`, `navn`, `tlf`, `email`, `adresse` or error message explaining failure.    |
| `/kunder`        | GET    | Retrieve a list of customers         | 200, 404       | Array of objects each containing `cpr`, `navn`, `tlf`, `email`, and `adresse` or error message explaining failure.|
| `/biler`              | GET    | Get all cars                     | 200, 404, 500  | Array of objects with `nummerplade`, `maerke`, and `abonnement_pris`. |
| `/biler/udlejet`      | GET    | Get all rented cars              | 200, 404, 500  | Array of objects with `nummerplade`, `maerke`, and `abonnement_pris`. |
| `/biler/udlejet/total`| GET    | Get total price for udlejet      | 200, 404, 500  | Object with `total` as an integer.                     |


---
## Dependencies

The following dependencies are required to run the microservice. These are specified in the `requirements.txt` file.

---
