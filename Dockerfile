FROM python:3.6
MAINTAINER Hal Vong<hvong@universalfinancialcompany.com>

ENV INSTALL_PATH /flasky
RUN mkdir -p $INSTALL_PATH 

WORKDIR $INSTALL_PATH      

COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt    

COPY . .
RUN pip install --editable .                             

CMD gunicorn -b 0.0.0.0:3000 --access-logfile - "flasky.app:create_app()" 
