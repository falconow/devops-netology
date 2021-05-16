### Задание1. 
#### Выполним команды:

>		1. root@vagrant:~# a=1;b=2;c=a+b;echo $c
>		a+b
>>Такой ответ получаем потому что в выражении мы не обращаемся к переменым a и b, поэтому получаем 
объединение символов a,+ и b.

>		2. root@vagrant:~# a=1;b=2;d=$a+$b;echo $d
>		1+2
>		root@vagrant:~# 
>>Здесь мы уже обращаемся к значениям переменных a и b, но т.к. по умолчанию все значения в переменных являются строками,
мы снова получаем объединение строк.

>		3. root@vagrant:~# a=1;b=2;e=$(($a+$b));echo $e
>		3
>>В этом случае используется синтаксис для арифметической операции, bash переводит значения переменных в целые числа и 
производит арифметическую операцию сложения чисел.


### Задание 2. 
В скрипте есть синтаксическая ошибка при задании цикла, не хватает скобки.
Также условие цикла 1==1 думаю некорректное, цикл никогда не завершится, я бы такой не использовал.
Мой вариант скрипта следующий:
	
	root@vagrant:~# cat test.sh
	a=1
	while (($a != 0))
	do
		curl http://localhost
		a=$?
		if (($a != 0))
		then
			date >> curl.log
		fi
	done
	root@vagrant:~# 

>Значение результата нужно хранить в переменной, которая участвует в уловии цикла.
После успешного выполнения запроса переменная a станет равной нулю, и условие цикла не выполнится.

#### Можно и такой вариант:
	while ((1==1))
	do
		curl http://localhost
		if (($? != 0))
		then
			date >> curl.log
		else
			break
		fi
	done

>Завершить выполнение цикла через break, при успешном запросе


>Работа скриптов проверена с помощью nginx



### Задание 3. 
#### Написал скрипт для проверки:

	root@vagrant:~# cat check.sh 
	#!/usr/bin/bash
	array_ip=(192.168.0.1 173.194.222.113 87.250.250.242)
	echo "Start check" > checklog.log
	for i in ${array_ip[@]}
	do
	    y=1
	    while(($y<6))
	    do
		echo ip $i попытка $y >> checklog.log
		curl -I $i>>checklog.log
		let "y +=1"
	    done
	done
	root@vagrant:~# 

>Проверим его работу:
 
	root@vagrant:~# 2>/dev/null ./check.sh; cat checklog.log 
```Start check
ip 192.168.0.1 попытка 1
HTTP/1.1 405 Method Not Allowed
Content-Type: text/html; charset=utf-8
Content-Length: 124
Set-Cookie: JSESSIONID=deleted; Expires=Thu, 01 Jan 1970 00:00:01 GMT; Path=/; HttpOnly
Connection: close

ip 192.168.0.1 попытка 2
HTTP/1.1 405 Method Not Allowed
Content-Type: text/html; charset=utf-8
Content-Length: 124
Set-Cookie: JSESSIONID=deleted; Expires=Thu, 01 Jan 1970 00:00:01 GMT; Path=/; HttpOnly
Connection: close

ip 192.168.0.1 попытка 3
HTTP/1.1 405 Method Not Allowed
Content-Type: text/html; charset=utf-8
Content-Length: 124
Set-Cookie: JSESSIONID=deleted; Expires=Thu, 01 Jan 1970 00:00:01 GMT; Path=/; HttpOnly
Connection: close

ip 192.168.0.1 попытка 4
HTTP/1.1 405 Method Not Allowed
Content-Type: text/html; charset=utf-8
Content-Length: 124
Set-Cookie: JSESSIONID=deleted; Expires=Thu, 01 Jan 1970 00:00:01 GMT; Path=/; HttpOnly
Connection: close

ip 192.168.0.1 попытка 5
HTTP/1.1 405 Method Not Allowed
Content-Type: text/html; charset=utf-8
Content-Length: 124
Set-Cookie: JSESSIONID=deleted; Expires=Thu, 01 Jan 1970 00:00:01 GMT; Path=/; HttpOnly
Connection: close

ip 173.194.222.113 попытка 1
HTTP/1.1 301 Moved Permanently
Location: http://www.google.com/
Content-Type: text/html; charset=UTF-8
Date: Sat, 15 May 2021 19:39:11 GMT
Expires: Mon, 14 Jun 2021 19:39:11 GMT
Cache-Control: public, max-age=2592000
Server: gws
Content-Length: 219
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN

ip 173.194.222.113 попытка 2
HTTP/1.1 301 Moved Permanently
Location: http://www.google.com/
Content-Type: text/html; charset=UTF-8
Date: Sat, 15 May 2021 19:39:11 GMT
Expires: Mon, 14 Jun 2021 19:39:11 GMT
Cache-Control: public, max-age=2592000
Server: gws
Content-Length: 219
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN

ip 173.194.222.113 попытка 3
HTTP/1.1 301 Moved Permanently
Location: http://www.google.com/
Content-Type: text/html; charset=UTF-8
Date: Sat, 15 May 2021 19:39:11 GMT
Expires: Mon, 14 Jun 2021 19:39:11 GMT
Cache-Control: public, max-age=2592000
Server: gws
Content-Length: 219
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN

ip 173.194.222.113 попытка 4
HTTP/1.1 301 Moved Permanently
Location: http://www.google.com/
Content-Type: text/html; charset=UTF-8
Date: Sat, 15 May 2021 19:39:11 GMT
Expires: Mon, 14 Jun 2021 19:39:11 GMT
Cache-Control: public, max-age=2592000
Server: gws
Content-Length: 219
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN

ip 173.194.222.113 попытка 5
HTTP/1.1 301 Moved Permanently
Location: http://www.google.com/
Content-Type: text/html; charset=UTF-8
Date: Sat, 15 May 2021 19:39:11 GMT
Expires: Mon, 14 Jun 2021 19:39:11 GMT
Cache-Control: public, max-age=2592000
Server: gws
Content-Length: 219
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN

ip 87.250.250.242 попытка 1
HTTP/1.1 406 Not acceptable
Connection: Close
Content-Length: 0

ip 87.250.250.242 попытка 2
HTTP/1.1 406 Not acceptable
Connection: Close
Content-Length: 0

ip 87.250.250.242 попытка 3
HTTP/1.1 406 Not acceptable
Connection: Close
Content-Length: 0

ip 87.250.250.242 попытка 4
HTTP/1.1 406 Not acceptable
Connection: Close
Content-Length: 0

ip 87.250.250.242 попытка 5
HTTP/1.1 406 Not acceptable
Connection: Close
Content-Length: 0

root@vagrant:~#> 
```

