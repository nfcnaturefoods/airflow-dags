from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "hello_world-1121103855",
}

dag = DAG(
    "hello_world-1121103855",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using hello_world.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_3deafd9e_5f84_401b_a634_04e6b96588c3 = NotebookOp(
    name="hello",
    namespace="ml-workshop",
    task_id="hello",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/hello.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="hello_world-1121103855",
    cos_dependencies_archive="hello-3deafd9e-5f84-401b-a634-04e6b96588c3.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-on-k8s/kaniko-container-builder:1.0.0",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_3deafd9e_5f84_401b_a634_04e6b96588c3.image_pull_policy = "IfNotPresent"


notebook_op_197c814c_c8e7_44dc_a5ee_77ea72d3ce33 = NotebookOp(
    name="world",
    namespace="ml-workshop",
    task_id="world",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/world.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="hello_world-1121103855",
    cos_dependencies_archive="world-197c814c-c8e7-44dc-a5ee-77ea72d3ce33.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-on-k8s/airflow-python-runner:0.0.11",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_197c814c_c8e7_44dc_a5ee_77ea72d3ce33.image_pull_policy = "IfNotPresent"

(
    notebook_op_197c814c_c8e7_44dc_a5ee_77ea72d3ce33
    << notebook_op_3deafd9e_5f84_401b_a634_04e6b96588c3
)
