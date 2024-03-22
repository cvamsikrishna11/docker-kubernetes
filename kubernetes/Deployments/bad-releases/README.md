# Rollback or Undo the deployment
kubectl apply -f deployment-v1.yml  
kubectl get pods  
kubectl port-forward --address 0.0.0.0 pod/POD-NAME 3001:8080  

kubectl apply -f deployment-bug.yml  
kubectl get pods  
kubectl port-forward --address 0.0.0.0 pod/POD-NAME 3001:8080  

kubectl rollout undo deployment web-app-deployment  
kubectl get pods  
kubectl port-forward --address 0.0.0.0 pod/POD-NAME 3001:8080  

# readiessProbe
kubectl apply -f deployment-bug-readiness-probe.yml  
kubectl get pods  
kubectl logs POD-NAME  

# livenessProbe (observe the container automatic restart)
kubectl apply -f deployment-bug-liveness-probe.yml  
kubectl get pods  
kubectl port-forward --address 0.0.0.0 pod/POD-NAME 3001:8080  
kubectl get pods  

