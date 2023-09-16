FROM python:3.11-bullseye
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY *.py /app/
COPY .openaikey /app
COPY themes.json /app
ADD templates /app/templates
CMD flask --app app run --host 0.0.0.0 --port 80