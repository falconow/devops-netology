## Домашнее задание к занятию "12.1 Компоненты Kubernetes"

### **Задача 1: Установить Minikube**
> С помощью Terraform поднял ВМ в YandexCloud, подклчючаемся по ssh и ставим Minikube

```
falconow@masterkube0:~$ curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 44.4M  100 44.4M    0     0  54.3M      0 --:--:-- --:--:-- --:--:-- 54.3M
falconow@masterkube0:~$ chmod +x ./kubectl
falconow@masterkube0:~$ 
falconow@masterkube0:~$ sudo mv ./kubectl /usr/local/bin/kubectl
falconow@masterkube0:~$ 
falconow@masterkube0:~$ sudo apt-get update && sudo apt-get install docker.io conntrack -y
```
```
falconow@masterkube0:~$ curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 66.3M  100 66.3M    0     0  42.6M      0  0:00:01  0:00:01 --:--:-- 42.6M
falconow@masterkube0:~$ 
```

> Смотрим версию Minikube
```
falconow@masterkube0:~$ minikube version
minikube version: v1.24.0
commit: 76b94fb3c4e8ac5062daf70d60cf03ddcc0a741b
falconow@masterkube0:~$ 
```

> Запускаем MiniKube
```
falconow@masterkube0:~$ sudo -i
root@masterkube0:~# minikube start --vm-driver=none
* minikube v1.24.0 on Ubuntu 20.04 (amd64)
* Using the none driver based on user configuration

X The requested memory allocation of 1987MiB does not leave room for system overhead (total system memory: 1987MiB). You may face stability issues.
* Suggestion: Start minikube with less memory allocated: 'minikube start --memory=1987mb'

* Starting control plane node minikube in cluster minikube
* Running on localhost (CPUs=2, Memory=1987MB, Disk=15058MB) ...
* OS release is Ubuntu 20.04.3 LTS
* Preparing Kubernetes v1.22.3 on Docker 20.10.7 ...
  - kubelet.resolv-conf=/run/systemd/resolve/resolv.conf
    > kubelet.sha256: 64 B / 64 B [--------------------------] 100.00% ? p/s 0s
    > kubectl.sha256: 64 B / 64 B [--------------------------] 100.00% ? p/s 0s
    > kubeadm.sha256: 64 B / 64 B [--------------------------] 100.00% ? p/s 0s
    > kubectl: 44.73 MiB / 44.73 MiB [-------------] 100.00% 17.40 MiB p/s 2.8s
    > kubeadm: 43.71 MiB / 43.71 MiB [-------------] 100.00% 15.44 MiB p/s 3.0s
    > kubelet: 115.57 MiB / 115.57 MiB [-----------] 100.00% 22.92 MiB p/s 5.2s
  - Generating certificates and keys ...
  - Booting up control plane ...
  - Configuring RBAC rules ...
* Configuring local host environment ...
* 
! The 'none' driver is designed for experts who need to integrate with an existing VM
* Most users should use the newer 'docker' driver instead, which does not require root!
* For more information, see: https://minikube.sigs.k8s.io/docs/reference/drivers/none/
* 
! kubectl and minikube configuration will be stored in /root
! To use kubectl or minikube commands as your own user, you may need to relocate them. For example, to overwrite your own settings, run:
* 
  - sudo mv /root/.kube /root/.minikube $HOME
  - sudo chown -R $USER $HOME/.kube $HOME/.minikube
* 
* This can also be done automatically by setting the env var CHANGE_MINIKUBE_NONE_USER=true
* Verifying Kubernetes components...
  - Using image gcr.io/k8s-minikube/storage-provisioner:v5
* Enabled addons: storage-provisioner, default-storageclass
* Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
root@masterkube0:~# 
```

> Проверяем
```
root@masterkube0:~# minikube status
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured

root@masterkube0:~# 
```
***

