FROM python:3.9-slim

WORKDIR ./app

# Install dependencies
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./. /app/

ENV PYTHONPATH=./app
ENV prometheus_multiproc_dir=/tmp

CMD ["python","-m", "app.main"]