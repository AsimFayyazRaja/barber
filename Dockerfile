FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN mkdir /barber
RUN apt update
RUN apt install -y cmake
RUN apt-get install ffmpeg libsm6 libxext6 poppler-utils ninja-build  -y
WORKDIR /barber
RUN ls
COPY . .

RUN pip install -r reqs.txt --no-cache-dir

RUN chmod +x start.sh
RUN ls
ENTRYPOINT ["./start.sh"]