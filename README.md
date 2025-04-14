# Mix Server

A Python-based server that provides local time functionality through MCP (Model Control Protocol).

## Features

- Get current local time in various formats
- Open files and URLs in the default web browser
- Simple and lightweight implementation
- Built with FastMCP for easy integration
- Uses uv for fast and reliable dependency management

## Prerequisites

- Python 3.x
- uv package manager (recommended for build and environment management)
- Cursor IDE (for development)

## Project Structure

The project consists of the following key files:

- `main.py`: The main server implementation with the time functionality
- `server.py`: Server configuration and setup
- `pyproject.toml`: Project configuration and dependencies
  - Defines project metadata (name, version, description)
  - Specifies Python version requirement (>=3.12)
  - Lists project dependencies (mcp[cli]>=1.6.0)
- `.python-version`: Specifies the Python version for the project
- `.gitignore`: Git ignore rules for the project
- `mcp.json.example`: Example configuration file for Cursor IDE
  - Contains MCP server settings for local development
  - Should be copied to `~/.cursor/mcp.json` for Cursor integration
  - Defines server configurations for time and sequential thinking services

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd mix-server
```

2. Create and activate virtual environment using uv:
```bash
uv venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

3. Install dependencies using uv:
```bash
uv pip install .
```

4. Set up Cursor configuration:
```bash
cp mcp_config.json.example ~/.cursor/mcp.json
```

## Development

The project uses uv for all Python-related operations:

- Environment management: `uv venv`
- Package installation: `uv pip install .`
- Running the server: `uv run main.py`

## Usage

The server provides the following functionality:

- `get_local_current_time()`: Returns the current local time in the format "YYYY-MM-DD@HH:MM:SS"
- `open_file_or_url_in_browser(target)`: Opens a file or URL in the default web browser
  - Supports both local files and web URLs
  - For URLs: Use complete URL with protocol (e.g., "https://www.google.com")
  - For files: Use local file path (relative or absolute)
  - Returns a message indicating the result of the operation

To start the server:
```bash
uv run main.py
```

## Configuration

The server uses the following configuration:
- Local timezone: Asia/Shanghai
- Default time format: %Y-%m-%d@%H:%M:%S

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]
