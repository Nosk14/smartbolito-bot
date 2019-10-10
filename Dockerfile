FROM resin/rpi-raspbian
RUN apt-get update \
    && apt-get install python3 python3-dev python3-pip gcc g++
RUN pip3 install --upgrade setuptools pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY src /usr/local/smartbolito-bot/
CMD python3 /usr/local/smartbolito-bot/smartbolito.py