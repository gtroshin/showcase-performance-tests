# Showcase Performance Tests
![Python 3.9.1](https://img.shields.io/badge/Python-3.9.1-green.svg)
![Locust 2.10.1](https://img.shields.io/badge/Locust-2.10.1-purple.svg)

## Requirements

* Docker
* Python 3.9.1+

## Development

To start all the services, run the following command in project root folder:

    docker-compose up

## Services

* Locust - http://localhost:8089
* Exported Metrics - http://localhost:9646/metrics
* Prometheus - http://localhost:9090
* Grafana - http://localhost:3000
