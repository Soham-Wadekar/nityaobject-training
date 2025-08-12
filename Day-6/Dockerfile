FROM opensuse/leap:15.5

# Install required packages
RUN zypper refresh && \
    zypper install -y \
        python3-kiwi \
        git \
        qemu \
        qemu-tools \
        gptfdisk \
        kpartx \
        dosfstools \
        btrfsprogs \
        squashfs \
        xorriso && \
    zypper clean --all

# Set working directory
WORKDIR /workspace

# Clone KIWI repo into /workspace
RUN git clone https://github.com/OSInside/kiwi

# Start with bash shell
CMD ["/bin/bash"]
