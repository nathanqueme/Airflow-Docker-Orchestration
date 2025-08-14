"""
Database Reader DAG
Demonstrates reading data from a Firestore database collection
"""

from __future__ import annotations

import pendulum
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from db.config import client


def read_firestore_data(**kwargs):
    collection = client.collection('automation_catalog')
    docs = collection.stream()
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')

with DAG(
    dag_id="database_reader",
    default_args={"retries": 0},
    description="Read data from Firestore database collection",
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["database", "firestore"],
) as dag:
    dag.doc_md = __doc__

    read_op = PythonOperator(
        task_id="read_firestore_data",
        python_callable=read_firestore_data,
    )

    read_op
