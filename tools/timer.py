import datetime
from asyncio.log import logger


def get_local_current_time() -> str:
    now = datetime.datetime.now()
    logger.info(f"get_local_current_time called at {now}")
    return now.strftime("%Y-%m-%d@%H:%M:%S")
