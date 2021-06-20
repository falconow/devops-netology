### Задание 1
> К сожалению знаком не со всеми вариантами программ, могу в чем-то ошибиться
>- Высоконагруженное монолитное java веб-приложение:
>>В данном случае использовал бы виртуальную машину, чтобы было проще полностью управлять ресурсами, 
>>которые
>> необходимы для работы приложения
>- Go-микросервис для генерации отчетов:
>> Здесь можно использовать контейнер
>- Nodejs веб-приложение:
> >Также можно использовать контейнер, либо виртуалку
> - Мобильное приложение c версиями для Android и iOS
> > Использовал бы контейнер
> - База данных postgresql используемая, как кэш:
> > Использовал бы виртуалку, так как база используется как кэш. 
> > А в целом считаю что базы данных должны быть максимально надежными,
> > и должны работать с железом напрямую.
> - Шина данных на базе Apache Kafka:
> > В данном случае использовал бы отдельную виртуальную машину
> - Очередь для Logstash на базе Redis:
> > Здесь тоже бы использовал отдельную виртуалку 
> - Elastic stack для реализации логирования продуктивного веб-приложения - три ноды elasticsearch, два logstash и две ноды kibana:
> > Система работает с большим количеством данных, использовал бы либо физический сервер, либо виртуалку
> - Мониторинг-стек на базе prometheus и grafana:
> > Установил бы на виртуалку
> - Mongodb, как основное хранилище данных для java-приложения:
> > По возможности использовал бы физический сервер, т.к. это основная база данных, 
> > но если ресурсов не так много то можно и виртуалку поднять.
> - Jenkins-сервер:
> > Использовал бы контейнер


### Задание 2



### Задание 3

> Загрузим образы centos и debian:
 ```buildoutcfg
root@vagrant:~# docker pull centos
Using default tag: latest
latest: Pulling from library/centos
7a0437f04f83: Pull complete 
Digest: sha256:5528e8b1b1719d34604c87e11dcd1c0a20bedf46e83b5632cdeac91b8c04efc1
Status: Downloaded newer image for centos:latest
docker.io/library/centos:latest
root@vagrant:~# docker pull debian
Using default tag: latest
latest: Pulling from library/debian
d960726af2be: Pull complete 
Digest: sha256:acf7795dc91df17e10effee064bd229580a9c34213b4dba578d64768af5d8c51
Status: Downloaded newer image for debian:latest
docker.io/library/debian:latest
root@vagrant:~# docker images
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
debian       latest    4a7a1f401734   5 weeks ago    114MB
centos       latest    300e315adb2f   6 months ago   209MB
root@vagrant:~# 
```
> Создадим директорию info на хосте:
 ```buildoutcfg
root@vagrant:~# mkdir info
root@vagrant:~# ls -l
total 4
drwxr-xr-x 2 root root 4096 Jun 20 16:05 info
root@vagrant:~# 
```

> Запустим контейнеры с образами centos и debian c подключенной директорией info:
```buildoutcfg
root@vagrant:/etc# docker run -v /root/info/:/share/info --name centos -d -ti centos
root@vagrant:/etc# docker run -v /root/info/:/info --name debian -d -ti debian
root@vagrant:/etc# docker ps -a
CONTAINER ID   IMAGE     COMMAND       CREATED              STATUS              PORTS     NAMES
b8629058f1af   debian    "bash"        20 seconds ago       Up 20 seconds                 debian
94d4a6466127   centos    "/bin/bash"   About a minute ago   Up About a minute             centos
```
> Создадим файл в директории info в контейнере centos:
```buildoutcfg
root@vagrant:~# docker exec -ti centos bash
[root@94d4a6466127 /]# echo "This text in centos!" > /share/info/centos.txt
[root@94d4a6466127 /]# ls -l /share/info/
total 4
-rw-r--r-- 1 root root 21 Jun 20 17:34 centos.txt
[root@94d4a6466127 /]# cat /share/info/centos.txt 
This text in centos!
[root@94d4a6466127 /]# 
```
> Добавим файл в папку info на хосте:
```buildoutcfg
root@vagrant:~# cd ./info/
root@vagrant:~/info# ls -l
total 4
-rw-r--r-- 1 root root 21 Jun 20 17:34 centos.txt
root@vagrant:~/info# echo "This text in host!" > host.txt
root@vagrant:~/info# ls -l
total 8
-rw-r--r-- 1 root root 21 Jun 20 17:34 centos.txt
-rw-r--r-- 1 root root 19 Jun 20 17:37 host.txt
root@vagrant:~/info# cat host.txt 
This text in host!
root@vagrant:~/info# 
```

> Смотрим второй контейнер:
```buildoutcfg
root@vagrant:~# docker exec -ti debian bash
root@b8629058f1af:/# ls -l /info
total 8
-rw-r--r-- 1 root root 21 Jun 20 17:34 centos.txt
-rw-r--r-- 1 root root 19 Jun 20 17:37 host.txt
root@b8629058f1af:/# cat /info/centos.txt 
This text in centos!
root@b8629058f1af:/# cat info/host.txt 
This text in host!
root@b8629058f1af:/# 
```
> Из всего этого видно что оба контейнера используют одну директорию на хосте


