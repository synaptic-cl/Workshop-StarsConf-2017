FROM python:3-alpine

WORKDIR /src
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD ["sh", "start_server.sh"]
