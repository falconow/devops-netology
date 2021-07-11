### Задание 1
***
Dockerfile
```buildoutcfg
FROM centos:7
RUN yum -y update && \
    yum install -y java-1.8.0-openjdk && \
    yum install -y wget
WORKDIR /tmp/
RUN wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.13.3-linux-x86_64.tar.gz
WORKDIR /usr/local/elasticsearch/
RUN tar -C /usr/local/elasticsearch/ -xzf /tmp/elasticsearch-7.13.3-linux-x86_64.tar.gz --strip-components 1
RUN echo "network.host: 0.0.0.0" >> /usr/local/elasticsearch/config/elasticsearch.yml
RUN echo "path.data: /var/lib" >> /usr/local/elasticsearch/config/elasticsearch.yml
RUN echo "node.name: netology_test" >> /usr/local/elasticsearch/config/elasticsearch.yml
RUN echo "discovery.type: single-node" >> /usr/local/elasticsearch/config/elasticsearch.yml
RUN chmod 777 /var/lib
EXPOSE 9200
EXPOSE 9300
RUN groupadd elasticsearch && \
    useradd elasticsearch -g elasticsearch -p elasticsearch && \
    chown -R elasticsearch:elasticsearch /usr/local/elasticsearch/
USER elasticsearch
ENTRYPOINT ["./bin/elasticsearch"]
```