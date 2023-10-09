FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /project/
COPY requirements.txt /project/
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
#COPY backend/ /project/
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
