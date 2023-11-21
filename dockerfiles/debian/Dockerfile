FROM debian:bookworm-slim

RUN sed -i 's#deb.debian.org#mirrors.tencent.com#g' /etc/apt/sources.list.d/debian.sources && \
    apt-get update && \
    apt-get install -y procps iproute2 net-tools dnsutils tcpdump \
        ngrep netcat-openbsd vim nano rsync curl mariadb-client lrzsz linux-perf sysstat && \
    rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
