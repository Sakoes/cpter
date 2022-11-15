FROM python:3.9

WORKDIR /app/

COPY ./app /app

RUN pip3 install --no-cache-dir --upgrade -r /app/requirements.txt

ENV PYTHONPATH=/app

#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]