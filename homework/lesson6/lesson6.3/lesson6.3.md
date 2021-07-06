### Задание 1
***
Запуск контейнера:
> docker run --name mysql -e MYSQL_ROOT_PASSWORD=3223555 -d -p3306:3306 -v /root/netology/devops-netology/homework/lesson6/lesson6.3/databases/:/var/lib/mysql mysql:8
 
Восстанавливаем дамп:
> root@vagrant:~# mysql -h127.0.0.1 -uroot -p3223555 -D test_db < /root/netology/devops-netology/homework/lesson6/lesson6.3/backup/test_dump.sql

 Статус базы:
```buildoutcfg
mysql> \s
--------------
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))

Connection id:		13
Current database:	
Current user:		root@172.17.0.1
SSL:			Cipher in use is TLS_AES_256_GCM_SHA384
Current pager:		stdout
Using outfile:		''
Using delimiter:	;
******************************************************************
Server version:		8.0.25 MySQL Community Server - GPL
******************************************************************
Protocol version:	10
Connection:		127.0.0.1 via TCP/IP
Server characterset:	utf8mb4
Db     characterset:	utf8mb4
Client characterset:	utf8mb4
Conn.  characterset:	utf8mb4
TCP port:		3306
Binary data as:		Hexadecimal
Uptime:			9 min 51 sec

Threads: 2  Questions: 50  Slow queries: 0  Opens: 155  Flush tables: 3  Open tables: 73  Queries per second avg: 0.084
--------------
```

Список таблиц:
```buildoutcfg
mysql> use test_db;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> SHOW TABLES;
+-------------------+
| Tables_in_test_db |
+-------------------+
| orders            |
+-------------------+
1 row in set (0.00 sec)

mysql> 
```

Результат запроса:
```buildoutcfg
mysql> SELECT * FROM orders WHERE price>300;
+----+----------------+-------+
| id | title          | price |
+----+----------------+-------+
|  2 | My little pony |   500 |
+----+----------------+-------+
1 row in set (0.01 sec)

mysql> SELECT COUNT(*) FROM orders WHERE price>300;
+----------+
| COUNT(*) |
+----------+
|        1 |
+----------+
1 row in set (0.01 sec)

mysql> 
```





