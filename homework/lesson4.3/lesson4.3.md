### Задание 1
> Исправил json, ошибка в третьем объекте в ключе ip
````
{ "info" : "Sample JSON output from our service\t",
  "elements" :[
        { "name" : "first",
        "type" : "server",
        "ip" : 7175 
        },
        { "name" : "second",
        "type" : "proxy",
        "ip" : "71.78.22.43"
        }
    ]
}
````
***

### Задание 2
> Доработал скрипт из предыдущего урока:

```
root@vagrant:~# cat ./test.py
#!/bin/python3
import socket
import os
import json
import yaml
site_list=("drive.google.com", "mail.google.com", "google.com")
list_to_dict=[]
for i in site_list:
    ip_new=socket.gethostbyname(i)
    list_to_dict.append({i:ip_new})
    with open(i,'r') as f:
        ip_old=f.read()
    print(f"{i}-{ip_new}")
    if (ip_new != ip_old):
        print(f"[ERROR] {i} IP mismatch: <{ip_old}> <{ip_new}>")
    with open(i,'w') as f:
        f.write(ip_new)
dict_sites={"sites":list_to_dict}
with open("sites.json","w") as f:
    f.write(json.dumps(dict_sites))
with open("sites.yaml","w") as f:
    f.write(yaml.dump(dict_sites))
root@vagrant:~#
```

> Запускаем и смотрим результат выполнения:

````
root@vagrant:~# ./test.py
drive.google.com-173.194.73.194
mail.google.com-142.250.74.37
google.com-142.250.74.14
````
````
root@vagrant:~# cat sites.json 
{"sites": [{"drive.google.com": "173.194.73.194"}, {"mail.google.com": "142.250.74.37"}, {"google.com": "142.250.74.14"}]}
root@vagrant:~# 
````
```` 
root@vagrant:~# cat sites.yaml 
sites:
- drive.google.com: 173.194.73.194
- mail.google.com: 142.250.74.37
- google.com: 142.250.74.14
root@vagrant:~# 
````

> Файлы json и yaml формируются