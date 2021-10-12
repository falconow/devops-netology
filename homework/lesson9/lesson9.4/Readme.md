## Домашнее задание к занятию "09.04 Jenkins"
### Подготовка к выполнению
> Создал две VM в YandexCloud jenkins-master и jenkins-agent
> 
> С помощью playbook'a подготовил сервера к работе, настроил jenkins, добавил ему
> агента
>

### Задание 1
> Для выполнения задания взял репозиторий с kibana-role https://github.com/falconow/kibana-role
> 
> Добавил в него ключи.

> Создал "Freestyle Job" с командами shell:
 ```
cd kibana-role
pip3 install -r test-requirements.txt
molecule test
```

### Задание 2
> Создал "Declarative Pipeline" с командами shell:
```buildoutcfg
pipeline {
    agent {
        label 'linux'
    }
    stages{
        stage('Checkout') {
            steps{
                git branch: 'main', credentialsId: '2cca28be-e634-40b5-9eac-f4b1bb42e847', url: 'https://github.com/falconow/kibana-role'
            }
        }
        stage('Install molecule') {
            steps{
                sh 'pip3 install -r test-requirements.txt'
            }
        }
        stage('Run molecule'){
            steps{
                sh 'molecule test'
            }
        }
    }

}
```

### Задание 3
> Перенес Declarative Pipeline в репозиторий с ролью в файл Jenkinsfile

### Задание 4
> В отдельном folder, чтобы избежать пересечения имен, создал "Multibranch Pipeline"
> В настройках указал репозиторий и Jenkins файл для автоматической сборки.

### Задание 5-6
> Создал "Scripted Pipeline", заполнил шаблоном.
> 
> Доработал скрипт на использование параметров
> 
> Создал credential для подключения к серверам, организовал согласованность ssh подключений

Scripted Pipeline:
```buildoutcfg
node("linux"){
    stage("Git checkout"){
       git branch: 'main', credentialsId: '2cca28be-e634-40b5-9eac-f4b1bb42e847', url: 'https://github.com/falconow/ansible_8.4'
    }
    
    
    stage("Run playbook"){
        withCredentials([sshUserPrivateKey(credentialsId: 'falconow', keyFileVariable: 'private_key', usernameVariable: 'username')])  {
            if (params.prod_run){
                sh 'ansible-playbook -i inventory/prod.yml --key-file ${private_key} -u ${username} site.yml'
            } 
            else {
                sh 'ansible-playbook -i inventory/prod.yml --key-file ${private_key} -u ${username} site.yml --check --diff'                
            }
        }
        
    }
}
```
>В результате получил собранный стек ELK в Ya.Cloud.

Прилагаю несколько скриншотов:

- [Скриншот1](jenkins1.jpg)
- [Скриншот2](jenkins2.jpg)
- [Скриншот3](jenkins3.jpg)