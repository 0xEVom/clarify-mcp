# clarify-mcp

Minimal MCP server that exposes a single `clarify` tool to elicit free-text clarification from the user via Cursor's elicitation UI.

## Features

- `clarify(message: str = "What should I clarify?") -> str`: prompts for input and returns the user's response.

## Project layout

- `server.py`: main MCP server using `fastmcp`.

## Requirements

- Python 3.10+

## Quickstart

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
python server.py
```

## Configure in Cursor (`~/.cursor/mcp.json`)

Add this entry:

```json
{
  "mcpServers": {
    "clarify": {
      "command": ".venv/bin/python",
      "args": [
        "server.py"
      ],
      "cwd": "/path/to/clarify-mcp"
    }
  }
}
```

Restart Cursor to load the new MCP server.

## License

MIT

