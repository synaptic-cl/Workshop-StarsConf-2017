FROM python:3

WORKDIR /src
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD ["bash", "start_server.sh"]
