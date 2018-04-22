FROM ubuntu

RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8
RUN apt-get update && apt-get install -y git curl vim strace tmux htop tar make
RUN apt-get install -y python3-dev tcl-dev gcc g++ libffi-dev python3-pip

RUN mkdir /src

COPY ./run.py /src
COPY ./requirements.txt /src
COPY ./env.sh /src

RUN pip3 install --upgrade pip
RUN cd /src && pip3 install -r requirements.txt

ENV CONSUMER_KEY='nrJ9uHeiZdUQQBHF9D9EdZQF7'
ENV CONSUMER_SECRET='DhUAac6hLOR6wDhf5XcwwzhVGBI2HFRjznXFghfXL7yOloxote'
ENV ACCESS_TOKEN='89558243-Fy9kHlIi3crMnopFOxMul961w1gKpeCJz504cCjR7'
ENV ACCESS_SECRET='YOyFDb5AZAkjvowjMUWahnWaIPqboXxXLoIpeCTrzHr2c'
ENV USERNAME="85b49ace-a428-49dc-be76-42251b884193"
ENV PASSWORD="LdBBLrYfmHh4"

RUN cd /src && mkdir moodmarbles

COPY ./moodmarbles /src/moodmarbles/

EXPOSE 5001
WORKDIR /src

CMD python3 /src/run.py
