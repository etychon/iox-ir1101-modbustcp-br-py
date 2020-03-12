FROM python:3.8.0-slim
COPY . .
RUN apt-get update \
	&& apt-get clean
RUN pip install --upgrade pip \
	&& pip install --user -r requirements.txt
ENTRYPOINT ["python","start.py"]
