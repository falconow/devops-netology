### Задание 1
> docker run --name postgres -d -p5432:5432 -v /root/lesson6.2/databases:/var/lib/postgresql/data -v /root/lesson6.2/backup:/var/backup -e POSTGRES_PASSWORD=3223555 postgres:12

### Задание 2

```buildoutcfg
test_db=# \l
                                     List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |       Access privileges        
-----------+----------+----------+------------+------------+--------------------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres                   +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres                   +
           |          |          |            |            | postgres=CTc/postgres
 test_db   | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =Tc/postgres                  +
           |          |          |            |            | postgres=CTc/postgres         +
           |          |          |            |            | "test-admin-user"=CTc/postgres
(4 rows)

test_db=# 
```

```buildoutcfg
test_db-# \d+ orders;
                                                   Table "public.orders"
    Column    |  Type   | Collation | Nullable |              Default               | Storage  | Stats target | Description 
--------------+---------+-----------+----------+------------------------------------+----------+--------------+-------------
 id           | integer |           | not null | nextval('orders_id_seq'::regclass) | plain    |              | 
 наименование | text    |           |          |                                    | extended |              | 
 цена         | integer |           |          |                                    | plain    |              | 
Indexes:
    "orders_pkey" PRIMARY KEY, btree (id)
Referenced by:
    TABLE "clients" CONSTRAINT "clients_заказ_fkey" FOREIGN KEY ("заказ") REFERENCES orders(id)
Access method: heap

test_db-# 
```

```buildoutcfg
test_db-# \d+ clients;
                                                      Table "public.clients"
      Column       |  Type   | Collation | Nullable |               Default               | Storage  | Stats target | Description 
-------------------+---------+-----------+----------+-------------------------------------+----------+--------------+-------------
 id                | integer |           | not null | nextval('clients_id_seq'::regclass) | plain    |              | 
 фамилия           | text    |           |          |                                     | extended |              | 
 страна проживания | text    |           |          |                                     | extended |              | 
 заказ             | integer |           |          |                                     | plain    |              | 
Indexes:
    "clients_pkey" PRIMARY KEY, btree (id)
    "index_on_clients" btree ("страна проживания")
Foreign-key constraints:
    "clients_заказ_fkey" FOREIGN KEY ("заказ") REFERENCES orders(id)
Access method: heap

test_db-# 

```

```buildoutcfg
test_db=# SELECT table_catalog, table_schema, table_name, privilege_type,grantee FROM information_schema.table_privileges WHERE table_schema='public';
 table_catalog | table_schema | table_name | privilege_type |     grantee      
---------------+--------------+------------+----------------+------------------
 test_db       | public       | orders     | INSERT         | postgres
 test_db       | public       | orders     | SELECT         | postgres
 test_db       | public       | orders     | UPDATE         | postgres
 test_db       | public       | orders     | DELETE         | postgres
 test_db       | public       | orders     | TRUNCATE       | postgres
 test_db       | public       | orders     | REFERENCES     | postgres
 test_db       | public       | orders     | TRIGGER        | postgres
 test_db       | public       | orders     | INSERT         | test-simple-user
 test_db       | public       | orders     | SELECT         | test-simple-user
 test_db       | public       | orders     | UPDATE         | test-simple-user
 test_db       | public       | orders     | DELETE         | test-simple-user
 test_db       | public       | orders     | INSERT         | test-admin-user
 test_db       | public       | orders     | SELECT         | test-admin-user
 test_db       | public       | orders     | UPDATE         | test-admin-user
 test_db       | public       | orders     | DELETE         | test-admin-user
 test_db       | public       | orders     | TRUNCATE       | test-admin-user
 test_db       | public       | orders     | REFERENCES     | test-admin-user
 test_db       | public       | orders     | TRIGGER        | test-admin-user
 test_db       | public       | clients    | INSERT         | postgres
 test_db       | public       | clients    | SELECT         | postgres
 test_db       | public       | clients    | UPDATE         | postgres
 test_db       | public       | clients    | DELETE         | postgres
 test_db       | public       | clients    | TRUNCATE       | postgres
 test_db       | public       | clients    | REFERENCES     | postgres
 test_db       | public       | clients    | TRIGGER        | postgres
 test_db       | public       | clients    | INSERT         | test-simple-user
 test_db       | public       | clients    | SELECT         | test-simple-user
 test_db       | public       | clients    | UPDATE         | test-simple-user
 test_db       | public       | clients    | DELETE         | test-simple-user
 test_db       | public       | clients    | INSERT         | test-admin-user
 test_db       | public       | clients    | SELECT         | test-admin-user
 test_db       | public       | clients    | UPDATE         | test-admin-user
 test_db       | public       | clients    | DELETE         | test-admin-user
 test_db       | public       | clients    | TRUNCATE       | test-admin-user
 test_db       | public       | clients    | REFERENCES     | test-admin-user
 test_db       | public       | clients    | TRIGGER        | test-admin-user
(36 rows)

test_db=# 

```

