"""
### ETL Pipeline DAG
Extract, Transform, and Load data workflow demonstrating basic ETL operations
"""

from __future__ import annotations

import json, pendulum

from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator

with DAG(
    dag_id="etl_pipeline",
    default_args={"retries": 2},
    description="ETL Pipeline demonstrating Extract, Transform, Load operations",
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["etl", "example"],
) as dag:
    dag.doc_md = __doc__

    def extract(**kwargs):
        ti = kwargs["ti"]
        data_string = '{"1001": 301.27, "1002": 433.21, "1003": 502.22}'
        ti.xcom_push("order_data", data_string)

    def transform(**kwargs):
        ti = kwargs["ti"]
        extract_data_string = ti.xcom_pull(task_ids="extract", key="order_data")
        order_data = json.loads(extract_data_string)

        total_order_value = 0
        for value in order_data.values():
            total_order_value += value

        total_value = {"total_order_value": total_order_value}
        total_value_json_string = json.dumps(total_value)
        ti.xcom_push("total_order_value", total_value_json_string)

    def load(**kwargs):
        ti = kwargs["ti"]
        total_value_string = ti.xcom_pull(task_ids="transform", key="total_order_value")
        total_order_value = json.loads(total_value_string)
        print(total_order_value)

    extract_op = PythonOperator(
        task_id="extract",
        python_callable=extract,
    )

    transform_op = PythonOperator(
        task_id="transform",
        python_callable=transform,
    )

    load_op = PythonOperator(
        task_id="load",
        python_callable=load,
    )

    extract_op >> transform_op >> load_op
