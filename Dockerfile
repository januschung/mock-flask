FROM python:3.11.0-alpine
WORKDIR /project
ADD . /project
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
