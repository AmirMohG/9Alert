FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENV TOKEN=default_token_value
ENV USER_ID=default_user_id
CMD ["python", "app.py"]

