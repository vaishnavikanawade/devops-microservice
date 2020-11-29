FROM mysql
ENV MYSQL_ROOT_PASSWORD pucsd123
ENV MYSQL_DATABASE dep
ENV MYSQL_USER pucsd
ENV MYSQL_PASSWORD pucsd123
ADD /module/script.sql /docker-entrypoint-initdb.d
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip
RUN mkdir -p /app
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
COPY main.py /app 
