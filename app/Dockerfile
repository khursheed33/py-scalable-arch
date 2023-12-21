FROM alpine:latest

# Install required dependencies
RUN apk --update --no-cache add \
    python3 \
    py3-pip \
    build-base \
    python3-dev \
    linux-headers \
    pcre-dev \
    && python3 -m venv /venv

# Set up the working directory
WORKDIR /app

# Copy the application files into the container
COPY . /app

# Activate the virtual environment
ENV PATH="/venv/bin:$PATH"

# Install required Python packages
RUN set -e; \
    pip install --upgrade pip setuptools; \
    pip --no-cache-dir install -r requirements.txt;

# Install build dependencies for uWSGI
RUN apk --no-cache --virtual .build-deps add \
        gcc \
        libc-dev \
        ; \
    pip install uwsgi; \
    apk del .build-deps;

# Your additional commands to start uWSGI or your application
CMD ["uwsgi", "--ini", "app.ini"]
