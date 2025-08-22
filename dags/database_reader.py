"""
Database Reader DAG
Demonstrates reading data from a Firebase Firestore database collection
"""

from __future__ import annotations

import pendulum
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from db.config import client as db


def fetch_cities(**kwargs):
    collection = db.collection('cities')
    docs = collection.stream()
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')

with DAG(
    dag_id="database_reader",
    default_args={"retries": 0},
    description="Fetch city data from the database collection",
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["database", "firestore"],
) as dag:
    dag.doc_md = __doc__

    read_op = PythonOperator(
        task_id="fetch_cities",
        python_callable=fetch_cities,
    )

    read_op
