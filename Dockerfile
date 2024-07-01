FROM python:3.12.3

ENV PYTHONUNBUFFERED=1
ENV TZ=America/New_York

WORKDIR /app
COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 3000
CMD python ./server.py