FROM debian:latest
MAINTAINER Nilo Alexandre "n1lux.comp@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip python3-dev build-essential
COPY . /web
WORKDIR /web
RUN pip3 install -r requirements.txt 
ENTRYPOINT ["python3"]
CMD ["web/app.py"]
