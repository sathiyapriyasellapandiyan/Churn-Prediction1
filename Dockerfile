# FROM python:3.11-slim
# WORKDIR /app
# COPY . /app
# RUN pip install --upgrade pip
# RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt
# EXPOSE 8501
# CMD ["streamlit", "run", "app.py"]
FROM  python:3.10-slim
WORKDIR /app
COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt
COPY artifacts /app/artifacts
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

