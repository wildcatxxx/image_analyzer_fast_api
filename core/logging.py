import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s \n %(message)s \n",
    filename="logger.txt"
)

logger = logging.getLogger("image-service")
