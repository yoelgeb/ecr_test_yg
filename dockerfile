FROM python:3.11.4-alpine3.18

#upgrade pip
RUN pip install --upgrade pip

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /dash_app.py /app/

EXPOSE 8050

CMD ["python", "dash_app.py"]