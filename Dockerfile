FROM python:3.9-alpine
WORKDIR /bot
RUN apk add --update --no-cache g++ gcc libxslt-dev
COPY . .
RUN pip install -r requirements.txt
CMD ["sh", "./start.sh"]

