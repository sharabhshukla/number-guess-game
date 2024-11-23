FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install uv, create a virtual environment, and sync dependencies in a single RUN command
RUN pip install uv && \
    python -m venv .venv && \
    chmod +x .venv/bin/activate && \
    .venv/bin/activate && \
    uv sync

# Expose the port
EXPOSE 8000

# Run the application
ENTRYPOINT [ ".venv/bin/streamlit", "run", "app.py", "--server.port=8000", "--server.address=0.0.0.0" ]