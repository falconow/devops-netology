### Задание 1.
1. При первом запуске скрипта поулчаем ошибку:
````
root@vagrant:~/lesson4.2# ./test.py 
Traceback (most recent call last):
  File "./test.py", line 4, in <module>
    c=a+b
TypeError: unsupported operand type(s) for +: 'int' and 'str'
````
> Ошибка несоответствия типов данных. python не может сложить строку и число.

2. Чтобы получить число 12, внесем изменения в скрипт
````
root@vagrant:~/lesson4.2# cat test.py 
#!/usr/bin/python3
a=1
b='2'
c=str(a)+b
print(c)
root@vagrant:~/lesson4.2# ./test.py 
12
root@vagrant:~/lesson4.2# 
````
>Чтобы получить в ответе 12, нам нужно произвести операцию объединения строк.
>Поэтому мы преобразуем тип переменной 'a' из int в str.

3. Чтобы получить число 3, сделаем новые изменения
````
root@vagrant:~/lesson4.2# cat test.py 
#!/usr/bin/python3
a=1
b='2'
c=a+int(b)
print(c)
root@vagrant:~/lesson4.2# ./test.py 
3
root@vagrant:~/lesson4.2# 
````
>Здесь чтоб получить ответ 3 нам необходимо выполнить сложение целых чисел,
> поэтому мы приводим значение переменной 'b' к типу int


### Задание 2
>В исходном скрипте была ошибка, после обработки первого элемента в массиве
скрипт завершался командой break, поэтому не выводились все измененные файлы

Измененный скрипт:
````
root@vagrant:~/lesson4.2# cat ./test2.py 
#!/usr/bin/python3
import os
bash_command = ["cd ~/netology/devops-netology", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(f"{os.getcwd()}/{prepare_result}")
root@vagrant:~/lesson4.2# 
````
>Проверим работу скрипта
````
root@vagrant:~/lesson4.2# ./test2.py 
/root/lesson4.2/homework/lesson3.7/dop_3.7.txt
/root/lesson4.2/homework/lesson3.8/lesson3.8.txt
/root/lesson4.2/homework/lesson4.1/lesson4.1.txt
root@vagrant:~/lesson4.2# 
````
> Скрипт работает, вывод изменили, 
> теперь на выходе полный путь к измененному файлу


### Задание 3
Доработанный скрипт:
````
root@vagrant:~/lesson4.2# cat test3.py 
#!/usr/bin/python3
import os
import sys
if (len(sys.argv)<2):
    print("Не указан путь к репозиторию")
    sys.exit()
bash_command = ["cd "+sys.argv[1], "git status"]
if (not os.access(sys.argv[1]+"/.git",os.F_OK)):
    print("Указанный путь не является локальным репозиторием!")
    sys.exit()
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(f"{os.getcwd()}/{prepare_result}")
````

>Проверим его работу:
````
root@vagrant:~/lesson4.2# ./test3.py 
Не указан путь к репозиторию
root@vagrant:~/lesson4.2# ./test3.py /tmp/
Указанный путь не является локальным репозиторием!
root@vagrant:~/lesson4.2# ./test3.py /root/netology/devops-netology/
/root/lesson4.2/homework/lesson3.7/dop_3.7.txt
/root/lesson4.2/homework/lesson3.8/lesson3.8.txt
/root/lesson4.2/homework/lesson4.1/lesson4.1.txt
root@vagrant:~/lesson4.2# 
````
>Все работает, ошибки некорректного указания репозитория обрабатываются


### Заданиме 4
Скрипт:
````
root@vagrant:~/lesson4.2# cat ./test4.py 
#!/bin/python3
import socket
import os
site_list=("drive.google.com", "mail.google.com", "google.com")
for i in site_list:
    ip_new=socket.gethostbyname(i)
    with open(i,'r') as f:
        ip_old=f.read()
    print(f"{i}-{ip_new}")
    if (ip_new != ip_old):
        print(f"[ERROR] {i} IP mismatch: <{ip_old}> <{ip_new}>")
    with open(i,'w') as f:
        f.write(ip_new)
````

>Проверим работу скрипта
````
root@vagrant:~/lesson4.2# ./test4.py 
drive.google.com-64.233.161.194
mail.google.com-142.250.74.5
google.com-209.85.233.101
````

>Проверяем еще раз через несколько минут
````
root@vagrant:~/lesson4.2# ./test4.py 
drive.google.com-64.233.161.194
mail.google.com-142.250.74.5
google.com-64.233.161.139
[ERROR] google.com IP mismatch: <209.85.233.101> <64.233.161.139>
````
>Скрипт работает, смену ip ловит успешно



