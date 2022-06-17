FROM python:3.10
RUN pip install --upgrade pip
WORKDIR /
COPY requirements.txt .
RUN pip3 install -r requirements.txt
EXPOSE 8050
COPY . .
CMD ["python","main.py"]
