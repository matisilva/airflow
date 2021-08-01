"""
# My DAG doc

## Just a dummy subtitle checking MD format

- Bash step
- Bash step
- Python step
"""
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonVirtualenvOperator
from airflow.utils.dates import days_ago
from defaults import default_args
from external.dummy_module import airflow_entrypoint


with DAG(
    'my_DAG',
    default_args=default_args,
    description='A simple dummy DAG',
    schedule_interval=timedelta(hours=1),
    catchup=False,
    start_date=days_ago(0),
    tags=['sample'],
) as dag:
    dag.doc_md = __doc__

    bash_task = BashOperator(
        task_id='bash.date',
        bash_command='date',
    )

    bash_sleep = BashOperator(
        task_id='bash.sleep',
        depends_on_past=False,
        bash_command='sleep 5',
        retries=3,
    )

    python_task = PythonVirtualenvOperator(
        task_id="python.task",
        python_callable=airflow_entrypoint.callable,
        requirements=airflow_entrypoint.requirements,
        system_site_packages=True,
        op_kwargs={
            'argument': "FIRST ARGUMENT"
        },
    )

    bash_task >> [bash_sleep, python_task]
