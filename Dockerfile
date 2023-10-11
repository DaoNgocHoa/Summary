FROM nvidia/cuda:12.1.1-runtime-ubuntu22.04
EXPOSE 8001

RUN apt update
RUN apt install -y python3.10 python3-pip

RUN adduser --disabled-password --gecos "" rest_server
USER rest_server
WORKDIR /home/rest_server
ENV PATH="/home/rest_server/.local/bin:${PATH}"
COPY --chown=rest_server:rest_server requirements.txt requirements.txt
COPY --chown=rest_server:rest_server requirements-torchcuda.txt requirements-torchcuda.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements-torchcuda.txt
COPY --chown=rest_server:rest_server . .

ENTRYPOINT ["python3.10", "FastAPI.py"]


