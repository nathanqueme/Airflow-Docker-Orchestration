# Airflow Data Orchestration

This repository contains **three example DAGs** for running orchestrated workflows that interact with databases and APIs using **Apache Airflow** on Docker. These examples demonstrate different data engineering patterns commonly used in production environments.

## Available DAGs

- **[ETL Pipeline](./dags/etl_pipeline.py)** - Classic Extract, Transform, Load workflow demonstrating data processing operations
- **[Database Reader](./dags/database_reader.py)** - Simple database connection and data retrieval from Firestore  
- **[API Database Workflow](./dags/api_database_workflow.py)** - Advanced workflow combining database operations, API calls, and conditional branching

These examples also demonstrate **XCom integration** using `xcom_push()` and `xcom_pull()` for passing data between tasks in Airflow workflows.

## Getting Started

### Prerequisites
- At least 4GB RAM and 10GB disk space

### Quick Setup

1. **Build the Docker image**
   ```bash
   docker-compose build
   ```

2. **Initialize Airflow** (first time only)
   ```bash
   docker-compose up airflow-init
   ```

3. **Start all services**
   ```bash
   docker-compose up
   ```

4. **Access the web interface**
   - Navigate to [http://localhost:8080](http://localhost:8080)
   - Login with: `airflow` / `airflow`

### Verify Installation

Check running containers:
```bash
docker ps
```

## Useful Commands

### Airflow CLI Operations
```bash
# List all DAGs
docker exec <container_id> airflow dags list

# Check for DAG import errors
docker exec <container_id> airflow dags list-import-errors

# Test a specific task
docker exec <container_id> airflow tasks test <dag_id> <task_id> <execution_date>
```

### Airflow REST API
```bash
# Get all DAGs
curl -X GET --user "airflow:airflow" "http://localhost:8080/api/v1/dags"

# Trigger a DAG run
curl -X POST --user "airflow:airflow" "http://localhost:8080/api/v1/dags/<dag_id>/dagRuns" \
  -H "Content-Type: application/json" \
  -d '{"conf": {}}'
```

## Architecture

This setup includes:
- **Airflow Webserver** (port 8080) - Web UI and API
- **Airflow Scheduler** - Task scheduling and execution
- **Airflow Worker** - Task execution (Celery)
- **PostgreSQL** - Metadata database
- **Redis** - Message broker for Celery

## License

Licensed under the Apache License 2.0 - see [LICENSE](LICENSE) for details.
