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
    git

RUN apt-key add /tmp/sgjp.gpg.key \
    && apt-add-repository http://download.sgjp.pl/apt/ubuntu \
    && apt-get update \
    && apt-get install -y --no-install-recommends libmorfeusz2-dev python3-morfeusz2 \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3.6 1

RUN curl -sSL https://get.haskellstack.org/ | sh

WORKDIR /

RUN git clone https://github.com/kawu/concraft-pl.git

WORKDIR /concraft-pl

RUN stack install

RUN python -m pip install \
    requests \
    pandas \
    tqdm \
    setuptools \
    flask \
    markdown

RUN cp /concraft-pl/bindings/python/concraft_pl2.py /usr/lib/python3/dist-packages/concraft_pl2.py

# locale
RUN apt-get install -y --no-install-recommends locales && locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

COPY . /app

#WORKDIR /data

#ENTRYPOINT ["python", "-u" ,"/app/entrypoint.py"]
CMD ["python", "-u" ,"/app/src/server.py"]