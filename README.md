# Model deployment project

Please do not fork this repository, but use this repository as a template for your refactoring project. Make Pull Requests to your own repository even if you work alone and mark the checkboxes with an x, if you are done with a topic in the pull request message.

## Project for today
The task for today you can find in the [project-description.md](project-description.md) file.

## Environment

```bash
pyenv local 3.11.3
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

## Steps of the Project
### Starting the mlflow-server
- start the PostgreSQL-DB 'mlflow-metadata-store' for the mlflow-server on GCP-SQL
- start the connected GC-Compute-Engine VM-Instance 'instance-1mlflow-tracking-server'
- Restart the MLFLOW server on 'instance-1mlflow-tracking-server' with:
```bash
source mlflow/bin/activate
mlflow server  -h 0.0.0.0  -p 5000  --backend-store-uri postgresql://<db_user>:<db_password>@<db_private_ip_address>:5432/<db_name>  --default-artifact-root gs://<gcs_bucket_name>/artifacts
```