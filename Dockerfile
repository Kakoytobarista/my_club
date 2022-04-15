FROM python:3.8.5
WORKDIR /code
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY /my_club .

#  TODO: Now its useles, but if i will(so i will) have more stages i will using that for build in docker-compose