### **Задача 2: Запуск Hello World**
> Устанавливаем тестовое приложение HelloWorld
```
root@masterkube0:~# kubectl create deployment hello-node --image=k8s.gcr.io/echoserver:1.4
deployment.apps/hello-node created
root@masterkube0:~# 
```
```
root@masterkube0:~# kubectl get deployments
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
hello-node   1/1     1            1           23s
root@masterkube0:~# 
```
```
root@masterkube0:~# kubectl get pods
NAME                          READY   STATUS    RESTARTS   AGE
hello-node-7567d9fdc9-gs569   1/1     Running   0          52s
root@masterkube0:~# 
```
> Смотрим events и config
```
root@masterkube0:~# kubectl get events
LAST SEEN   TYPE     REASON                    OBJECT                             MESSAGE
104s        Normal   Scheduled                 pod/hello-node-7567d9fdc9-gs569    Successfully assigned default/hello-node-7567d9fdc9-gs569 to masterkube0
103s        Normal   Pulling                   pod/hello-node-7567d9fdc9-gs569    Pulling image "k8s.gcr.io/echoserver:1.4"
94s         Normal   Pulled                    pod/hello-node-7567d9fdc9-gs569    Successfully pulled image "k8s.gcr.io/echoserver:1.4" in 8.287097001s
93s         Normal   Created                   pod/hello-node-7567d9fdc9-gs569    Created container echoserver
93s         Normal   Started                   pod/hello-node-7567d9fdc9-gs569    Started container echoserver
104s        Normal   SuccessfulCreate          replicaset/hello-node-7567d9fdc9   Created pod: hello-node-7567d9fdc9-gs569
104s        Normal   ScalingReplicaSet         deployment/hello-node              Scaled up replica set hello-node-7567d9fdc9 to 1
30m         Normal   Starting                  node/masterkube0                   Starting kubelet.
30m         Normal   NodeHasSufficientMemory   node/masterkube0                   Node masterkube0 status is now: NodeHasSufficientMemory
30m         Normal   NodeHasNoDiskPressure     node/masterkube0                   Node masterkube0 status is now: NodeHasNoDiskPressure
30m         Normal   NodeHasSufficientPID      node/masterkube0                   Node masterkube0 status is now: NodeHasSufficientPID
30m         Normal   NodeAllocatableEnforced   node/masterkube0                   Updated Node Allocatable limit across pods
29m         Normal   Starting                  node/masterkube0                   Starting kubelet.
29m         Normal   NodeHasSufficientMemory   node/masterkube0                   Node masterkube0 status is now: NodeHasSufficientMemory
29m         Normal   NodeHasNoDiskPressure     node/masterkube0                   Node masterkube0 status is now: NodeHasNoDiskPressure
29m         Normal   NodeHasSufficientPID      node/masterkube0                   Node masterkube0 status is now: NodeHasSufficientPID
29m         Normal   NodeAllocatableEnforced   node/masterkube0                   Updated Node Allocatable limit across pods
29m         Normal   NodeReady                 node/masterkube0                   Node masterkube0 status is now: NodeReady
29m         Normal   RegisteredNode            node/masterkube0                   Node masterkube0 event: Registered Node masterkube0 in Controller
29m         Normal   Starting                  node/masterkube0                   
root@masterkube0:~# 
root@masterkube0:~# 
root@masterkube0:~# kubectl config view
apiVersion: v1
clusters:
- cluster:
    certificate-authority: /root/.minikube/ca.crt
    extensions:
    - extension:
        last-update: Wed, 22 Dec 2021 18:09:25 UTC
        provider: minikube.sigs.k8s.io
        version: v1.24.0
      name: cluster_info
    server: https://10.127.0.31:8443
  name: minikube
contexts:
- context:
    cluster: minikube
    extensions:
    - extension:
        last-update: Wed, 22 Dec 2021 18:09:25 UTC
        provider: minikube.sigs.k8s.io
        version: v1.24.0
      name: context_info
    namespace: default
    user: minikube
  name: minikube
current-context: minikube
kind: Config
preferences: {}
users:
- name: minikube
  user:
    client-certificate: /root/.minikube/profiles/minikube/client.crt
    client-key: /root/.minikube/profiles/minikube/client.key
root@masterkube0:~# 
```

