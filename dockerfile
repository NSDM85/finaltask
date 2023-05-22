FROM python:3.10.6
WORKDIR /newapp
COPY . /newapp
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8081
ENTRYPOINT ["python3"]
CMD ["variant3.py"]
