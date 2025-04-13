from asyncio.log import logger
import datetime
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("mix_server")


@mcp.tool()
def get_local_current_time():
    now = datetime.datetime.now()
    logger.info(f"get_local_current_time called at {now}")
    return now.strftime("%Y-%m-%d@%H:%M:%S")


# Entry point to run the server
if __name__ == "__main__":
    mcp.run()
