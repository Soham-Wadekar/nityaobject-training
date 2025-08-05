# Base Image
FROM python:3.12.3-slim

# Set working directory
WORKDIR /app

# Copy the contents of the file
COPY . .

# Install dependencies
RUN pip install python-dotenv

# Execute commands
CMD [ "python", "email_operations.py" ]