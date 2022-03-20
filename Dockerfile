FROM python:3
LABEL maintainer="xy8000"

#Setting up dependencies
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#Copying Source-Code
COPY ./src/* ./

#ENV-Parameter
ENV PORT 8082
ENV GPIO 4

# Run server
ENTRYPOINT python3 prometheus_server.py -p $PORT -g $GPIO

