FROM python:3.7-alpine

# Dependencies
COPY requirements.txt /
RUN pip install -r /requirements.txt

# App config
COPY . /app
WORKDIR /app

EXPOSE 5000

CMD ["python", "api.py"]