# docker build -t flask_tutorial . -> Run command in the directory where Dockerfile is located

# FROM python:3.11.4
# EXPOSE 5050
# WORKDIR /PythonFlask
# RUN pip install flask_sqlalchemy psycopg2-binary python-dotenv flask-cors flask-bcrypt flask-jwt-extended click flask-httpauth
# COPY . .
# ENV FLASK_APP=app.py
# CMD ["python", "/flaskProject/app.py"]

FROM python:3.11.4

# Expose Flask port
EXPOSE 5000

# Set the working directory to the project root
WORKDIR /PythonFlask

# Copy everything into /app
COPY . .

# Install Python dependencies
RUN pip install flask_sqlalchemy psycopg2-binary python-dotenv flask-cors flask-bcrypt flask-jwt-extended click flask-httpauth

# Set environment variables for Flask
ENV FLASK_APP=flaskProject/app.py
ENV FLASK_RUN_HOST=0.0.0.0
# ENV PYTHONPATH=/app

# Run the Flask application
CMD ["flask", "run"]