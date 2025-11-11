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
./.venv/bin/python3 -m pip install --upgrade pip
./.venv/bin/python3 -m pip install -r requirements.txt
./.venv/bin/python3 server.py
```

macOS notes:
- Always call the venv interpreter directly (`./.venv/bin/python3 -m pip ...`) to avoid PEP 668 issues.
- If you get ENOENT for `.venv/bin/python3`, delete `.venv` and recreate it with `python3 -m venv .venv`.

## Configure in Cursor (`~/.cursor/mcp.json`)

Add this entry:

```json
{
  "mcpServers": {
    "clarify": {
      "command": ".venv/bin/python3",
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

