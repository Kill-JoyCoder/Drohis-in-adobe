FROM --platform=linux/amd64 python:3.12.1-alpine

WORKDIR /Task-1A

# RUN apt-get update \
#     && apt-get upgrade -y \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*
# Copy the processing script
COPY main.py .

# Run the script
CMD ["python", "main.py"] 
