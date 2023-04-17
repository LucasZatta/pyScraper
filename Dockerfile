FROM python:3.8.10

RUN pip freeze > requirements.txt

RUN pip3 install -r requirements.txt

RUN python app.py