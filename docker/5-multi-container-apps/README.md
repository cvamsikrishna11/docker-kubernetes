# Goals Project Docker Setup

This README provides instructions on how to build and run Docker containers for the Goals project, which includes a MongoDB database, a Node.js backend, and a React frontend.

## Prerequisites

Before you begin, ensure you have Docker installed on your system. If you haven't installed Docker yet, follow the instructions on the [Docker official website](https://docs.docker.com/get-docker/).

**Clone the repo & access the project**
```shell
git clone https://github.com/cvamsikrishna11/goals-app-docker.git
cd goals-app-docker
```

**Build the React Frontend Docker Image:**

 ```shell
cd frontend
docker build . -t goals-react
```

**Build the Node Backend Docker Image:**

 ```shell
cd ..
cd backend
docker build . -t goals-node
```


**Create the containers one after another:**

 ```shell
docker run --name mongodb -d --rm --network goals -v data:/data/db -e MONGO_INITDB_ROOT_USERNAME=vamsi -e MONGO_INITDB_ROOT_PASSWORD=secret mongo
docker run --name goals-backend -d --rm --network goals -p 80:80 goals-node:latest
docker run --name goals-frontend --network goals -d --rm -p 3000:3000 goals-react:latest
```

**Access the app**
Open browser and access: http://localhost:3000/ 


**To clear the setup**
```shell
docker stop $(docker ps -q)
```