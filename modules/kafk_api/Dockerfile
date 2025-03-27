FROM python:3.7-alpine

WORKDIR .

RUN apk update 
RUN apk add bash
RUN apk add openjdk17

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

#kafka broker has its one pod (apache/kafka image) see deployment/udaconnect-kafka-broker.yaml
#RUN export KAFKA_CLUSTER_ID=`./kafka/bin/kafka-storage.sh random-uuid`
#RUN ./kafka/bin/kafka-storage.sh format --standalone -t $KAFKA_CLUSTER_ID -c ./kafka/config/server.properties

EXPOSE 5004

COPY . .

CMD ["flask", "run", "--host", "0.0.0.0"]

