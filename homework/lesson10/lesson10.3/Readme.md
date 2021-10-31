## Домашнее задание к занятию "10.03. Grafana"

Задание повышенной сложности
> Решил написать playbook для установки всех компонентов, но столкнулся с проблемой
рассинхронизации времени между сервером в YandexCloud и рабочим компьютером. 
Разобраться со всем этим не хватило времени, поэтому использовал готовый docker-compose.

 1  100 - (avg by(instance) (rate(node_cpu_seconds_total{instance="nodeexporter:9100", mode="idle"}[5m])) * 100)

 2 node_memory_MemAvailable_bytes/1024^3

3 node_load1

4 node_filesystem_avail_bytes{fstype!~"tmpfs|fuse.lxcfs|squashfs"} / node_filesystem_size_bytes{fstype!~"tmpfs|fuse.lxcfs|squashfs"}*100

