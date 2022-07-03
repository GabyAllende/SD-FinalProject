
FROM node:latest


WORKDIR /usr/src/app


COPY package*.json ./

RUN npm install

COPY . .


ENV HOST = "broker"
ENV PORT = 1883
ENV TOPIC = "control"
ENTRYPOINT [ "node" , "index.js" ]

