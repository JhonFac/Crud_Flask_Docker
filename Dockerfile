FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1

RUN pip install --upgrade pip
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN apk add --update --no-cache mysql-client mysql-dev jpeg-dev mariadb-dev gcc
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers musl-dev zlib zlib-dev 


COPY . /code
WORKDIR /code

# Expose port
EXPOSE 5000

# Start app
# CMD ["python", "main.py"]
CMD ["gunicorn", "--bind", "0.0.0.0:80", "main:app"]
