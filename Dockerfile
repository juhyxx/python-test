FROM python:3.11-bookworm

COPY requirements.txt .
COPY ./app ./app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
ENV FLASK_APP=app.py
CMD python3 app run