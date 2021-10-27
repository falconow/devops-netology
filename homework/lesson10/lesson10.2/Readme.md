## Домашнее задание к занятию "10.02. Системы мониторинга"

### Задание 1

PUSH - удобна при использовании большого количества клиентов, которые отправляют данные. 
Например у нас есть приложение которым пользуются тысячи клиентов, и их количество постоянно меняется. 
Поэтому удобно когда приложение само отправляет статистику своей работы. 
Получаем данные в момент когда приложение работает. Используя протокол UDP можно повысить скорость сбора метрик.
Из минусов низкая защита данных, негарантированная доставкаметрики при использовании протокола UDP, а также потеря всех данных на время отказа сервера, 
принимающего метрики.

PULL - удобный, централизованный контроль метрик. Собираем метрики с тех узлов, которые нас интересуют. Можно безопасно подключаться к агентам, используя защищенные соединения. Удобно использовать в статичных системах, где нет постоянного увеличения числа устройств для считывания метрик. 
Из минусов как написал выше это неудобство использования в системах с динамическим увеличением клиентов. Также в таких системах ты получаешь все метрики которые дает агент, несмотря на то, что половина из них может быть не нужна в той или иной реализации.

***

###  Задание 2
-  **Prometheus**   
 По умолчанию, метрики в Prometheus попадают методом pull — система обращается к агентам (exporter) и забирает данные. 

 - **TICK**   
 Метод push. telegraph собирает метрики и  передает информацию в систему хранения. модели

 - **Zabbix**   
  pull метод.Подключается к ресурсом по стандартным протоколам или оправшивает свои агенты установленные на серверах для получения данных

  - **VictoriaMetrics**     
  Т.к. VictoriaMetrics является СУБД для хранения временных рядов, в нее данные пишутся напрямую. Поэтому здесь метод push

  - **Nagios**    
  Здесь метод pull. Он также опращивает агентов, которые собирают информацию


***
### Задание 3
> Клонировал репозиторий. Запустил TICK-стэк.
```
falconow@falconow:~$ docker ps
CONTAINER ID   IMAGE                   COMMAND                  CREATED          STATUS          PORTS                                                                                                                             NAMES
70b442608033   chrono_config           "/entrypoint.sh chro…"   30 minutes ago   Up 30 minutes   0.0.0.0:8888->8888/tcp, :::8888->8888/tcp                                                                                         sandbox_chronograf_1
29c095fe4dea   kapacitor               "/entrypoint.sh kapa…"   30 minutes ago   Up 30 minutes   0.0.0.0:9092->9092/tcp, :::9092->9092/tcp                                                                                         sandbox_kapacitor_1
601ce633c3bd   telegraf                "/entrypoint.sh tele…"   30 minutes ago   Up 30 minutes   8092/udp, 8125/udp, 8094/tcp                                                                                                      sandbox_telegraf_1
19d497ab182a   sandbox_documentation   "/documentation/docu…"   30 minutes ago   Up 30 minutes   0.0.0.0:3010->3000/tcp, :::3010->3000/tcp                                                                                         sandbox_documentation_1
f54637f388bd   influxdb                "/entrypoint.sh infl…"   30 minutes ago   Up 30 minutes   0.0.0.0:8082->8082/tcp, :::8082->8082/tcp, 0.0.0.0:8086->8086/tcp, :::8086->8086/tcp, 0.0.0.0:8089->8089/udp, :::8089->8089/udp   sandbox_influxdb_1
falconow@falconow:~$ 

```

> Запускаем команды curl. Некоторые команды возвращают пустую строку

1.  
```
falconow@falconow:~$ curl http://localhost:8086/ping
falconow@falconow:~$ 
falconow@falconow:~$ curl http://localhost:8888
<!DOCTYPE html><html><head><meta http-equiv="Content-type" content="text/html; charset=utf-8"><title>Chronograf</title><link rel="icon shortcut" href="/favicon.fa749080.ico"><link rel="stylesheet" href="/src.3dbae016.css"></head><body> <div id="react-root" data-basepath=""></div> <script src="/src.fab22342.js"></script> </body></html>falconow@falconow:~$ 
falconow@falconow:~$ 
falconow@falconow:~$ curl http://localhost:9092/kapacitor/v1/ping
ng
falconow@falconow:~$ 
```
Скриншот
![Скрин](./screenshots/screen1.png)
***

### Задание 4
> Изучил вывод интерфейса и БД telegraf.autogen. посмотрел как можно построить запрос на примере утилизации оперативной памяти. 

> По аналогии построил запрос для просмотра утилизации диска

Скриншот:

![Скрин](./screenshots/screen2.png)

***

### Задание 5
> Изучил telegraf inputs. Добавил в конфигурацию telegraf плагин docker. 
Перенастроил контейнер с telegraf и пересобрал его. Увидел новые метрики docker в web-интерфейсе

Скриншот:
![Скрин](./screenshots/screen3.png)