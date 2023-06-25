FROM python:3.11.0-alpine
WORKDIR /project
COPY . $WORKDIR
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