```buildoutcfg
test_db=# \dp
                                           Access privileges
 Schema |      Name      |   Type   |         Access privileges          | Column privileges | Policies 
--------+----------------+----------+------------------------------------+-------------------+----------
 public | clients        | table    | postgres=arwdDxt/postgres         +|                   | 
        |                |          | "test-simple-user"=arwd/postgres  +|                   | 
        |                |          | "test-admin-user"=arwdDxt/postgres |                   | 
 public | clients_id_seq | sequence |                                    |                   | 
 public | orders         | table    | postgres=arwdDxt/postgres         +|                   | 
        |                |          | "test-simple-user"=arwd/postgres  +|                   | 
        |                |          | "test-admin-user"=arwdDxt/postgres |                   | 
 public | orders_id_seq  | sequence |                                    |                   | 
(4 rows)

test_db=# 

```

### Задание 3

```buildoutcfg
test_db=# SELECT * FROM orders;
 id | наименование | цена 
----+--------------+------
  1 | Шоколад      |   10
  2 | Принтер      | 3000
  3 | Книга        |  500
  4 | Монитор      | 7000
  5 | Гитара       | 4000
(5 rows)

test_db=# 
```
```buildoutcfg
test_db=# SELECT COUNT(*) FROM orders;
 count 
-------
     5
(1 row)

test_db=# 

```

```buildoutcfg
test_db=# SELECT * FROM clients;
 id |       фамилия        | страна проживания | заказ 
----+----------------------+-------------------+-------
  1 | Иванов Иван Иванович | USA               |      
  2 | Петров Петр Петрович | Canada            |      
  3 | Иоганн Себастьян Бах | Japan             |      
  4 | Ронни Джеймс Дио     | Russia            |      
  5 | Ritchie Blackmore    | Russia            |      
(5 rows)

test_db=# 
```
```buildoutcfg
test_db=# SELECT COUNT(*) FROM clients;
 count 
-------
     5
(1 row)

test_db=# 
```

### Задание 4
```buildoutcfg
UPDATE clients SET "заказ"=(SELECT id FROM orders WHERE "наименование"='Книга') WHERE "фамилия"='Иванов Иван Иванович';
UPDATE clients SET "заказ"=(SELECT id FROM orders WHERE "наименование"='Монитор') WHERE "фамилия"='Петров Петр Петрович';
UPDATE clients SET "заказ"=(SELECT id FROM orders WHERE "наименование"='Гитара') WHERE "фамилия"='Иоганн Себастьян Бах';
```
```buildoutcfg
test_db=# SELECT * FROM clients ORDER BY id;
 id |       фамилия        | страна проживания | заказ 
----+----------------------+-------------------+-------
  1 | Иванов Иван Иванович | USA               |     3
  2 | Петров Петр Петрович | Canada            |     4
  3 | Иоганн Себастьян Бах | Japan             |     5
  4 | Ронни Джеймс Дио     | Russia            |      
  5 | Ritchie Blackmore    | Russia            |      
(5 rows)

test_db=# 
```
```buildoutcfg
test_db=# SELECT "фамилия" FROM clients WHERE "заказ">0;
       фамилия        
----------------------
 Иванов Иван Иванович
 Петров Петр Петрович
 Иоганн Себастьян Бах
(3 rows)

test_db=# 
```

