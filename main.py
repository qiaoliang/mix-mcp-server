from asyncio.log import logger
import datetime
from mcp.server.fastmcp import FastMCP
from tools.browser import open_file_or_url
from tools.timer import get_local_current_time

mcp = FastMCP("mix_server")


@mcp.tool()
def get_local_current_time() -> str:
    return get_local_current_time()


@mcp.tool()
def open_file_or_url_in_browser(target: str) -> str:
    """Open a file or URL in the default web browser.

    Args:
        target (str): The file path or URL to open

    Returns:
        str: A message indicating the result of the operation
    """
    result = open_file_or_url(target)
    logger.info(f"Browser tool returned: {result}")
    return result


# Entry point to run the server
if __name__ == "__main__":
    mcp.run()
