FROM python:3.11-bullseye
RUN mkdir /app
COPY *.py /app
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD flask --app app run --host 0.0.0.0