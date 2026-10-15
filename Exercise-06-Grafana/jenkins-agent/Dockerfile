FROM jenkins/inbound-agent:latest-jdk21

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends python3 python3-pip ca-certificates curl \
    && rm -rf /var/lib/apt/lists/*

COPY --from=docker:cli /usr/local/bin/docker /usr/local/bin/docker

USER jenkins
