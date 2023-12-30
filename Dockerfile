
# Use the official Python base image
FROM python

# Set the working directory in the container
WORKDIR /edzeup

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files to the working directory
COPY . .

# Set the entrypoint command to run the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
