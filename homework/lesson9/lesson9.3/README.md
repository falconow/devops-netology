```
falconow@falconow:~/test/09-ci-03-cicd/mvn$ mvn --version
Apache Maven 3.8.3 (ff8e977a158738155dc465c6a97ffaf31982d739)
Maven home: /home/falconow/.local/share/apache-maven-3.8.3
Java version: 17, vendor: Private Build, runtime: /usr/lib/jvm/java-17-openjdk-amd64
Default locale: ru_RU, platform encoding: UTF-8
OS name: "linux", version: "5.11.0-37-generic", arch: "amd64", family: "unix"
```


```
falconow@falconow:~/test/09-ci-03-cicd/mvn$ sonar-scanner --version
INFO: Scanner configuration file: /home/falconow/.local/share/sonar-scanner-4.6.2.2472-linux/conf/sonar-scanner.properties
INFO: Project root configuration file: NONE
INFO: SonarScanner 4.6.2.2472
INFO: Java 11.0.11 AdoptOpenJDK (64-bit)
INFO: Linux 5.11.0-37-generic amd64
```


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

2 directories, 6 files
falconow@falconow:~$ 
```