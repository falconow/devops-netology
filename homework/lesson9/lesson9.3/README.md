## Домашнее задание к занятию "09.03 CI\CD"
***
### Подготовка к выполнению
> Создал две виртуальные машины в yandex cloud. Развернул с помощью playbook ПО.
> Проверил готовность Sonarqube и Nexus 
***

### Знакомоство с SonarQube
> Создал проект, установил sonar-scanner.
```
falconow@falconow:~/test/09-ci-03-cicd/mvn$ sonar-scanner --version
INFO: Scanner configuration file: /home/falconow/.local/share/sonar-scanner-4.6.2.2472-linux/conf/sonar-scanner.properties
INFO: Project root configuration file: NONE
INFO: SonarScanner 4.6.2.2472
INFO: Java 11.0.11 AdoptOpenJDK (64-bit)
INFO: Linux 5.11.0-37-generic amd64
```
> Запустил анализатор кода и исправил ошибки.

> Приложил [скриншот](https://github.com/falconow/devops-netology/blob/main/homework/lesson9/lesson9.3/sonar-scanner.jpg) с результатом
***

### Знакомство с Nexus
> Загрузил два артефакта с версиями 8_282 и 8_102

[maven-metadata.xml](https://github.com/falconow/devops-netology/blob/main/homework/lesson9/lesson9.3/maven-metadata.xml)
```buildoutcfg
<?xml version="1.0" encoding="UTF-8"?>
<metadata modelVersion="1.1.0">
  <groupId>netology</groupId>
  <artifactId>java</artifactId>
  <versioning>
    <latest>8_282</latest>
    <release>8_282</release>
    <versions>
      <version>8_102</version>
      <version>8_282</version>
    </versions>
    <lastUpdated>20211006121424</lastUpdated>
  </versioning>
</metadata>
```
***

### Знакомство с Maven
> Скачал и установил maven
```
falconow@falconow:~/test/09-ci-03-cicd/mvn$ mvn --version
Apache Maven 3.8.3 (ff8e977a158738155dc465c6a97ffaf31982d739)
Maven home: /home/falconow/.local/share/apache-maven-3.8.3
Java version: 17, vendor: Private Build, runtime: /usr/lib/jvm/java-17-openjdk-amd64
Default locale: ru_RU, platform encoding: UTF-8
OS name: "linux", version: "5.11.0-37-generic", arch: "amd64", family: "unix"
```

> Запустил mvn package в директории с pom.xml
```
falconow@falconow:~$ tree /home/falconow/.m2/repository/netology/
/home/falconow/.m2/repository/netology/
└── java
    └── 8_282
        ├── java-8_282-distrib.tar.gz
        ├── java-8_282-distrib.tar.gz.sha1
        ├── java-8_282.pom
        ├── java-8_282.pom.lastUpdated
        ├── java-8_282.pom.sha1
        └── _remote.repositories
falconow@falconow:~$ 
```
Файл [pom.xml](https://github.com/falconow/devops-netology/blob/main/homework/lesson9/lesson9.3/pom.xml)
```buildoutcfg
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
 
  <groupId>com.netology.app</groupId>
  <artifactId>simple-app</artifactId>
  <version>1.0-SNAPSHOT</version>
   <repositories>
    <repository>
      <id>my-repo</id>
      <name>maven-public</name>
      <url>http://178.154.222.193:8081/repository/maven-public/</url>
    </repository>
  </repositories>
  <dependencies>
    <dependency>
      <groupId>netology</groupId>
      <artifactId>java</artifactId>
      <version>8_282</version>
      <classifier>distrib</classifier>
      <type>tar.gz</type>
    </dependency> 
  </dependencies>
</project>
```

