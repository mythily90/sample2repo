FROM python:alpine3.7 
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt 
EXPOSE 5001 
ENTRYPOINT [ "python" ] 
CMD [ "api.py" ] 
