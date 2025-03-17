# Transaction-Processing-System
The Transaction Processing System (TPS) is a scalable and resilient system that handles high transaction volumes, performance, reliability, and operational visibility. 
The system is designed with a microservices architecture that can scale horizontally and automatically recover from failures.

## The TPS includes the following components:

- API Service - FastAPI - Exposes RESTful APIs for transaction management.

- Database - The system interacts with a relational database (PostgreSQL) to store transaction data.

- Caching - Uses Redis to cache transaction data and reduce database load.

- Prometheus Monitoring - Provides detailed metrics and monitoring of the application.

- Auto-Scaling - Kubernetes Horizontal Pod Autoscaler (HPA) automatically adjusts the number of pods based on CPU utilization.

- High Availability and Resilience - The system is designed for fault tolerance with features like rolling updates and pod disruption budgets.


## Prerequisites

1. **Docker and Docker Compose**: Ensure you have Docker and Docker Compose installed on your machine.
   - [Install Docker](https://docs.docker.com/engine/install/)
   - [Install Docker Compose](https://docs.docker.com/compose/install/)

    Alternatively you can Install [Docker Desktop](https://docs.docker.com/desktop/) which include both.

2. **Python 3.9+**: Ensure you have Python 3.9 or newer installed if you plan to run parts of the project outside of Docker.
   - [Install Python](https://www.python.org/downloads/)

## Project Structure

~~~
tps/
│── app/
│   │── __init__.py
│   │── main.py
│   │── models.py
│   │── database.py
│   │── transactions.py
│   │── schemas.py
│   │── cache.py
│   │── auth.py
│   │── worker.py
│── infra/
│   │── docker-compose.yml
│   │── k8s/
│   │   │── deployment.yaml
│   │   │── prometheus.yaml
│── requirements.txt
│── Dockerfile
│── README.md
~~~

## Setup Instructions

`git clone https://github.com/Yuda4/Transaction-Processing-System.git`

`cd Transaction-Processing-System`

1. Build and Start the Services:
    - Open a terminal on project-root location
    - Run the build command: `docker-compose up --build`
    - Want to delete the container with all data? Run this command: `docker-compose down -v`
    - Want to stop the running of container? `docker-compose stop` or press `Ctrl-C`
  
2. API's endpoints:

   After docker is running and all services are up run this CURL in the terminal or using Postman:
   
   POST: /transactions
      ~~~~
      curl --location 'http://localhost:8000/transactions' \
      --header 'Content-Type: application/json' \
      --data '{
          "user_id": "user_11",
          "amount": 12.75,
          "currency": "USD"
      }'
      ~~~~
      
   GET: /transactions/{txn_id}
      ~~~~
      curl --location 'http://localhost:8000/transactions/1'
      ~~~~
      
    GET: /metrics
      ~~~~
      curl --location 'http://localhost:8000/metrics'
      ~~~~
      
3. Connecting to DB:
   
    Open the terminal and use this command:

   `docker exec -it infra-db-1 psql -U user -d tps` which will connect to DB named tps that is hosted in `infra-db-1` docker container.

   `\l` - List all databases.
   
    `\dt` - List database tables.
   
    `\d <table-name>` - Describe a table.

    `SELECT * FROM transactions;` - shows **transactions** table's records.

Exmaple of records in table:

![Screenshot 2025-03-18 at 0 14 36](https://github.com/user-attachments/assets/9ba7a2c1-9c24-44dd-b089-63002957466b)

   
