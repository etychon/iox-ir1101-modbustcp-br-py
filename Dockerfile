FROM python:3.8.0-slim
COPY start.py /app
RUN apt-get update \
&& apt-get clean
WORKDIR app
RUN pip install --user -r requirements.txt
ENTRYPOINT python start.py
