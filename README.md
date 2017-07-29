## Docker Simple Flask Service

This is a Simple Flask Service as Docker Services example

### Create docker image
```
cd docker_simple_flask_app
docker build -t flask-sample-docker:latest .
```

### Run
```console
docker run -d -p 5000:5000 flask-sample-docker
```

### Access service resource
```
http://localhost:5000/api/v0/machine
```

### Check container is running
```console
docker ps
```

### Stop container
```console
docker stop <container>
```
