### Docker Simple Flask Service

This is a Simple Flask Service as Docker Services example

## Run
```console
cd docker_simple_flask_app
docker build -t flask-sample-docker:latest .
docker run -d -p 5000:5000 flask-sample-docker
```

##Check if running
```console
docker ps
```

