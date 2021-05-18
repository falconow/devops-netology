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