### Задание 4. 
#### Изменил предыдущий скрипт. Наш новый скрипт: 

	root@vagrant:~# cat check2.sh 
```
#!/usr/bin/bash
array_ip=(192.168.0.1 173.194.222.113 192.168.1.1)
echo "Start check" > checklog2.log
for i in ${array_ip[@]}
do
    y=1
    while(($y<6))
    do
	echo ip $i попытка $y >> checklog2.log
	curl --connect-timeout 3 -I $i>>checklog2.log
	if (($? != 0))
	then 
	    echo $i >> error
	    break
	fi
	let "y +=1"
    done
done
```

>Проверяем:

	root@vagrant:~# 2>/dev/null ./check2.sh
	root@vagrant:~# cat checklog2.log 
```
Start check
ip 192.168.0.1 попытка 1
HTTP/1.1 405 Method Not Allowed
Content-Type: text/html; charset=utf-8
Content-Length: 124
Set-Cookie: JSESSIONID=deleted; Expires=Thu, 01 Jan 1970 00:00:01 GMT; Path=/; HttpOnly
Connection: close

ip 192.168.0.1 попытка 2
HTTP/1.1 405 Method Not Allowed
Content-Type: text/html; charset=utf-8
Content-Length: 124
Set-Cookie: JSESSIONID=deleted; Expires=Thu, 01 Jan 1970 00:00:01 GMT; Path=/; HttpOnly
Connection: close

ip 192.168.0.1 попытка 3
HTTP/1.1 405 Method Not Allowed
Content-Type: text/html; charset=utf-8
Content-Length: 124
Set-Cookie: JSESSIONID=deleted; Expires=Thu, 01 Jan 1970 00:00:01 GMT; Path=/; HttpOnly
Connection: close

ip 192.168.0.1 попытка 4
HTTP/1.1 405 Method Not Allowed
Content-Type: text/html; charset=utf-8
Content-Length: 124
Set-Cookie: JSESSIONID=deleted; Expires=Thu, 01 Jan 1970 00:00:01 GMT; Path=/; HttpOnly
Connection: close

ip 192.168.0.1 попытка 5
HTTP/1.1 405 Method Not Allowed
Content-Type: text/html; charset=utf-8
Content-Length: 124
Set-Cookie: JSESSIONID=deleted; Expires=Thu, 01 Jan 1970 00:00:01 GMT; Path=/; HttpOnly
Connection: close

ip 173.194.222.113 попытка 1
HTTP/1.1 301 Moved Permanently
Location: http://www.google.com/
Content-Type: text/html; charset=UTF-8
Date: Sun, 16 May 2021 17:29:30 GMT
Expires: Tue, 15 Jun 2021 17:29:30 GMT
Cache-Control: public, max-age=2592000
Server: gws
Content-Length: 219
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN

ip 173.194.222.113 попытка 2
HTTP/1.1 301 Moved Permanently
Location: http://www.google.com/
Content-Type: text/html; charset=UTF-8
Date: Sun, 16 May 2021 17:29:30 GMT
Expires: Tue, 15 Jun 2021 17:29:30 GMT
Cache-Control: public, max-age=2592000
Server: gws
Content-Length: 219
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN

ip 173.194.222.113 попытка 3
HTTP/1.1 301 Moved Permanently
Location: http://www.google.com/
Content-Type: text/html; charset=UTF-8
Date: Sun, 16 May 2021 17:29:30 GMT
Expires: Tue, 15 Jun 2021 17:29:30 GMT
Cache-Control: public, max-age=2592000
Server: gws
Content-Length: 219
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN

ip 173.194.222.113 попытка 4
HTTP/1.1 301 Moved Permanently
Location: http://www.google.com/
Content-Type: text/html; charset=UTF-8
Date: Sun, 16 May 2021 17:29:30 GMT
Expires: Tue, 15 Jun 2021 17:29:30 GMT
Cache-Control: public, max-age=2592000
Server: gws
Content-Length: 219
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN

ip 173.194.222.113 попытка 5
HTTP/1.1 301 Moved Permanently
Location: http://www.google.com/
Content-Type: text/html; charset=UTF-8
Date: Sun, 16 May 2021 17:29:30 GMT
Expires: Tue, 15 Jun 2021 17:29:30 GMT
Cache-Control: public, max-age=2592000
Server: gws
Content-Length: 219
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN

ip 192.168.1.1 попытка 1
```
```
root@vagrant:~# cat error 
192.168.1.1
root@vagrant:~#
``` 

>Все работает, скрипт останавливается, файл error записывается