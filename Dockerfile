From python:3.9
WORKDIR /app
COPY . .

# python package install
RUN pip install -r requirements.txt

# docker install
RUN apt install -y docker.io

# CMD ["bash", "start.sh"]
CMD ["sleep", "infinity"]
