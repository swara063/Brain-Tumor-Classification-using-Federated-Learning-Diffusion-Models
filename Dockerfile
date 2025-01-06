# Use the official Python 3.10 image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the kaggle.json file into the .config/kaggle directory
COPY .config/kaggle/kaggle.json /root/.config/kaggle/

# Set permissions for kaggle.json
RUN chmod 600 /root/.config/kaggle/kaggle.json

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Command to run the app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