> Создаем сервис для доступа к приложению извне
```
root@masterkube0:~# kubectl expose deployment hello-node --type=LoadBalancer --port=8080
service/hello-node exposed
root@masterkube0:~# kubectl get services
NAME         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
hello-node   LoadBalancer   10.110.91.178   <pending>     8080:30034/TCP   52s
kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          33m
root@masterkube0:~# 
```

```
root@masterkube0:~# minikube service hello-node
|-----------|------------|-------------|--------------------------|
| NAMESPACE |    NAME    | TARGET PORT |           URL            |
|-----------|------------|-------------|--------------------------|
| default   | hello-node |        8080 | http://10.127.0.31:30034 |
|-----------|------------|-------------|--------------------------|
* Opening service default/hello-node in default browser...
  http://10.127.0.31:30034
root@masterkube0:~# 
```


> Смотрим включенные дополнения
```
root@masterkube0:~# minikube addons list
|-----------------------------|----------|--------------|-----------------------|
|         ADDON NAME          | PROFILE  |    STATUS    |      MAINTAINER       |
|-----------------------------|----------|--------------|-----------------------|
| ambassador                  | minikube | disabled     | unknown (third-party) |
| auto-pause                  | minikube | disabled     | google                |
| csi-hostpath-driver         | minikube | disabled     | kubernetes            |
| dashboard                   | minikube | enabled ✅   | kubernetes            |
| default-storageclass        | minikube | enabled ✅   | kubernetes            |
| efk                         | minikube | disabled     | unknown (third-party) |
| freshpod                    | minikube | disabled     | google                |
| gcp-auth                    | minikube | disabled     | google                |
| gvisor                      | minikube | disabled     | google                |
| helm-tiller                 | minikube | disabled     | unknown (third-party) |
| ingress                     | minikube | disabled     | unknown (third-party) |
| ingress-dns                 | minikube | disabled     | unknown (third-party) |
| istio                       | minikube | disabled     | unknown (third-party) |
| istio-provisioner           | minikube | disabled     | unknown (third-party) |
| kubevirt                    | minikube | disabled     | unknown (third-party) |
| logviewer                   | minikube | disabled     | google                |
| metallb                     | minikube | disabled     | unknown (third-party) |
| metrics-server              | minikube | disabled     | kubernetes            |
| nvidia-driver-installer     | minikube | disabled     | google                |
| nvidia-gpu-device-plugin    | minikube | disabled     | unknown (third-party) |
| olm                         | minikube | disabled     | unknown (third-party) |
| pod-security-policy         | minikube | disabled     | unknown (third-party) |
| portainer                   | minikube | disabled     | portainer.io          |
| registry                    | minikube | disabled     | google                |
| registry-aliases            | minikube | disabled     | unknown (third-party) |
| registry-creds              | minikube | disabled     | unknown (third-party) |
| storage-provisioner         | minikube | enabled ✅   | kubernetes            |
| storage-provisioner-gluster | minikube | disabled     | unknown (third-party) |
| volumesnapshots             | minikube | disabled     | kubernetes            |
|-----------------------------|----------|--------------|-----------------------|
root@masterkube0:~# 
```


