[![Build Status](https://dev.azure.com/renjiravindranathan/Python-Flask-K8s/_apis/build/status/mysticrenji.python-flask-mysql-k8s?branchName=main)](https://dev.azure.com/renjiravindranathan/Python-Flask-K8s/_build/latest?definitionId=26&branchName=main)

# Python App created with Flask and MYSQL as Backend

## How to deploy sample application?

1. Create services,  
    `kubectl create -f mysql-service.yaml`  
    `kubectl create -f testapp-service.yaml`

2. Create deployments,  
    `kubectl create -f mysql-deployment.yaml`  
    `kubectl create -f testapp-deployment.yaml`
