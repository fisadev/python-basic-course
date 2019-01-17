FROM python:3.6

RUN mkdir /myweb
WORKDIR /myweb

COPY requirements.txt /myweb/
RUN pip install -r requirements.txt

COPY web.py /myweb/

ENV FLASK_APP web.py
CMD ["flask", "run", "--host=0.0.0.0"]
