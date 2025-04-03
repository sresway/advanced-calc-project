"""QR Code Generator Script"""

import qrcode
import os
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

# Load environment variables
data_url = os.getenv("QR_DATA_URL", "https://github.com/sresway")  # Replace with your GitHub username
output_dir = os.getenv("QR_CODE_DIR", "qr_codes")
filename = os.getenv("QR_CODE_FILENAME", "my_github_qr.png")
fill_color = os.getenv("FILL_COLOR", "black")
back_color = os.getenv("BACK_COLOR", "white")

# Create directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Build the full output path
output_path = os.path.join(output_dir, filename)

try:
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(data_url)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(output_path)

    logging.info(f"QR code saved to: {output_path}")
    logging.info(f"Encoded URL: {data_url}")

except Exception as e:
    logging.error(f"Failed to generate QR code: {e}")
