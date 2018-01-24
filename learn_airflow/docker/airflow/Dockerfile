FROM puckel/docker-airflow:1.8.2

USER root
RUN apt-get update &&\
    apt-get install git -y

COPY airflow.cfg /usr/local/airflow/airflow.cfg

USER airflow
