FROM python:3.9-alpine
WORKDIR /bot
COPY . .
RUN pip install -r requirements.txt
CMD ["sh", "./start.sh"]

