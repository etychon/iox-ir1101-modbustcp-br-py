FROM multiarch/qemu-user-static:x86_64-aarch64 as qemu
FROM arm64v8/python:3.7-slim-stretch

COPY --from=qemu /usr/bin/qemu-aarch64-static /usr/bin
COPY requirements.txt .
COPY start.py .
COPY package_config.ini .

RUN apt-get update \
	&& apt-get clean
RUN pip install --upgrade pip \
	&& pip install --user -r requirements.txt
ENTRYPOINT ["python","start.py"]