> Добавляем ingress
```
root@masterkube0:~# minikube addons enable ingress
  - Using image k8s.gcr.io/ingress-nginx/kube-webhook-certgen:v1.1.1
  - Using image k8s.gcr.io/ingress-nginx/kube-webhook-certgen:v1.1.1
  - Using image k8s.gcr.io/ingress-nginx/controller:v1.0.4
* Verifying ingress addon...
* The 'ingress' addon is enabled
root@masterkube0:~# 
root@masterkube0:~# 
root@masterkube0:~# minikube addons list
|-----------------------------|----------|--------------|-----------------------|
|         ADDON NAME          | PROFILE  |    STATUS    |      MAINTAINER       |
|-----------------------------|----------|--------------|-----------------------|
| ambassador                  | minikube | disabled     | unknown (third-party) |
| auto-pause                  | minikube | disabled     | google                |
| csi-hostpath-driver         | minikube | disabled     | kubernetes            |
| dashboard                   | minikube | enabled ✅   | kubernetes            |
| default-storageclass        | minikube | enabled ✅   | kubernetes            |
| efk                         | minikube | disabled     | unknown (third-party) |
| freshpod                    | minikube | disabled     | google                |
| gcp-auth                    | minikube | disabled     | google                |
| gvisor                      | minikube | disabled     | google                |
| helm-tiller                 | minikube | disabled     | unknown (third-party) |
| ingress                     | minikube | enabled ✅   | unknown (third-party) |
| ingress-dns                 | minikube | disabled     | unknown (third-party) |
| istio                       | minikube | disabled     | unknown (third-party) |
| istio-provisioner           | minikube | disabled     | unknown (third-party) |
| kubevirt                    | minikube | disabled     | unknown (third-party) |
| logviewer                   | minikube | disabled     | google                |
| metallb                     | minikube | disabled     | unknown (third-party) |
| metrics-server              | minikube | disabled     | kubernetes            |
| nvidia-driver-installer     | minikube | disabled     | google                |
| nvidia-gpu-device-plugin    | minikube | disabled     | unknown (third-party) |
| olm                         | minikube | disabled     | unknown (third-party) |
| pod-security-policy         | minikube | disabled     | unknown (third-party) |
| portainer                   | minikube | disabled     | portainer.io          |
| registry                    | minikube | disabled     | google                |
| registry-aliases            | minikube | disabled     | unknown (third-party) |
| registry-creds              | minikube | disabled     | unknown (third-party) |
| storage-provisioner         | minikube | enabled ✅   | kubernetes            |
| storage-provisioner-gluster | minikube | disabled     | unknown (third-party) |
| volumesnapshots             | minikube | disabled     | kubernetes            |
|-----------------------------|----------|--------------|-----------------------|
root@masterkube0:~# 
```

***

### **Задача 3: Установить kubectl**

> Устанавливаем kubectl на рабочую машину

```
falconow@falconow:~$ curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 44.4M  100 44.4M    0     0  8823k      0  0:00:05  0:00:05 --:--:-- 9340k
falconow@falconow:~$ chmod +x ./kubectl
falconow@falconow:~$ sudo mv ./kubectl /usr/local/bin/kubectl
[sudo] пароль для falconow: 
falconow@falconow:~$ 
```

```
falconow@falconow:~$ kubectl version --client
Client Version: version.Info{Major:"1", Minor:"23", GitVersion:"v1.23.1", GitCommit:"86ec240af8cbd1b60bcc4c03c20da9b98005b92e", GitTreeState:"clean", BuildDate:"2021-12-16T11:41:01Z", GoVersion:"go1.17.5", Compiler:"gc", Platform:"linux/amd64"}
falconow@falconow:~$ 
```

> Перенес файлы конфигов kubctl для подключния к minikube с сервера на ноутбук.  
Проверим работу:  
```
falconow@falconow:~$ kubectl get pods --namespace=kube-system
NAME                                  READY   STATUS    RESTARTS      AGE
coredns-78fcd69978-zf6z8              1/1     Running   0             24m
etcd-masterkube0                      1/1     Running   0             24m
kube-apiserver-masterkube0            1/1     Running   0             24m
kube-controller-manager-masterkube0   1/1     Running   0             24m
kube-proxy-4ztvs                      1/1     Running   0             24m
kube-scheduler-masterkube0            1/1     Running   0             24m
storage-provisioner                   1/1     Running   1 (23m ago)   24m
falconow@falconow:~$ 
```

>Проверим сервис приложения:
```
falconow@falconow:~$ kubectl get services
NAME         TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
hello-node   LoadBalancer   10.104.209.213   <pending>     8080:32195/TCP   12m
kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          25m
falconow@falconow:~$ 
```

> Пробросил порт до приложения, проверям с помощью curl:

```
falconow@falconow:~/learning/devops-netology$ curl http://62.84.115.45:32195
CLIENT VALUES:
client_address=172.17.0.1
command=GET
real path=/
query=nil
request_version=1.1
request_uri=http://62.84.115.45:8080/

SERVER VALUES:
server_version=nginx: 1.10.0 - lua: 10001

HEADERS RECEIVED:
accept=*/*
host=62.84.115.45:32195
user-agent=curl/7.68.0
BODY:
-no body in request-falconow@falconow:~/learning/devops-netology$
```








