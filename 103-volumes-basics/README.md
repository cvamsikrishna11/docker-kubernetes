------------------ No volume Scenario -----------------------
# Build image
docker build -t my-app .

# Run container
docker run -d -p 8000:5000 --rm my-app

# Connect to container shell and execute commands
docker exec -it container-id bash

cd /data

ls

cat mydata.txt


------------------ volume Scenario -----------------------
# Create volume
docker volume create my-data

# Run container with volume
docker run --rm -d -p 8000:5000 -v my-data:/data my-app

# Connect to container shell and execute commands
docker exec -it container-id bash