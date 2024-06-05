FROM python:3.9.19-alpine3.20
EXPOSE 8000
WORKDIR /app 
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app 
ENTRYPOINT ["/bin/sh"]
CMD ["server.sh"]
