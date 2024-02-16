# https://hub.docker.com/_/mongo

# Create a Docker volume for MongoDB to persist data:
docker volume create mongodb-data


# Run a MongoDB container using the created volume for data persistence:

docker run -d --name mongo -v mongodb-data:/data/db -e MONGO_INITDB_ROOT_USERNAME=mongoadmin -e MONGO_INITDB_ROOT_PASSWORD=secret mongo

# Search for mongodb container IP with below command and replace the IP in the app.py (line 14)
docker inspect MONGO-CONTAINER-ID

# Build app
docker build -t flask-app .

# Create a Docker volume for the Flask application logs:
docker volume create flask-logs

# Run container
docker run -d --rm -p 5001:5000 --name flask-app-container -v flask-logs:/app/logs flask-app

# Perform POST action on http://localhost:5001/students via POSTMAN
{
    "student_name":"naruto",
    "course_name": "leaf village"
}

# Perform GET action http://localhost:5001/enroll via POSTMAN or browser