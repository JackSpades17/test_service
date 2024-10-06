FROM python:3

WORKDIR /app
COPY test_service/requirements.txt .
COPY test_service/app.py .
RUN pip3 install -r /app/requirements.txt
EXPOSE 1717
CMD python3 ./app.py

