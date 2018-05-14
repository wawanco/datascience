docker build -t airflow .
docker run -d -p 8080:8080 airflow

To see running container
docker ps

Run a command inside the running container
docker exec -it 3d7160de5c4f ls

docker kill <container_id>

# Airflow Concepts

* DAG: a description of the order in which work should take place
* Operator: a class that acts as a template for carrying out some work
* Task: a parameterized instance of an operator
* Task Instance: a task that
 * has been assigned to a DAG
  * has a state associated (`running`, `success`, `failed`, `skipped`, `up for retry`, ...)
  * has a specific run of the DAG
