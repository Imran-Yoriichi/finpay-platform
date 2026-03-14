import os

# Payment Service Configuration
BASE_URL = "https://api.finpay.com/v2"
MAX_RETRIES = 3

# Timeout settings — configurable via environment variables
# Added after incident INC-2024-0892 (hung connections → thread exhaustion)
CONNECTION_TIMEOUT = int(os.getenv("PAYMENT_CONNECTION_TIMEOUT", 10))
READ_TIMEOUT = int(os.getenv("PAYMENT_READ_TIMEOUT", 30))
RETRY_BACKOFF_FACTOR = float(os.getenv("PAYMENT_RETRY_BACKOFF", 0.5))
