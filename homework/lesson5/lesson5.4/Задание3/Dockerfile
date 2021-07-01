FROM node
WORKDIR /usr/local/
RUN apt-get update && git clone https://github.com/simplicitesoftware/nodejs-demo.git
WORKDIR /usr/local/nodejs-demo/
RUN npm install
EXPOSE 3000
ENTRYPOINT ["npm"]
CMD ["start","0.0.0.0"]