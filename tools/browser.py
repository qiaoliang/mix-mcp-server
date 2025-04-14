import sys
import webbrowser
import os
from asyncio.log import logger
import datetime


def open_file_or_url(target) -> str:
    """Open a file or URL in the default web browser.

    Args:
        target (str): The file path or URL to open

    Returns:
        str: A message indicating the result of the operation
    """
    now = datetime.datetime.now()
    logger.info(f"open_file_or_url called at {now} with {target}")
    try:
        if target.startswith(('http://', 'https://')):
            # 如果是URL，直接用浏览器打开
            webbrowser.open(target)
            return f"Opened URL: {target} at {now.strftime('%Y-%m-%d@%H:%M:%S')}"
        elif os.path.exists(target):
            # 如果是本地文件，构建文件的URL并打开
            file_url = 'file://' + os.path.abspath(target)
            webbrowser.open(file_url)
            return f"Opened file: {target} at {now.strftime('%Y-%m-%d@%H:%M:%S')}"
        else:
            error_msg = f"Error: {target} is neither a valid URL nor an existing file."
            logger.error(error_msg)
            return error_msg
    except Exception as e:
        error_msg = f"An error occurred: {e}"
        logger.error(error_msg)
        return error_msg


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path_or_url>")
    else:
        target = sys.argv[1]
        open_file_or_url(target)
