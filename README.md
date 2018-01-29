# offline-legacy

Use s2i to build the image, eg:

s2i build -E .s2i/environment . centos/python-35-centos7 victims-cache

and Run with Docker eg:

docker run -p 8080:8080 victims-cache
