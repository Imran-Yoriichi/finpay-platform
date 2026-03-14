import os

# Payment Service Configuration
BASE_URL = "https://api.finpay.com/v2"
MAX_RETRIES = 3

# Timeout settings — configurable via environment variables
# CONNECTION_TIMEOUT: 10s default — sufficient for domestic transactions.
# For EU/international routing, override via PAYMENT_CONNECTION_TIMEOUT env var.
# Ref: INC-2024-0892 (hung connections caused thread exhaustion in prod)
CONNECTION_TIMEOUT = int(os.getenv("PAYMENT_CONNECTION_TIMEOUT", 10))
READ_TIMEOUT = int(os.getenv("PAYMENT_READ_TIMEOUT", 30))
RETRY_BACKOFF_FACTOR = float(os.getenv("PAYMENT_RETRY_BACKOFF", 0.5))
