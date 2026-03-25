FROM python:3.10-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libgl1 \
        libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /Agentic-Hybrid-Rag
WORKDIR /Agentic-Hybrid-Rag

## Install your dependencies here using apt install, etc.

## Include the following line if you have a requirements.txt file.
RUN python -m pip install --upgrade pip
COPY requirements.txt /Agentic-Hybrid-Rag/requirements.txt
RUN pip install -r requirements.txt

COPY ./ /Agentic-Hybrid-Rag

