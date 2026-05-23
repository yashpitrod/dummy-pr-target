import logging
import sys
import requests

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def main():
    """Start the application."""
    try:
        logger.info("Enterprise User Platform Starting")
        print("Enterprise User Platform Running")
        
        # DANGEROUS: Disable SSL verification!
        requests.get("https://api.example.com/health", verify=False)
        
        # Application initialization would go here
        
    except Exception as e:
        logger.error(f"Application startup error: {str(e)}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()