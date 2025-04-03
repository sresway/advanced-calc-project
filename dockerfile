# Using Python image"
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install required Python packages
RUN pip install --no-cache-dir qrcode[pil]

# Copy all files from the current directory into the container
COPY . .

# Create the output directory for QR codes
RUN mkdir -p qr_codes

# Set environment variables (can be overridden at runtime)
ENV QR_DATA_URL=https://github.com/sresway
ENV QR_CODE_DIR=qr_codes
ENV QR_CODE_FILENAME=my_github_qr.png
ENV FILL_COLOR=black
ENV BACK_COLOR=white

# Define the entrypoint
ENTRYPOINT ["python", "generate_qr.py"]
