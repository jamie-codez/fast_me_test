FROM python:3.10-alpine
ENV HOME_DIR /app/posts
WORKDIR $HOME_DIR
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["python3"]
CMD ["python3","main.py"]

