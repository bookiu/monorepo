FROM docker.io/yaxin/debian:latest

ENV PATH="/usr/local/python-venv/bin:$PATH"

RUN apt-get update && \
    apt-get install --no-install-recommends --no-install-suggests -y python3 python3-pip python3-venv && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt

RUN python3 -m venv /usr/local/python-venv && \
    /usr/local/python-venv/bin/pip3 install -r /tmp/requirements.txt
