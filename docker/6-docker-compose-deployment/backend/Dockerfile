FROM node:latest

WORKDIR /app

COPY package.json /app/

RUN npm install

COPY . /app/

EXPOSE 80

ENV MONGO_DB_USERNAME=vamsi
ENV MONGO_DB_PASSWORD=secret

CMD [ "npm", "start" ]