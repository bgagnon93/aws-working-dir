## Kubernetes

Kubernetes is used for container orchestration. I set up this directory to practice the deployment of container services to EKS, but I wound up deploying everything locally using minikube. 

### Prerequisites
* docker
* [kubernetes](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/#install-kubectl-binary-with-curl-on-linux)
    * Kubernetes is an open-source container orchestration system for automating software deployment, scaling, and management.
* [helm](https://helm.sh/docs/intro/install/#from-apt-debianubuntu)
    * Helm is a package manager for Kubernetes that simplifies the management and deployment of applications.
* [minikube](https://minikube.sigs.k8s.io/docs/start/)
    * minikube is local Kubernetes, focusing on making it easy to learn and develop for Kubernetes. 

## Walkthrough

### Repo Setup

First, I created a simple Flask application in `src`, consisting of an `app.py`, `Dockerfile`, and `requirements.txt`. The image was built with ```docker build -t flask-hello-world src/``` and test with ```docker run -p 5000:5000 flask-hello-world```. 

The Kubernetes chart was created with the following command: 
```
helm create flask-hello-world
````

The following updates were made following files in the newly created `flask-hello-world` directory:
* values.yaml:
    * image.repository: flask-hello-world # local image
    * service.port: 5000 # This is the port the Flask application is bound/exposed on
* templates/deployment.yaml: 
    * spec.template.spec.containers[0].image: "{{ .Values.image.repository }}:latest"
    * spec.template.spec.containers[0].env[0].name: PORT
    * spec.template.spec.containers[0].env[0].value: {{ .Values.service.port }}
    * spec.template.spec.containers[0].livenessProbe.httpGet.port: {{ .Values.service.port }}
    * spec.template.spec.containers[0].readinessProbe.httpGet.port: {{ .Values.service.port }}
* templates/service.yaml
    * spec.ports[0].targetPort: {{ .Values.service.port }}

Given the above updates, helm can deploy the image to any Kubernetes cluster loaded with the `flask-hello-world` image. 

### Local Kubernetes
`minikube` is local Kubernetes, and is started with:
```
minikube start
```

When using minikube, it's necessary to load all container images into minikube. Images may be built with the user's installed docker engine and loaded manually into minikube (using `minikube image load flask-hello-world`), or may just be built inside minikube using minikube's docker engine. I found the latter to my preferred process. The commands below sets the docker environment variables so future docker commands were run docker in minikube, then builds the image anew:

```
eval $(minikube docker-env)
docker build -t flask-hello-world src/
```

With the image built and loaded inside the minikube environment, the below helm command will "upgrade" the `flask-hello-world` helm release. 
```
helm upgrade --install flask-hello-world ./flask-hello-world
```

The minikube environment is now managing all objects described by the Helm Chart. To access the exposed ports from each service, port forwarding must be enabled. The following command will setup the port forwarding (run this in a separate terminal, it must stay running):
```
minikube service --all
```

The kubernetes deployment may be restarted at any time by running:
```
kubectl rollout restart deployments/flask-hello-world
```

However, it will be necessary to re-enable the port forwarding with `minikube service --all`. 

### Install a Helm Chart
Grafana is a multi-platform open source analytics and interactive visualization web application. It provides charts, graphs, and alerts for the web when connected to supported data sources. To install Grafana in the Kubernetes cluster, first, add the repository:

```
helm repo add grafana https://grafana.github.io/helm-charts
```

Before the helm chart can be installed, it is necessary to perform a `helm repo update`. Otherwise, helm will not recognize that a repo has been added. Run `helm repo update`, then install the helm chart to the release:
```
helm install grafana grafana/grafana-agent-operator
```

There is no need to run a a `helm upgrade`, but it is necessary to re-run the command to enable port forwarding (`minikube service --all`). 

Launch the endpoint associated with the `argo-argocd-server`. The username is `admin`. The password is obtained by running the following command:
```
kubectl get secret argocd-initial-admin-secret --template={{.data.password}} | base64 --decode
```


#### TOOD EVERYTHING BELOW THIS LINE BELONGS IN ANOTHER EXAMPLE APPLICATION

### Argo CD
Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes. To install Argo CD in the Kubernetes cluster, first, add the repository:
```
helm repo add argo https://argoproj.github.io/argo-helm
```

Argo CD may now be installed:
```
helm install argo argo/argo-cd
```

There is no need to run a a `helm upgrade`, but it is necessary to re-run the command to enable port forwarding (`minikube service --all`). 

Launch the endpoint associated with the `argo-argocd-server`. The username is `admin`. The password is obtained by running the following command:
```
kubectl get secret argocd-initial-admin-secret --template={{.data.password}} | base64 --decode
```

With Argo CD added, it is now possible to manage the deployment of other services. 

#### Uninstall Argo CD
Removing a service is as simple as running `helm uninstall chart`:
```
helm uninstall argo
```


#### Useful K8s commands

* `kubectl get pods`
* `kubectl describe deployments/flask-hello-world`
* `minikube service --all`
* `kubectl get secret argocd-initial-admin-secret --template={{.data.password}} | base64 --decode`
* `kubectl get secret argocd-initial-admin-secret --template={{.data.password}} | base64 --decode`

```
kubectl describe deployments/flask-hello-world
```

```
kubectl get pods
```

```
kubectl --namespace default port-forward deployment/flask-hello-world 5000:5000
```

```
kubectl rollout restart deployments/flask-hello-world
```

PORT FORWARDING TO K8s: lol delete me
```
minikube service flask-hello-world --url
```

PORT FORWARDING FOR EVERYTHING:
```minikube service --all```

```kubectl get secrets```

```kubectl get secret argocd-initial-admin-secret --template={{.data.password}} | base64 --decode```

kubectl get secret argocd-initial-admin-secret --template={{.data.password}} | base64 --decode

kubectl edit secret argocd-initial-admin-secret -o jsonpath="{.data['admin\.password']}" | base64 -d

$2a$10$0zz3NsTIYLltw8.PThf6fegs3sqjH8eVgzOOK6wX4Tept7aJF4lZC

dkF4anRuMWtrSGp6M0xBcw==

echo dkF4anRuMWtrSGp6M0xBcw== | base64 -d

i44XlxrxKQN9Dvu-
