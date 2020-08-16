FROM python:3.7-alpine
WORKDIR /bots

COPY bots/fractal_bot.py /bots/
COPY bots/authentication.py /bots/
COPY bots/julia.py /bots/
COPY requirements.txt /tmp

RUN apk update
RUN echo "http://dl-8.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
RUN apk --no-cache --update-cache add gcc gfortran build-base wget freetype-dev libpng-dev openblas-dev
RUN apk add zlib-dev jpeg-dev gcc musl-dev
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

CMD ["python3", "fractal_bot.py"]
