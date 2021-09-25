# for setting up docker-container, see https://www.docker.com/blog/containerized-python-development-part-1/

# set base image (os)
FROM python:3.8

# set working directory in the docker container
WORKDIR /app

# copy source and app requirements
COPY ./src /app
COPY ./requirements.txt /app

# install dependencies to working directory
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# run on container command
CMD ["python", "app.py"]