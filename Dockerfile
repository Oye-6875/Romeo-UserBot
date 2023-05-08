FROM python:3.9.7-slim-buster
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get install git curl python3-pip ffmpeg -y
COPY . /app/
WORKDIR /app/
RUN pip3 install -U -r requirements.txt
CMD python3 -m Romeo
