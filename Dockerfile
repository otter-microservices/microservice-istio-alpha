FROM python

WORKDIR /app

COPY . /app

RUN apt-get update -y && apt-get install -y dnsutils curl

RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT [ "python" ]

CMD [ "service.py" ]
