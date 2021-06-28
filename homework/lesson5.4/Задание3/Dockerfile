FROM node
WORKDIR /usr/local/
RUN apt-get update && git clone https://github.com/simplicitesoftware/nodejs-demo.git
WORKDIR /usr/local/nodejs-demo/
EXPOSE 3000
RUN npm install
CMD ["npm","start"]