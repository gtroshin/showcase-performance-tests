# Showcase Performance Tests
![Python 3.9.1](https://img.shields.io/badge/Python-3.9.1-green.svg)
![Locust 2.10.1](https://img.shields.io/badge/Locust-2.10.1-purple.svg)

This project is designed to run performance tests using Locust framework against the services with a following profile:

Number of users (peak concurrency): 4 \
Spawn rate (users started/second): 10

All the performance test information is available at the inbuilt Locust charts and at [custom Grafana dashboard](http://localhost:3000/d/0WllLp6mq/locust-test).

## Requirements

* Docker
* Python 3.9.1+

## Development

To start all the services, run the following command in project root folder:

    docker-compose up

## Services and addresses

| Service          | Address                       | Description                          |
|------------------|-------------------------------|--------------------------------------|
| Locust           | http://localhost:8089         | Load testing tool                    |
| Exported Metrics | http://localhost:9646/metrics | Locust metrics exporter              |
| Prometheus       | http://localhost:9090         | Data source for Grafana              |
| Grafana          | http://localhost:3000         | Visualization and observability tool |
