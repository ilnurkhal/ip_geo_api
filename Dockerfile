FROM ubuntu

RUN apt update
RUN apt install -y python3 python3-pip

WORKDIR /app
COPY api /app

RUN pip3 install -r /app/requirements.txt 
EXPOSE 8080

ENTRYPOINT ["python3", "/app/main.py"] 