FROM python:3.11.0-alpine
WORKDIR /project
COPY app $WORKDIR
RUN pwd
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
