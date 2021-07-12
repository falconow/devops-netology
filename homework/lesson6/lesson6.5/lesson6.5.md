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
> Поправил конфиг elaticsearch.yml, добавил в него параметр: 
> > echo "path.repo: /usr/local/elasticsearch/snapshots/" >> ./config/elasticsearch.yml
> 
> Перезапускаем контейнер
> 
Зарегистрируем директорию snapshot repository:
```buildoutcfg
root@vagrant:~/test# curl -X PUT "localhost:9200/_snapshot/netology_backup?pretty" -H 'Content-Type: application/json' -d'
> {
>   "type": "fs",
>   "settings": {
>     "location": "/usr/local/elasticsearch/snapshots/"
>   }
> }
> '
{
  "acknowledged" : true
}
root@vagrant:~/test# 
```

Создаем индекс test:
```buildoutcfg
root@vagrant:~/test# curl -X PUT "localhost:9200/test?pretty" -H 'Content-Type: application/json' -d'
> {
>   "settings": {
>     "index": {
>       "number_of_shards": 1,  
>       "number_of_replicas": 0 
>     }
>   }
> }
> '
{
  "acknowledged" : true,
  "shards_acknowledged" : true,
  "index" : "test"
}

```

Список индексов:
```buildoutcfg
root@vagrant:~/test# curl localhost:9200/_cat/indices?v
health status index uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   test  g473plJuQZOOq9pdWh2OwA   1   0          0            0       208b           208b
root@vagrant:~/test# 

```

Создаем snapshot:
```buildoutcfg
root@vagrant:~/test# curl -X PUT "localhost:9200/_snapshot/netology_backup/snapshot_1?wait_for_completion=true&pretty"
{
  "snapshot" : {
    "snapshot" : "snapshot_1",
    "uuid" : "ng8uUO5QToWkzBncD0rVNw",
    "version_id" : 7130399,
    "version" : "7.13.3",
    "indices" : [
      "test"
    ],
    "data_streams" : [ ],
    "include_global_state" : true,
    "state" : "SUCCESS",
    "start_time" : "2021-07-12T16:51:25.188Z",
    "start_time_in_millis" : 1626108685188,
    "end_time" : "2021-07-12T16:51:25.394Z",
    "end_time_in_millis" : 1626108685394,
    "duration_in_millis" : 206,
    "failures" : [ ],
    "shards" : {
      "total" : 1,
      "failed" : 0,
      "successful" : 1
    },
    "feature_states" : [ ]
  }
}
root@vagrant:~/test# 

```

Cписок файлов в директории со snapshotами:
```buildoutcfg
[elasticsearch@b160db3e8615 elasticsearch]$ ls -l /usr/local/elasticsearch/snapshots/
total 44
-rw-r--r-- 1 elasticsearch elasticsearch   505 Jul 12 16:51 index-0
-rw-r--r-- 1 elasticsearch elasticsearch     8 Jul 12 16:51 index.latest
drwxr-xr-x 3 elasticsearch elasticsearch  4096 Jul 12 16:51 indices
-rw-r--r-- 1 elasticsearch elasticsearch 25553 Jul 12 16:51 meta-ng8uUO5QToWkzBncD0rVNw.dat
-rw-r--r-- 1 elasticsearch elasticsearch   360 Jul 12 16:51 snap-ng8uUO5QToWkzBncD0rVNw.dat
[elasticsearch@b160db3e8615 elasticsearch]$ 

```

Удаляем индекс test:
```buildoutcfg
[elasticsearch@b160db3e8615 elasticsearch]$ curl -X DELETE "localhost:9200/test?pretty"
{
  "acknowledged" : true
}
[elasticsearch@b160db3e8615 elasticsearch]$
```

Создаем индекс  test2:
```buildoutcfg
root@vagrant:~# curl -X PUT "localhost:9200/test2?pretty" -H 'Content-Type: application/json' -d'
> {
>   "settings": {
>     "index": {
>       "number_of_shards": 1,  
>       "number_of_replicas": 0 
>     }
>   }
> }
> '
{
  "acknowledged" : true,
  "shards_acknowledged" : true,
  "index" : "test2"
}
root@vagrant:~# 


```

Список всех индексов:
```buildoutcfg
root@vagrant:~# curl localhost:9200/_cat/indices?v
health status index uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   test2 s-XhD3niSa-cEbwQB9d65A   1   0          0            0       208b           208b
root@vagrant:~# 
```

Восстанавливаемся из snapshot_1:
```buildoutcfg
root@vagrant:~# curl -X POST "localhost:9200/_snapshot/netology_backup/snapshot_1/_restore?pretty"
{
  "accepted" : true
}
root@vagrant:~#
```

Смотрим итоговый список индексов:
```buildoutcfg
root@vagrant:~# curl localhost:9200/_cat/indices?v
health status index uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   test2 s-XhD3niSa-cEbwQB9d65A   1   0          0            0       208b           208b
green  open   test  XTjtvsPOQeK9gbPz7mXdGQ   1   0          0            0       208b           208b
root@vagrant:~# 

```

