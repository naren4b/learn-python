FROM python:3.14.0
COPY app.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
ENTRYPOINT ["python","app.py"]
