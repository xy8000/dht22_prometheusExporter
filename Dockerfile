FROM python:3
LABEL maintainer="xy8000"

#Setting up dependencies
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#Copying Source-Code
COPY ./src/* .

ENV GPIO_PIN=5
ENV PORT=8080

# Run server
CMD [ "python", "./prometheus_server.py", "-p ${PORT}", "-g ${GPIO_PIN}"]
