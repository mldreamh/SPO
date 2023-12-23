FROM python:3.9.13

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

#specify the port number the container should explose
EXPOSE 5000

#run the application
CMD ["python", "./laba1.py"]
