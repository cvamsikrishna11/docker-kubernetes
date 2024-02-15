FROM python:alpine

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "app.py" ]