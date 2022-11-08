FROM python:3.8-alpine
RUN mkdir /app
COPY . /app
WORKDIR /app
RUN pip install tk
CMD [ "python", "./wlcme_pge.py" ]