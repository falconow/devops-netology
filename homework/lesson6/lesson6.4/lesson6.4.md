### Задание 1
***
Вывод списка БД:
```buildoutcfg
 \l[+]   [PATTERN]      list databases
```
Подключение к БД:
```buildoutcfg
 \c[onnect] {[DBNAME|- USER|- HOST|- PORT|-] | conninfo}
                         connect to new database (currently "postgres")

```
Вывод списка таблиц:
```buildoutcfg
 \d[S+]                 list tables, views, and sequences
```
Вывод описания содержимого таблиц:
```buildoutcfg
 \d[S+]  NAME           describe table, view, sequence, or index
```
Выход из psql:
```buildoutcfg
 \q                     quit psql
```

### Задание 2
***
```buildoutcfg
SELECT avg_width,attname FROM pg_stats WHERE tablename='orders';
 avg_width | attname 
-----------+---------
         4 | id
        16 | title
         4 | price
(3 rows)
```
> Наибольшее среднее значение у столбца 'title'


### Задание 3
***
