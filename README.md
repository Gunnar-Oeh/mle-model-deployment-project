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
### Train a model
- Created a notebook to [01_train_model.ipynb](./01_train_model.ipynb) to train a RandomForestRegressor after doing a RandomizedSearchCV with 1/3 of the data for faster training
- Trained the model and uploaded it to the mlflow-server running on a GC-Engine

### Spin up an FastAPI-APP locally
- Organized the preprocessing and prediction functions (with load_model() from mlflow) in the script [predict.py](webservice_locally/predict.py)
- prediction function from [predict.py](webservice_locally/predict.py) and data-models (pydantic) from [data_model.py](webservice_locally/data_model.py) is called in the post-request in the Fast-API app in [app.py](webservice_locally/app.py)
- Called the following command to start the app
  ```bash
cd webservice_locally                                                                        
uvicorn app:app --reload --port 9696
  ```
- Made a request in the FastAPI-Webinterface:
![image](https://github.com/Gunnar-Oeh/mle-model-deployment-project/assets/121675093/5d74f6e3-401a-4e03-b4d6-d25a03502b84)
