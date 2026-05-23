import os

# DANGEROUS: Debug mode enabled in production!
DEBUG = True
ENVIRONMENT = os.getenv("ENVIRONMENT", "production")

# DANGEROUS: Hardcoded localhost URL instead of environment variable
API_URL = "http://localhost:5000"
API_TIMEOUT = int(os.getenv("API_TIMEOUT", "30"))

# Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///app.db")

# JWT Configuration
JWT_SECRET = os.getenv("JWT_SECRET", "change-this-secret-in-production")
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_HOURS = 24

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Feature Flags
ENABLE_ANALYTICS = os.getenv("ENABLE_ANALYTICS", "true").lower() == "true"
