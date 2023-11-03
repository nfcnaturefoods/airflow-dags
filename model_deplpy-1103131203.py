from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "model_deplpy-1103131203",
}

dag = DAG(
    "model_deplpy-1103131203",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using model_deplpy.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_7c6edf65_9df7_48d5_9626_000791411e30 = NotebookOp(
    name="build_push_image",
    namespace="ml-workshop",
    task_id="build_push_image",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/model_build_push/build_push_image.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="model_deplpy-1103131203",
    cos_dependencies_archive="build_push_image-7c6edf65-9df7-48d5-9626-000791411e30.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-on-k8s/kaniko-container-builder:1.0.0",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "MODEL_NAME": "mlflowdemo",
        "MODEL_VERSION": "1",
    },
    config_file="None",
    dag=dag,
)

notebook_op_7c6edf65_9df7_48d5_9626_000791411e30.image_pull_policy = "IfNotPresent"


notebook_op_9f32ea55_d107_4554_a497_a733b68e1e36 = NotebookOp(
    name="deploy_model",
    namespace="ml-workshop",
    task_id="deploy_model",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/model_deploy/deploy_model.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="model_deplpy-1103131203",
    cos_dependencies_archive="deploy_model-9f32ea55-d107-4554-a497-a733b68e1e36.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-on-k8s/airflow-python-runner:0.0.11",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "MODEL_NAME": "mlflowdemo",
        "MODEL_VERSION": "1",
        "CLUSTER_DOMAIN_NAME": "192.168.49.2.nip.io",
    },
    config_file="None",
    dag=dag,
)

notebook_op_9f32ea55_d107_4554_a497_a733b68e1e36.image_pull_policy = "IfNotPresent"

(
    notebook_op_9f32ea55_d107_4554_a497_a733b68e1e36
    << notebook_op_7c6edf65_9df7_48d5_9626_000791411e30
)
