FROM puckel/docker-airflow:1.8.2

USER root
RUN apt-get update &&\
    apt-get install git -y

# Make port 80 available to the world outside this container
EXPOSE 8080

COPY dags/ /usr/local/airflow/dags/
COPY airflow.cfg /usr/local/airflow/airflow.cfg

USER airflow
