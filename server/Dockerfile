FROM python:alpine
LABEL maintainer="Jason Shepherd"

WORKDIR /usr/src/app
CMD ["mkdir", "service"]
COPY service service
COPY server.py .

EXPOSE 8000

CMD [ "python", "./server.py" ]