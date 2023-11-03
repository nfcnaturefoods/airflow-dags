from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "hello_world-1103125054",
}

dag = DAG(
    "hello_world-1103125054",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using hello_world.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_65d749ff_4c76_409a_9d28_d9e8dbd2b202 = NotebookOp(
    name="hello",
    namespace="ml-workshop",
    task_id="hello",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/hello.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="hello_world-1103125054",
    cos_dependencies_archive="hello-65d749ff-4c76-409a-9d28-d9e8dbd2b202.tar.gz",
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

notebook_op_65d749ff_4c76_409a_9d28_d9e8dbd2b202.image_pull_policy = "IfNotPresent"


notebook_op_7f8a80ad_35f0_436e_a7dd_d2d1b5e9205d = NotebookOp(
    name="world",
    namespace="ml-workshop",
    task_id="world",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/world.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="hello_world-1103125054",
    cos_dependencies_archive="world-7f8a80ad-35f0-436e-a7dd-d2d1b5e9205d.tar.gz",
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

notebook_op_7f8a80ad_35f0_436e_a7dd_d2d1b5e9205d.image_pull_policy = "IfNotPresent"

(
    notebook_op_7f8a80ad_35f0_436e_a7dd_d2d1b5e9205d
    << notebook_op_65d749ff_4c76_409a_9d28_d9e8dbd2b202
)
