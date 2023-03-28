From python:3.9
WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

# CMD ["bash", "start.sh"]
CMD ["sleep", "infinity"]
