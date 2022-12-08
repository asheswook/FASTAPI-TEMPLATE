FROM python:3.11.1-slim

COPY . /root/FASTAPI-APP
RUN cd /root/FASTAPI-APP && \
    pip3 install -r requirements.txt


CMD cd /root/FASTAPI-APP && \
    uvicorn app.main:app --host=0.0.0.0 --port=8000 --reload --reload-dir /root/FASTAPI-APP/app