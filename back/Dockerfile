FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONFAULTHANDLER 1

WORKDIR /src
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD ["sh", "start_server.sh"]
