FROM python:3
ARG DATABASE_URL
WORKDIR /opt/app
COPY templates requirements.txt app.py .
RUN pip3 install -r /opt/app/requirements.txt
EXPOSE 1717
#CMD python3 ./app.py $DATABASE_URL

