FROM python:3.11.5

WORKDIR /Oficina

COPY . .

RUN apt-get update \
    && apt-get install -y default-libmysqlclient-dev \
    && pip install -r requirements.txt

EXPOSE 8000

CMD ["python","manage.py"]