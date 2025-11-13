FROM nvcr.io/nvidia/pytorch:25.06-py3

# Most dependencies are already in the base image
# Only install what's missing for Cursor and development
RUN apt-get update && apt-get install -y \
    ripgrep \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /workspace

# Install Python packages
RUN pip install --no-cache-dir nengo nengo-gui

# Expose port for Nengo GUI
EXPOSE 8080

