FROM python:3.10.3-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY handsign_model_v1.h5 handsign_model_v1.h5

COPY main.py main.py

ENV PYTHONUNBUFFERED=1

ENV HOST 0.0.0.0

EXPOSE 8001

CMD ["python", "main.py"]