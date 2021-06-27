FROM amazoncorretto

RUN yum update && \
    yum install -y wget
WORKDIR /usr/local/jenkins
RUN wget https://get.jenkins.io/war-stable/2.289.1/jenkins.war
EXPOSE 8080
ENTRYPOINT ["java"]
CMD ["-jar","jenkins.war"]