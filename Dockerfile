FROM ubuntu:18.04

# Use Bash
SHELL ["/bin/bash", "-c"]

# Change locale
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Update and install python
RUN apt-get -y update
RUN apt -y install python3.6 python3-pip

# Upgrade pip
RUN pip3 install --upgrade pip

# Copy app contents to Docker image
COPY . /app

# Install virtualenv
RUN pip3 install virtualenv

# Create virtual environment
RUN python3 -m virtualenv app/cg-venv
RUN source app/cg-venv/bin/activate

RUN python3 --version

# Install requirements
RUN pip3 install -r app/requirements-server.txt
RUN pip3 install -r app/requirements-cpu.txt

# Run tests
# Do tests here :)

# Set entrypoint
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

