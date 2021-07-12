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

Ответ сервера:
```buildoutcfg
root@vagrant:~/lesson6.5# curl http://127.0.0.1:9200
{
  "name" : "netology_test",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "GQvQ9l44QC-JhomTlUHbTw",
  "version" : {
    "number" : "7.13.3",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "5d21bea28db1e89ecc1f66311ebdec9dc3aa7d64",
    "build_date" : "2021-07-02T12:06:10.804015202Z",
    "build_snapshot" : false,
    "lucene_version" : "8.8.2",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}



```

Ссылка на образ:
```buildoutcfg
docker pull falconow/node_elasticsearch
```


### Задание 2
***
Создаем индексы: 
```buildoutcfg
root@vagrant:~/lesson6.5# curl -X PUT "localhost:9200/ind-1?pretty" -H 'Content-Type: application/json' -d'
{
  "settings": {
    "index": {
      "number_of_shards": 1,  
      "number_of_replicas": 0 
    }
  }
}
' 
{
  "acknowledged" : true,
  "shards_acknowledged" : true,
  "index" : "ind-1"
}
root@vagrant:~/lesson6.5# 
root@vagrant:~/lesson6.5# 
root@vagrant:~/lesson6.5# curl -X PUT "localhost:9200/ind-2?pretty" -H 'Content-Type: application/json' -d'
> {
>   "settings": {
>     "index": {
>       "number_of_shards": 2,  
>       "number_of_replicas": 1
>     }
>   }
> }
> '
{
  "acknowledged" : true,
  "shards_acknowledged" : true,
  "index" : "ind-2"
}
root@vagrant:~/lesson6.5# 
root@vagrant:~/lesson6.5# curl -X PUT "localhost:9200/ind-3?pretty" -H 'Content-Type: application/json' -d'
> {
>   "settings": {
>     "index": {
>       "number_of_shards": 4,  
>       "number_of_replicas": 2 
>     }
>   }
> }
> '
{
  "acknowledged" : true,
  "shards_acknowledged" : true,
  "index" : "ind-3"
}
root@vagrant:~/lesson6.5# 
```

Список индексов:
```buildoutcfg
root@vagrant:~/lesson6.5# curl localhost:9200/_cat/indices?v
health status index uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   ind-1 Afn_tGi8SWyaZ-xzSoAz3Q   1   0          0            0       208b           208b
yellow open   ind-3 K70vHBASTPyADflkLDz4KQ   4   2          0            0       832b           832b
yellow open   ind-2 ojiukN7LRQ2_LE-xNIJGSA   2   1          0            0       416b           416b
root@vagrant:~/lesson6.5# 

```

Статус кластера:
```buildoutcfg
root@vagrant:~/lesson6.5# curl -X GET "localhost:9200/_cluster/health?pretty"
{
  "cluster_name" : "elasticsearch",
  "status" : "yellow",
  "timed_out" : false,
  "number_of_nodes" : 1,
  "number_of_data_nodes" : 1,
  "active_primary_shards" : 7,
  "active_shards" : 7,
  "relocating_shards" : 0,
  "initializing_shards" : 0,
  "unassigned_shards" : 10,
  "delayed_unassigned_shards" : 0,
  "number_of_pending_tasks" : 0,
  "number_of_in_flight_fetch" : 0,
  "task_max_waiting_in_queue_millis" : 0,
  "active_shards_percent_as_number" : 41.17647058823529
}

```
> Думаю что статус "yellow" из-за того что реплики не настроенны

Удаляем индексы:
```buildoutcfg
root@vagrant:~/lesson6.5# curl -X DELETE "localhost:9200/_all"
{"acknowledged":true}
```

### Задание 3
***
Запустим контейнер с директорией snapshots:
```buildoutcfg
root@vagrant:~/lesson6.5# docker run --name test -p9200:9200 -d -v /root/lesson6.5/snapshots:/usr/local/elasticsearch/snapshots elasticsearch
```
