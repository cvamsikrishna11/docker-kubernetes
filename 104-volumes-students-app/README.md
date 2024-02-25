# https://hub.docker.com/_/mongo

# Create a Docker volume for MongoDB to persist data:
docker volume create mongodb-data

# Run a MongoDB container using the created volume for data persistence:

docker run -d --name mongo -v mongodb-data:/data/db -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=Admin12345 mongo

# Search for mongodb container IP with below command and replace the IP in the app.py (line 14)
docker container inspect MONGO-CONTAINER-ID

# Build app
docker build -t flask-app .

# Run container - without the volume for logs

docker run -d --rm -p 5001:5000 --name flask-app flask-app

# Run container - with the volume for logs
docker volume create flask-logs
docker run -d --rm -p 5001:5000 --name flask-app -v flask-logs:/app/logs flask-app
