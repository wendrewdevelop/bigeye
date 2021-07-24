FROM python:3.8

WORKDIR /src

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "vim"]
RUN ["apt-get", "install", "-y", "clamav", "clamav-daemon"]
RUN ["freshclam"]
RUN []

CMD [ "python3", "src/core.py"]