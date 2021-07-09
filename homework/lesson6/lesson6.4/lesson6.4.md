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
> К сожалению на лекциях не показали никаких примеров как работать с масштабированием, все изучено 
> самостоятельно из доп. материала. Возможно есть способ проще, я бы был рад увидеть его.

Транзакция для разбиения таблицы:
```buildoutcfg
BEGIN;
ALTER TABLE orders RENAME TO orders_old;
CREATE TABLE orders (LIKE orders_old INCLUDING ALL);
CREATE TABLE orders_1 (CHECK (price<=499)) INHERITS (orders);
CREATE TABLE orders_2 (CHECK (price>499)) INHERITS (orders);
CREATE INDEX orders_1_rate_idx ON orders_1(id);
CREATE INDEX orders_2_rate_idx ON orders_2(id);
CREATE RULE orders_insert_to_1 AS ON INSERT TO orders WHERE ( price <= 499) DO INSTEAD INSERT INTO orders_1 VALUES (NEW.*);
CREATE RULE orders_insert_to_2 AS ON INSERT TO orders WHERE ( price > 499) DO INSTEAD INSERT INTO orders_2 VALUES (NEW.*);
INSERT INTO orders SELECT * FROM orders_old;
COMMIT;
```

Смотрим что получилось:
```buildoutcfg
test_database=# EXPLAIN ANALYZE SELECT * FROM orders;
                                                      QUERY PLAN                                                      
----------------------------------------------------------------------------------------------------------------------
 Append  (cost=0.00..31.41 rows=761 width=186) (actual time=0.005..0.010 rows=8 loops=1)
   ->  Seq Scan on orders orders_1  (cost=0.00..0.00 rows=1 width=186) (actual time=0.003..0.003 rows=0 loops=1)
   ->  Seq Scan on orders_1 orders_2  (cost=0.00..13.80 rows=380 width=186) (actual time=0.002..0.003 rows=5 loops=1)
   ->  Seq Scan on orders_2 orders_3  (cost=0.00..13.80 rows=380 width=186) (actual time=0.002..0.002 rows=3 loops=1)
 Planning Time: 0.077 ms
 Execution Time: 0.021 ms
(6 rows)
```

```buildoutcfg
test_database=# SELECT * FROM only orders;
 id | title | price 
----+-------+-------
(0 rows)

```
```buildoutcfg
test_database=# SELECT * FROM orders_1;
 id |        title         | price 
----+----------------------+-------
  1 | War and peace        |   100
  3 | Adventure psql time  |   300
  4 | Server gravity falls |   300
  5 | Log gossips          |   123
  7 | Me and my bash-pet   |   499
(5 rows)

```
```buildoutcfg
test_database=# SELECT * FROM orders_2;
 id |       title        | price 
----+--------------------+-------
  2 | My little database |   500
  6 | WAL never lies     |   900
  8 | Dbiezdmin          |   501
(3 rows)

```

> Как видно из транзакции, разбиение можно делать сразу при проектировании таблицы


### Задание 4
***
> pg_dump -h127.0.0.1 -Upostgres test_database > /tmp/test_database.sql

Текущий backup:
```buildoutcfg
root@d5eb5d008c5f:/# cat /tmp/test_database.sql 
--
-- PostgreSQL database dump
--

-- Dumped from database version 13.3 (Debian 13.3-1.pgdg100+1)
-- Dumped by pg_dump version 13.3 (Debian 13.3-1.pgdg100+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: orders_old; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.orders_old (
    id integer NOT NULL,
    title character varying(80) NOT NULL,
    price integer DEFAULT 0
);


ALTER TABLE public.orders_old OWNER TO postgres;

--
-- Name: orders_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.orders_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.orders_id_seq OWNER TO postgres;

--
-- Name: orders_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.orders_id_seq OWNED BY public.orders_old.id;


--
-- Name: orders; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.orders (
    id integer DEFAULT nextval('public.orders_id_seq'::regclass) NOT NULL,
    title character varying(80) NOT NULL,
    price integer DEFAULT 0
);


ALTER TABLE public.orders OWNER TO postgres;

--
-- Name: orders_1; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.orders_1 (
    CONSTRAINT orders_1_price_check CHECK ((price <= 499))
)
INHERITS (public.orders);


ALTER TABLE public.orders_1 OWNER TO postgres;

--
-- Name: orders_2; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.orders_2 (
    CONSTRAINT orders_2_price_check CHECK ((price > 499))
)
INHERITS (public.orders);


ALTER TABLE public.orders_2 OWNER TO postgres;

--
-- Name: orders_1 id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders_1 ALTER COLUMN id SET DEFAULT nextval('public.orders_id_seq'::regclass);


--
-- Name: orders_1 price; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders_1 ALTER COLUMN price SET DEFAULT 0;


--
-- Name: orders_2 id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders_2 ALTER COLUMN id SET DEFAULT nextval('public.orders_id_seq'::regclass);


--
-- Name: orders_2 price; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders_2 ALTER COLUMN price SET DEFAULT 0;


--
-- Name: orders_old id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders_old ALTER COLUMN id SET DEFAULT nextval('public.orders_id_seq'::regclass);


--
-- Data for Name: orders; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.orders (id, title, price) FROM stdin;
\.


--
-- Data for Name: orders_1; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.orders_1 (id, title, price) FROM stdin;
1	War and peace	100
3	Adventure psql time	300
4	Server gravity falls	300
5	Log gossips	123
7	Me and my bash-pet	499
\.


--
-- Data for Name: orders_2; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.orders_2 (id, title, price) FROM stdin;
2	My little database	500
6	WAL never lies	900
8	Dbiezdmin	501
\.


--
-- Data for Name: orders_old; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.orders_old (id, title, price) FROM stdin;
1	War and peace	100
2	My little database	500
3	Adventure psql time	300
4	Server gravity falls	300
5	Log gossips	123
6	WAL never lies	900
7	Me and my bash-pet	499
8	Dbiezdmin	501
\.


--
-- Name: orders_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.orders_id_seq', 8, true);


--
-- Name: orders_old orders_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders_old
    ADD CONSTRAINT orders_pkey PRIMARY KEY (id);


--
-- Name: orders orders_pkey1; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey1 PRIMARY KEY (id);


--
-- Name: orders_1_rate_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX orders_1_rate_idx ON public.orders_1 USING btree (id);


--
-- Name: orders_2_rate_idx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX orders_2_rate_idx ON public.orders_2 USING btree (id);


--
-- Name: orders orders_insert_to_1; Type: RULE; Schema: public; Owner: postgres
--

CREATE RULE orders_insert_to_1 AS
    ON INSERT TO public.orders
   WHERE (new.price <= 499) DO INSTEAD  INSERT INTO public.orders_1 (id, title, price)
  VALUES (new.id, new.title, new.price);


--
-- Name: orders orders_insert_to_2; Type: RULE; Schema: public; Owner: postgres
--

CREATE RULE orders_insert_to_2 AS
    ON INSERT TO public.orders
   WHERE (new.price > 499) DO INSTEAD  INSERT INTO public.orders_2 (id, title, price)
  VALUES (new.id, new.title, new.price);


--
-- PostgreSQL database dump complete
--

root@d5eb5d008c5f:/# 

```

> Чтобы добавить уникальность значения столбца title нужно поправить в дампе создание таблицы orders и добавить параметр UNIQUE
```buildoutcfg
CREATE TABLE public.orders (
    id integer DEFAULT nextval('public.orders_id_seq'::regclass) NOT NULL,
    title character varying(80) NOT NULL UNIQUE,
    price integer DEFAULT 0
);
```