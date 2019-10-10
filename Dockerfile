FROM python:3.6-slim
RUN apt-get update \
    && apt-get install build-essential gcc g++ -y
RUN pip3 install --upgrade setuptools pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY src /usr/local/smartbolito-bot/
WORKDIR /usr/local/smartbolito-bot
CMD python smartbolito.py
