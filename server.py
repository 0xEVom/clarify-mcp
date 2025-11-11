from fastmcp import FastMCP, Context

mcp = FastMCP("clarify-server")

@mcp.tool
async def clarify(ctx: Context, message: str = "What should I clarify?") -> str:
    """
    Ask the user for a free-text clarification and return it.
    Works with Cursor's elicitation UI.
    """
    result = await ctx.elicit(
        message=message,
        response_type=str,
    )
    if result.action != "accept":
        return "User declined or canceled."
    return result.data

if __name__ == "__main__":
    mcp.run()
