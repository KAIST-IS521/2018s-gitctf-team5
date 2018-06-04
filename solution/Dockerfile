FROM debian:latest

# =========Install your package=========
RUN apt-get update && apt-get install -y python vsftpd
RUN apt-get install -y python-pip
RUN pip install pwn
# ======================================

# ======================================
# Build your exploit here
# ======================================


# ======Build and run your exploit=====
COPY exploit.py /bin/exploit
# ======================================

