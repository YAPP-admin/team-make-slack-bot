FROM python:latest

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

COPY ./app /code/app
COPY ./properties.py /code/properties.py

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
