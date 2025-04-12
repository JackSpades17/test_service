FROM python:3

WORKDIR /opt/app
COPY requirements.txt .
COPY app.py .
RUN pip3 install -r /opt/app/requirements.txt
RUN apt install postgresql-client-common
EXPOSE 1717
CMD python3 ./app.py

