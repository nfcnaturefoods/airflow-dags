from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "model_deploy-1121145932",
}

dag = DAG(
    "model_deploy-1121145932",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using model_deploy.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_6bee7f2d_b076_470d_82f9_958dab70218f = NotebookOp(
    name="build_push_image",
    namespace="ml-workshop",
    task_id="build_push_image",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/model_build_push/build_push_image.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="model_deploy-1121145932",
    cos_dependencies_archive="build_push_image-6bee7f2d-b076-470d-82f9-958dab70218f.tar.gz",
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
        "CONTAINER_REGISTRY": "index.docker.io/v1",
        "CONTAINER_REGISTRY_USER": "hebum2",
        "CONTAINER_REGISTRY_PASSWORD": "Svl@12345",
        "CONTAINER_DETAILS": "hebum2/mlflowdemo:latest",
    },
    config_file="None",
    dag=dag,
)

notebook_op_6bee7f2d_b076_470d_82f9_958dab70218f.image_pull_policy = "IfNotPresent"
