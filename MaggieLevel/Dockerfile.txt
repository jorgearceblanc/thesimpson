FROM python:latest

RUN mkdir MaggieLevel
RUN mkdir MaggieLevel/General
RUN mkdir MaggieLevel/Homer
RUN mkdir MaggieLevel/Lisa

COPY main.py ./MaggieLevel
COPY requirements.txt ./MaggieLevel

RUN pip install --upgrade pip
RUN pip install -r ./MaggieLevel/requirements.txt

CMD ["python", "MaggieLevel/main.py"]