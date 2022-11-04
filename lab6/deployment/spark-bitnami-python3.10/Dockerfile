FROM bitnami/python:3.10 as build

FROM bitnami/spark:3.3

COPY --from=build /opt/bitnami/python/ /opt/bitnami/python/
# Update the guava library needed by the gcs connector
RUN mv /opt/bitnami/spark/jars/guava-14.0.1.jar /opt/bitnami/spark/jars/guava-14.0.1.jar.bk
COPY *.jar /opt/bitnami/spark/jars/