FROM python:3.11-alpine

WORKDIR /app

COPY . /app

RUN apk add --no-cache bash

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH="/app"

RUN find . -name "*.py" | xargs pylint --errors-only

RUN python3 -m unittest discover -s tests

COPY lookup_cli.py /usr/local/bin/lookup-cli

RUN chmod +x /usr/local/bin/lookup-cli

CMD ["bash"]
