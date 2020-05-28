FROM python:3

ADD company.py /

RUN pip install requests

CMD [ "python3", "./company.py" ]