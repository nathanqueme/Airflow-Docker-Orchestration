# Airflow Orchestration

#### Steps to configure Airflow locally on your computer with Docker
1. Build the docker image
```docker-compose build```

2. Start Airflow services
Run this the first time only
```docker-compose up airflow-init```

Run this after initialization
```docker-compose up```

3. Check which containers are running
```docker ps```

4. After a few minute(s), navigate to http://localhost:8080

5. Login with the username/password: `airflow/airflow`


#### Useful commands
1. Using the Airflow CLI
```docker exec <Container ID> <Command>```
For instance to list the current dags run:
```docker exec efg123 airflow dags list```
To list dags which aren't part of the UI run:
```docker exec efg123 airflow dags list-import-errors```

2. Using the Airflow API
```curl -X GET --user "<username>:<password>" "<endpoint>"```
For instance to get the list of dags:
```curl -X GET --user "airflow:airflow" "http://localhost:8080/api/v1/dags"```
