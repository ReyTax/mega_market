FROM python:3.9.0
ENV PYTHONUNBUFFERED=1
WORKDIR /mega_market
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
