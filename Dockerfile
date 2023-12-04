FROM python:3.11.5

WORKDIR /Oficina

COPY . .

RUN pip install django
RUN pip install mysqlclient

EXPOSE 8000

CMD ["python","manage.py"]