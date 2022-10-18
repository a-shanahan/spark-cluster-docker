# Sentiment Analysis with Spark Streaming

## Overview

A simple network integrating Spark Streaming with Kafka. This configuration has been tested 
on Apple M2 silicon. 

This example scrapes the BBC news website for the Top 10 news articles and publishes the content to a 
Kafka topic. Spark Streaming monitors this topic and uses TextBlob to perform sentiment analysis on the 
content. The results are then published to a different topic. 


The docker compose will create the following containers:

container|Exposed ports
---|---
spark-master|9090
spark-worker-a|9091
spark-worker-b|9092
kafka|29092
zookeeper|22181

## Installation
The following steps will set up the network and generate example data:

### Pre-requisites
- Docker
- Docker-compose

### Docker compose
To run the network in detached mode use the ```-d```flag at the end of the command:  
```shell
docker-compose up
```

## Validate setup

To validate the setup of the cluster example producer and consumer [scripts](kafka-examples) have been provided. 
Install the virtual environment and run both scripts in separate terminal windows.

```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 <name of file>
```

## Spark Streaming
The Spark script is copied to the master node during start up along with a cron job that executes the script. 
This has been done for local testing so that the streaming job does not hog all the cluster resources. A script 
is executed on start up which starts the cluster. A spark installation file is provided, a different version can be 
obtained using:

```shell
PARK_VERSION=3.3.0
HADOOP_VERSION=3
wget --no-verbose -O apache-spark.tgz "https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" \
```

### Website scraping
The BBC news website is the target for content scraping. The News homepage is scraped for the Top 10 news links which 
are then iterated through and the article content extracted. 