FROM python:3.10-alpine
ENV HOME_DIR /app/posts
WORKDIR $HOME_DIR
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . $HOME_DIR
EXPOSE 8001
CMD ["python3","main.py"]