### Задание 5
```buildoutcfg
test_db=# EXPLAIN SELECT "фамилия" FROM clients WHERE "заказ">0;
                        QUERY PLAN                         
-----------------------------------------------------------
 Seq Scan on clients  (cost=0.00..20.12 rows=270 width=32)
   Filter: ("заказ" > 0)
(2 rows)
```
> Seq Scan — последовательное, блок за блоком, чтение данных таблицы clients.
> 
> cost, не является временем, это абстрактное понятие, которое характеризует затраты на получение. Первая цифра на получение
> первой строки, второе на получение всех строк
> 
> row, отображает количество строк(у нас почему-то неверно).
> 
> width, средний размер строки в байтах.

>  Выполнил команду:
> 
> 
```
test_db=# ANALYZE clients;
ANALYZE
test_db=# 
test_db=# EXPLAIN SELECT "фамилия" FROM clients WHERE "заказ">0;
                       QUERY PLAN                       
--------------------------------------------------------
 Seq Scan on clients  (cost=0.00..1.06 rows=3 width=33)
   Filter: ("заказ" > 0)
(2 rows)

test_db=# 
```
>Теперь количество строк верно
> 

### Задание 6

```buildoutcfg
root@vagrant:~# docker exec -ti postgres bash
root@83e029f1a911:/# pg_dump -Upostgres test_db > /var/backup/dump.sql
```
```buildoutcfg
root@vagrant:~# docker ps -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS      NAMES
dcb93016179f   postgres:12   "docker-entrypoint.s…"   24 minutes ago   Up 1 second                 5432/tcp   postgres_backup
83e029f1a911   postgres:12   "docker-entrypoint.s…"   5 hours ago      Exited (0) 19 seconds ago              postgres
root@vagrant:~# docker exec -ti postgres_backup bash
root@dcb93016179f:/# 
```
```buildoutcfg
root@dcb93016179f:/# psql -Upostgres -d test_db -f /var/backup/dump.sql 
```
```buildoutcfg
root@dcb93016179f:/# psql -Upostgres
psql (12.7 (Debian 12.7-1.pgdg100+1))
Type "help" for help.

postgres=# \l
                                 List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
-----------+----------+----------+------------+------------+-----------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 test_db   | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
(4 rows)

postgres=# \c test_db
You are now connected to database "test_db" as user "postgres".
test_db=# 
test_db=# \d
               List of relations
 Schema |      Name      |   Type   |  Owner   
--------+----------------+----------+----------
 public | clients        | table    | postgres
 public | clients_id_seq | sequence | postgres
 public | orders         | table    | postgres
 public | orders_id_seq  | sequence | postgres
(4 rows)

test_db=# SELECT * FROM clients;
 id |       фамилия        | страна проживания | заказ 
----+----------------------+-------------------+-------
  4 | Ронни Джеймс Дио     | Russia            |      
  5 | Ritchie Blackmore    | Russia            |      
  1 | Иванов Иван Иванович | USA               |     3
  2 | Петров Петр Петрович | Canada            |     4
  3 | Иоганн Себастьян Бах | Japan             |     5
(5 rows)

test_db=# SELECT * FROM orders;
 id | наименование | цена 
----+--------------+------
  1 | Шоколад      |   10
  2 | Принтер      | 3000
  3 | Книга        |  500
  4 | Монитор      | 7000
  5 | Гитара       | 4000
(5 rows)

test_db=# 
```
> БД восстановленна