FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
EXPOSE 80
COPY . /app
ENTRYPOINT [ "streamlit", "run" ]
CMD ["app/app.py"]
