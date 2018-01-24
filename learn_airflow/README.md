docker pull puckel/docker-airflow
docker run -d -p 8080:8080 puckel/docker-airflow

docker-compose -f docker-compose-local_executor.yml up -d