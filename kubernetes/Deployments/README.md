# To create a new deployment with image nginx
kubectl create deployment nginx-deployment --image=nginx

# Build the image (replace with your details)
docker build . -t vamsichunduru/facebook-practice

# Docker login
docker login

# Push the image to repo(replace with your details)
docker push vamsichunduru/facebook-practice

# To run the manifest file
kubectl apply -f deployment.yml

# To check deployments
kubectl get deloyments

# To check the pods
kubectl get pods
kubectl get all
# To desribe the deployment
kubectl describe deployment facebook-deployment

# To expose the traffic on the pod
nohup kubectl port-forward --address 0.0.0.0 pod/facebook-deployment-55677cfc9d-v92ls 3001:80 > /dev/null 2>&1 &

# To check the pod logs
kubectl logs facebook-deployment-7bf8c99ff-qhqjq

# Lets kill the pod to see what happens
kubectl delete pod facebook-deployment-7bf8c99ff-qhqjq

# Check pods immediatly
kubectl get pods

# So the observation at this point is, deployment is automatically restarting the desired pods even if the existing ones are terminated!

# Note: But we cant access the traffic on the same port again as at the moment traffic is on pod level with pod ip

# Observing the sclability up
change  replicas: 1 to   replicas: 10 in the deployment.yml and reapply the manifest file with 

kubectl apply -f deployment.yml

kubectl get pods

# Scaling down 
do the same process with replicas: 2

# Rolling updates
kubectl apply -f deployment-v1-rollout.yml

# maxSurge & maxUnavailable
kubectl apply -f deployment-roll-out-rate.yml

# Recreate strategy
kubectl apply -f deployment-recreate.yml