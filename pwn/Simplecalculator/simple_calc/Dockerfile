FROM gcc:latest

WORKDIR /app

COPY . /app

RUN apt update && apt install socat -y && \
groupadd -r simple_calc \
&& useradd -r -g simple_calc simple_calc && chmod +x runservice.sh && chmod +x run.sh

USER simple_calc

CMD ["./runservice.sh"]
