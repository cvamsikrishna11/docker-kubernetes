# To run pod with command
kubectl run nginx --image=nginx

# To run the kubernetes manifest file objects to create pod
kubectl apply -f nginx.yml

# To check running pods
kubectl get pods

# To check running pods with wider details
kubectl get pods -o wide

# To port-forward the traffic to pod 
kubectl port-forward --address 0.0.0.0 pod/nginx 3001:80
# Note: By default, without the --address flag, kubectl port-forward binds to 127.0.0.1 (localhost), which means the service can only be accessed locally from the host machine. Using --address 0.0.0.0 changes this behavior, allowing external access. 

# To run on background
nohup kubectl port-forward --address 0.0.0.0 pod/nginx 3001:80 > /dev/null 2>&1 &


# To check logs of a pod with name
kubectl logs nginx

# Executing commands on the pod
kubectl exec nginx -- ls

# To run interactive shell on the pod
kubectl exec -it nginx -- bash

# Lets try and change the application code once we connect to the container
echo "it works!" > /usr/share/nginx/html/index.html

Now reload the page, to see the changes!

# Come out of pod/container by typing exit and hit enter

# Terminating the pod directly with name (also check if its restarting)
kubectl delete pod nginx

# Terminating the pod by applying delete action on the manifest file
kubectl delete -f nginx.yaml

# To get all events in the environment
kubectl get eventss
