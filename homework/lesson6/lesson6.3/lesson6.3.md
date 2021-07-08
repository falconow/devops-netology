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

### Задание 2
***
Создание пользователя:
```buildoutcfg
CREATE USER 'test'@'127.0.0.1' 
IDENTIFIED WITH mysql_native_password BY 'test-pass'
WITH MAX_QUERIES_PER_HOUR 100 
PASSWORD EXPIRE INTERVAL 180 DAY 
FAILED_LOGIN_ATTEMPTS 3 
ATTRIBUTE '{"fname":"James", "lname":"Pretty"}';
```

Привилегии:
```buildoutcfg
GRANT SELECT ON test_db.* TO test@127.0.0.1;
```

Данные по пользователю:
```buildoutcfg
mysql> SELECT * FROM INFORMATION_SCHEMA.USER_ATTRIBUTES WHERE USER='test';
+------+-----------+---------------------------------------+
| USER | HOST      | ATTRIBUTE                             |
+------+-----------+---------------------------------------+
| test | 127.0.0.1 | {"fname": "James", "lname": "Pretty"} |
+------+-----------+---------------------------------------+
1 row in set (0.00 sec)

```

### Задание 3
***
```buildoutcfg
mysql> SHOW PROFILES;
+----------+------------+-------------------------+
| Query_ID | Duration   | Query                   |
+----------+------------+-------------------------+
|        1 | 0.01102175 | SHOW ENGINES            |
|        2 | 0.00022625 | DROP TABLE IF EXISTS t1 |
|        3 | 0.02470950 | SHOW DATABASES          |
|        4 | 0.00354250 | SELECT DATABASE()       |
|        5 | 0.00126725 | show databases          |
|        6 | 0.01512975 | show tables             |
|        7 | 0.00188075 | SHOW TABLES             |
|        8 | 0.00080450 | SHOW DATABASES          |
|        9 | 0.00046600 | SELECT DATABASE()       |
|       10 | 0.00107025 | show databases          |
|       11 | 0.00139550 | show tables             |
|       12 | 0.00029700 | SET profiling = 1       |
|       13 | 0.00038975 | SELECT @@profiling      |
+----------+------------+-------------------------+
13 rows in set, 1 warning (0.00 sec)
```
> Видим длительность выполнения последних команд

Смотрим Engine:
```buildoutcfg
mysql> SELECT TABLE_NAME,ENGINE,ROW_FORMAT,TABLE_ROWS,DATA_LENGTH,INDEX_LENGTH FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'test_db' ORDER BY ENGINE asc;
+------------+--------+------------+------------+-------------+--------------+
| TABLE_NAME | ENGINE | ROW_FORMAT | TABLE_ROWS | DATA_LENGTH | INDEX_LENGTH |
+------------+--------+------------+------------+-------------+--------------+
| orders     | InnoDB | Dynamic    |          5 |       16384 |            0 |
+------------+--------+------------+------------+-------------+--------------+
1 row in set (0.00 sec)


```

Время выполнения:
```buildoutcfg
|       18 | 0.04891800 | ALTER TABLE orders ENGINE = MyISAM  
```

```buildoutcfg
|       24 | 0.00029375 | SELECT * FROM orders 
```

```buildoutcfg
|       22 | 0.23670525 | ALTER TABLE orders ENGINE = InnoDB  
```

```buildoutcfg
|       26 | 0.00031350 | SELECT * FROM orders 
```

> Как видно из результатов, на InnoDB запрос выполняется медленнее


### Задание 4
***

```buildoutcfg
root@a18c5cddc997:/etc/mysql# cat my.cnf
# Copyright (c) 2017, Oracle and/or its affiliates. All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA

#
# The MySQL  Server configuration file.
#
# For explanations see
# http://dev.mysql.com/doc/mysql/en/server-system-variables.html

[mysqld]
pid-file        = /var/run/mysqld/mysqld.pid
socket          = /var/run/mysqld/mysqld.sock
datadir         = /var/lib/mysql
secure-file-priv= NULL
innodb_buffer_pool_size=300M
innodb_log_file_size=100M
innodb_log_buffer_size=1M
innodb_file_per_table=1
innodb_flush_log_at_trx_commit = 2

# Custom config should go here
!includedir /etc/mysql/conf.d/

```