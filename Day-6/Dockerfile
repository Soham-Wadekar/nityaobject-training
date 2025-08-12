FROM opensuse/leap:15.5

RUN zypper refresh && \
    zypper install -y --non-interactive python3-kiwi git && \
    zypper clean --all

WORKDIR /workspace

RUN git clone https://github.com/OSInside/kiwi

CMD ["/bin/bash"]
