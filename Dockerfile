FROM ubuntu:18.04

ENV APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=1
ADD http://download.sgjp.pl/apt/sgjp.gpg.key /tmp/sgjp.gpg.key

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    software-properties-common \
    gpg-agent \
    curl \
    libtinfo-dev \
    git \
    locales \
    unzip \
    && rm -rf /var/lib/{apt,dpkg,cache,log}

RUN apt-key add /tmp/sgjp.gpg.key \
    && apt-add-repository http://download.sgjp.pl/apt/ubuntu \
    && apt-get update \
    && apt-get install -y --no-install-recommends libmorfeusz2-dev python3-morfeusz2 \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3.6 1 \
    && python -m pip install \
    requests \
    flask \
    markdown \
    && rm -rf /var/lib/{apt,dpkg,cache,log}

COPY docker /app/docker
RUN unzip /app/docker/Concraft-Linux.zip \
    && mv /concraft-pl /usr/local/bin \
    && cp /app/docker/concraft_pl2.py /usr/lib/python3/dist-packages/concraft_pl2.py

# locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

COPY . /app

CMD ["python", "-u" ,"/app/src/server.py"]
