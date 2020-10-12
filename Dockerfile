FROM python:3

WORKDIR /usr/src/EngineeringAssessment

RUN pip install nameko
RUN pip install dahuffman

COPY src/ .
COPY conf.yml .

CMD ["nameko", "run", "--config", "conf.yml", "engineering_assessment"]