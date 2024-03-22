# Rollback or Undo the deployment
kubectl apply -f deployment-v1.yml

kubectl port-forward --address 0.0.0.0 pod/POD-NAME 3001:8080

kubectl apply -f deployment-bug.yml

kubectl port-forward --address 0.0.0.0 pod/POD-NAME 3001:8080

kubectl rollout undo deployment web-app-deployment

kubectl port-forward --address 0.0.0.0 pod/POD-NAME 3001:8080

# readiessProbe & livenessProbe
kubectl apply -f deployment-bug-readiness-probe.yml
kubectl get pods
kubectl logs facebook-deployment-566bd9db44-kbfsj

kubectl apply -f deployment-bug-liveness-probe.yml
kubectl get pods
kubectl port-forward --address 0.0.0.0 pod/POD-NAME 3001:8080
kubectl get pods
kubectl port-forward --address 0.0.0.0 pod/POD-NAME 3001:8080